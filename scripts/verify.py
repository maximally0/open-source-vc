#!/usr/bin/env python3
"""
Validate the directory. Runs in CI on every push and pull request.

Two modes:

    --offline   structural checks only (no network). Schema, duplicates,
                categories, tiers, licences present, attribution, markers,
                generated-file staleness.

    (default)   offline checks + live GitHub lookups: URL liveness, archived
                status drift, licence drift, and snapshot age.

Exit code is 0 only when there are no errors. Warnings do not fail the build.

Usage:
    python scripts/verify.py --offline
    python scripts/verify.py
    python scripts/verify.py --json report.json
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CURATION = ROOT / "curation.yaml"
SNAPSHOT = ROOT / "metadata" / "snapshot.json"
REPOS_JSON = ROOT / "metadata" / "repositories.json"
REPOS_YAML = ROOT / "metadata" / "repositories.yaml"
CATEGORIES_DIR = ROOT / "categories"
README = ROOT / "README.md"

REQUIRED_ITEM_FIELDS = ("name", "category", "tier", "kind", "vc_use_case", "why_interesting",
                        "vc_relevance")
VALID_TIERS = {"essential", "recommended", "experimental", "research"}
VALID_RELEVANCE = {"native", "adaptable", "infrastructure"}
VALID_KINDS = {"software", "dataset", "framework", "standard", "research"}
REQUIRED_README_REGIONS = ("stats", "categories", "essentials", "updated", "stages", "vcnative")
REQUIRED_FILES = (
    "README.md", "LICENSE", "CONTRIBUTING.md", "CHANGELOG.md", "ROADMAP.md",
    "SOURCES.md", "METHODOLOGY.md", "VC_WORKFLOW.md", "COMPARISON.md", "curation.yaml",
    "GAPS.md", "UNFAIR_ADVANTAGE.md", "STARTER_PACK.md", "HIDDEN_GEMS.md",
)

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def token() -> str | None:
    for env in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(env):
            return os.environ[env]
    try:
        return subprocess.run(["gh", "auth", "token"], capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Offline checks
# ---------------------------------------------------------------------------

def check_files() -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            err(f"missing required file: {rel}")
    if not CATEGORIES_DIR.is_dir():
        err("missing categories/ directory")
    else:
        if not list(CATEGORIES_DIR.glob("*.md")):
            err("categories/ contains no pages")


def check_markers() -> None:
    if not README.exists():
        err("README.md missing")
        return
    text = README.read_text(encoding="utf-8")
    for key in REQUIRED_README_REGIONS:
        if f"<!-- BEGIN GENERATED:{key} -->" not in text or f"<!-- END GENERATED:{key} -->" not in text:
            err(f"README missing GENERATED markers for region '{key}'")
    if len(text) < 3000:
        warn("README looks thin (<3000 chars)")


def check_json_malformed() -> None:
    for p in (REPOS_JSON, SNAPSHOT):
        if not p.exists():
            err(f"missing {p.relative_to(ROOT)}")
            continue
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            err(f"malformed JSON in {p.relative_to(ROOT)}: {exc}")


def check_yaml_malformed() -> None:
    for p in (CURATION, REPOS_YAML):
        if not p.exists():
            err(f"missing {p.relative_to(ROOT)}")
            continue
        try:
            yaml.safe_load(p.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            err(f"malformed YAML in {p.relative_to(ROOT)}: {exc}")


def load_inputs() -> tuple[dict, dict, list[dict]]:
    curation = yaml.safe_load(CURATION.read_text(encoding="utf-8")) or {}
    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8")) if SNAPSHOT.exists() else {}
    published = []
    if REPOS_JSON.exists():
        published = json.loads(REPOS_JSON.read_text(encoding="utf-8")).get("repositories", [])
    return curation, snapshot, published


def check_items(curation: dict, snapshot: dict) -> None:
    repos = curation.get("repos") or []
    if not repos:
        err("curation.yaml lists no repositories")
        return
    if len(repos) < 20:
        warn(f"only {len(repos)} repositories curated")

    for i, item in enumerate(repos, 1):
        label = item.get("name") or f"<item {i}>"
        for field in REQUIRED_ITEM_FIELDS:
            if not item.get(field):
                err(f"{label}: missing required field '{field}'")
        name = item.get("name", "")
        if name and name.count("/") != 1:
            err(f"{label}: 'name' must be owner/repo")
        if item.get("tier") and item["tier"].lower() not in VALID_TIERS:
            err(f"{label}: invalid tier '{item['tier']}'")
        if item.get("kind") and item["kind"].lower() not in VALID_KINDS:
            err(f"{label}: invalid kind '{item['kind']}'")
        if item.get("vc_relevance") and item["vc_relevance"].lower() not in VALID_RELEVANCE:
            err(f"{label}: invalid vc_relevance '{item['vc_relevance']}'")
        # The tier answers "how good"; vc_relevance answers "was it built for this".
        # Keep them separate — an earlier version merged them and ended up ranking
        # generic software as though it were venture tooling.
        if (item.get("vc_relevance") or "").lower() == "infrastructure" and item.get("tier") == "infrastructure":
            err(f"{label}: 'infrastructure' used as both tier and relevance")
        if not item.get("good_for"):
            warn(f"{label}: no 'good_for' entries")
        if not item.get("limitations"):
            warn(f"{label}: no 'limitations' — every tool has caveats")
        use = str(item.get("vc_use_case", ""))
        if use and len(use) < 40:
            warn(f"{label}: vc_use_case is thin ({len(use)} chars)")
        if use and not use.rstrip().endswith((".", "!", "?", ")", "`")):
            warn(f"{label}: vc_use_case does not end in a full stop")
        # attribution: the GitHub URL must point at the owner/repo
        if name and name not in str(item.get("name", "")):
            err(f"{label}: attribution mismatch")
        # A curated name absent from the snapshot is a real inconsistency, not a nit:
        # either the entry was added without refreshing metadata, or the repository was
        # renamed or deleted upstream. Either way the published record would be built
        # from a fallback rather than verified data, so this blocks the build.
        if name and snapshot and name not in snapshot.get("repos", {}):
            err(f"{label}: not present in metadata/snapshot.json — run "
                f"`python scripts/update.py --repos-only {name}`, or the repository was "
                f"renamed or deleted upstream and the entry needs attention")


def check_duplicates(curation: dict) -> None:
    names = [i.get("name", "").lower() for i in (curation.get("repos") or [])]
    dupes = [n for n, c in Counter(names).items() if c > 1]
    for d in dupes:
        err(f"duplicate repository in curation.yaml: {d}")
    # near-duplicates by repo slug (owner differs)
    slugs = Counter(n.split("/")[-1] for n in names if "/" in n)
    for slug, c in slugs.items():
        if c > 1:
            warn(f"same repo slug under multiple owners (possible duplicate implementation): {slug}")


def check_licenses(published: list[dict]) -> None:
    for r in published:
        lic = r.get("license") or ""
        if not lic or lic == "unknown" or lic.startswith("unverified"):
            warn(f"{r['name']}: licence unverified — flagged in metadata, must not be redistributed")


def check_archived(published: list[dict], curation: dict) -> None:
    # An archived repository is normally an error: the directory should not present a
    # dead project as usable. The exception is a deliberately kept entry where the
    # artefact outlives the repository — a live dataset whose sample code was archived,
    # for instance. Those set `archived_ok` and are downgraded to a warning so the fact
    # stays visible in the review queue instead of vanishing.
    allowed = {i.get("name") for i in (curation.get("repos") or []) if i.get("archived_ok")}
    for r in published:
        if r.get("archived") is True:
            if r.get("name") in allowed:
                warn(f"{r['name']}: archived upstream, kept deliberately "
                     f"(dataset still live) — see the entry")
            else:
                err(f"{r['name']}: archived upstream but still listed as a curated entry")
        elif str(r.get("status", "")).startswith("Dormant"):
            warn(f"{r['name']}: dormant — candidate for removal or re-labelling")


def check_category_pages(curation: dict) -> None:
    cats = {i.get("category") for i in (curation.get("repos") or [])}
    for cat in sorted(c for c in cats if c):
        page = CATEGORIES_DIR / f"{cat}.md"
        if not page.exists():
            err(f"no category page for '{cat}' (expected categories/{cat}.md)")
        elif page.stat().st_size < 400:
            warn(f"categories/{cat}.md looks empty")
    for page in CATEGORIES_DIR.glob("*.md"):
        if page.stem not in cats:
            warn(f"categories/{page.stem}.md exists but no curated repo uses it")


def check_generated_freshness() -> None:
    """Generated artefacts must be newer than their inputs, or they are stale."""
    if not REPOS_JSON.exists() or not CURATION.exists():
        return
    if CURATION.stat().st_mtime > REPOS_JSON.stat().st_mtime + 1:
        err("curation.yaml is newer than metadata/repositories.json — run "
            "`python scripts/generate_index.py` and commit the result")
    if SNAPSHOT.exists() and SNAPSHOT.stat().st_mtime > REPOS_JSON.stat().st_mtime + 1:
        err("metadata/snapshot.json is newer than metadata/repositories.json — regenerate")


def check_attribution(published: list[dict]) -> None:
    for r in published:
        gh = r.get("github") or ""
        name = r.get("name") or ""
        if not gh.startswith("https://github.com/"):
            err(f"{name}: github link is not a github.com URL ({gh!r})")
        elif name and gh.split("github.com/")[-1].strip("/").lower() != name.lower():
            err(f"{name}: github link ({gh}) does not match recorded name ({name})")
        if not r.get("description"):
            warn(f"{name}: no description/tagline")


def check_snapshot_age() -> None:
    if not SNAPSHOT.exists():
        return
    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    ts = snapshot.get("generated_at")
    if not ts:
        warn("snapshot has no generated_at")
        return
    dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
    age = (datetime.now(timezone.utc) - dt).days
    if age > 21:
        warn(f"metadata snapshot is {age} days old — weekly workflow may be failing")


# ---------------------------------------------------------------------------
# Live checks
# ---------------------------------------------------------------------------

def check_live(published: list[dict], tok: str) -> None:
    print(f"live check: {len(published)} repositories")
    for i, r in enumerate(published, 1):
        name = r["name"]
        req = urllib.request.Request(
            f"https://api.github.com/repos/{name}",
            headers={"Authorization": f"Bearer {tok}",
                     "Accept": "application/vnd.github+json",
                     "User-Agent": "open-source-vc-verify"},
        )
        try:
            with urllib.request.urlopen(req, timeout=25) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code in (404, 410):
                err(f"{name}: DEAD LINK — repository not reachable ({exc.code})")
            elif exc.code in (403, 429):
                warn(f"{name}: rate limited, live check incomplete")
                time.sleep(20)
            else:
                warn(f"{name}: live check HTTP {exc.code}")
            continue
        except Exception as exc:
            warn(f"{name}: live check failed ({type(exc).__name__})")
            continue

        if data.get("archived"):
            err(f"{name}: archived upstream (should not be listed as active)")
        live_lic = ((data.get("license") or {}).get("spdx_id")) or "unknown"
        rec_lic = (r.get("license") or "unknown")
        if live_lic != "NOASSERTION" and rec_lic not in ("unknown",) and live_lic != rec_lic:
            err(f"{name}: licence drift — recorded {rec_lic}, live {live_lic}")
        if data.get("size", 0) == 0:
            warn(f"{name}: repository is empty")
        if i % 25 == 0:
            print(f"  ...{i}/{len(published)}")
        time.sleep(0.3)


# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true", help="skip network checks")
    ap.add_argument("--json", help="write a JSON report to this path")
    args = ap.parse_args()

    print("== structural ==")
    check_files()
    check_markers()
    check_json_malformed()
    check_yaml_malformed()

    if not CURATION.exists() or not SNAPSHOT.exists():
        report(args)
        return

    curation, snapshot, published = load_inputs()
    check_items(curation, snapshot)
    check_duplicates(curation)
    check_licenses(published)
    check_archived(published, curation)
    check_category_pages(curation)
    check_generated_freshness()
    check_attribution(published)
    check_snapshot_age()

    if not args.offline:
        tok = token()
        if not tok:
            warn("no GitHub token; live checks skipped")
        else:
            print("== live ==")
            check_live(published, tok)

    report(args)


def report(args) -> None:
    print()
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    if args.json:
        Path(args.json).write_text(json.dumps(
            {"errors": errors, "warnings": warnings,
             "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds")},
            indent=2), encoding="utf-8")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
