#!/usr/bin/env python3
"""
Refresh verified metadata for curated repositories and report what changed.

This is the engine behind the weekly update workflow.

Contract (deliberate, and the reason this repo stays trustworthy):

  * It reads  metadata/snapshot.json  -> the last verified state
  * It reads  curation.yaml           -> the curated list (read-only here)
  * It fetches live state from the GitHub API
  * It writes metadata/snapshot.json  -> refreshed state
  * It writes research/review-queue-YYYY-MM-DD.md -> findings for a human

  * It NEVER edits curation.yaml, never adds a repository to the directory,
    and never removes one. Discovery is automated; curation is human.

Changes it detects:
  archived / unarchived      license changed      significant star growth
  repository gone (404/410)  major new release    stalls (no push for N months)
  pushed_at freshness        fork count movement

Usage:
    python scripts/update.py                    # refresh + report
    python scripts/update.py --stars-threshold 0.25
    python scripts/update.py --repos-only a/b,c/d
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "metadata" / "snapshot.json"
CURATION = ROOT / "curation.yaml"
QUEUE_DIR = ROOT / "research"

API = "https://api.github.com"

# Fields we record verbatim from the API. If it is not here, we do not claim it.
KEEP = (
    "full_name", "html_url", "description", "stargazers_count", "forks_count",
    "subscribers_count", "open_issues_count", "language", "archived", "disabled",
    "created_at", "updated_at", "pushed_at", "homepage", "size", "default_branch",
    "topics", "fork",
)


def token() -> str:
    for env in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(env):
            return os.environ[env]
    try:
        return subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True, check=True
        ).stdout.strip()
    except Exception as exc:
        sys.exit(f"No GitHub token available ({exc}). Set GITHUB_TOKEN or run `gh auth login`.")


def api_get(path: str, tok: str) -> tuple[dict | None, str | None]:
    """GET a GitHub API path. Returns (payload, error). 404/410 are answers, not failures."""
    req = urllib.request.Request(
        f"{API}{path}",
        headers={
            "Authorization": f"Bearer {tok}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "open-source-vc-updater",
        },
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8")), None
        except urllib.error.HTTPError as exc:
            if exc.code in (404, 410):
                return None, f"gone:{exc.code}"
            if exc.code in (403, 429):
                time.sleep(15 * (attempt + 1))
                continue
            return None, f"HTTP {exc.code}"
        except Exception as exc:
            if attempt == 3:
                return None, f"{type(exc).__name__}"
            time.sleep(3)
    return None, "exhausted"


def fetch_repo(full_name: str, tok: str) -> dict | None:
    data, err = api_get(f"/repos/{full_name}", tok)
    if not data:
        return None
    rec = {k: data.get(k) for k in KEEP}
    lic = data.get("license") or {}
    rec["license_spdx"] = lic.get("spdx_id")
    rec["license_name"] = lic.get("name")
    rec["owner_type"] = (data.get("owner") or {}).get("type")
    return rec


def fetch_releases(full_name: str, tok: str, limit: int = 5) -> list[dict]:
    data, err = api_get(f"/repos/{full_name}/releases?per_page={limit}", tok)
    if not isinstance(data, list):
        return []
    return [
        {
            "tag": r.get("tag_name"),
            "name": r.get("name"),
            "published_at": r.get("published_at"),
            "prerelease": r.get("prerelease"),
        }
        for r in data
    ]


def load_curation_names() -> list[str]:
    """Minimal YAML read so this script has no third-party dependency."""
    if not CURATION.exists():
        return []
    names, in_repos = [], False
    for raw in CURATION.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line.startswith("repos:"):
            in_repos = True
            continue
        if in_repos:
            if line and not line[0].isspace():
                break
            stripped = line.strip()
            if stripped.startswith("- name:"):
                names.append(stripped.split(":", 1)[1].strip().strip("'\""))
    return [n for n in names if n]


def months_since(iso: str | None) -> float | None:
    if not iso:
        return None
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except ValueError:
        return None
    return (datetime.now(timezone.utc) - dt).days / 30.44


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stars-threshold", type=float, default=0.20,
                    help="relative star change that counts as notable (default 0.20 = 20%%)")
    ap.add_argument("--stale-months", type=float, default=12.0,
                    help="no-push window that triggers a stall flag")
    ap.add_argument("--repos-only", help="comma-separated subset to refresh")
    ap.add_argument("--with-releases", action="store_true",
                    help="also fetch latest releases (extra API calls, off by default)")
    args = ap.parse_args()

    tok = token()
    if args.repos_only:
        names = [n.strip() for n in args.repos_only.split(",") if n.strip()]
    else:
        names = load_curation_names()
    if not names:
        sys.exit("No repositories to refresh (curation.yaml empty or missing).")

    prev = json.loads(SNAPSHOT.read_text(encoding="utf-8")) if SNAPSHOT.exists() else {}
    prev_repos = prev.get("repos", {})

    now = datetime.now(timezone.utc)
    current: dict[str, dict] = {}
    findings: dict[str, list[str]] = {
        "gone": [], "archived": [], "unarchived": [],
        "license_changed": [], "star_growth": [], "stalled": [], "new_release": [],
    }
    errors: list[dict] = []

    for i, name in enumerate(names, 1):
        rec = fetch_repo(name, tok)
        if rec is None:
            findings["gone"].append(name)
            errors.append({"repo": name, "error": "unavailable"})
            print(f"[{i}/{len(names)}] {name}: GONE", flush=True)
            continue
        current[name] = rec
        old = prev_repos.get(name)

        if rec.get("archived"):
            findings["archived"].append(name)
        elif old and old.get("archived"):
            findings["unarchived"].append(name)

        if old:
            if (old.get("license_spdx") or "?") != (rec.get("license_spdx") or "?"):
                findings["license_changed"].append(
                    f"{name}: {old.get('license_spdx') or 'none'} -> {rec.get('license_spdx') or 'none'}"
                )
            o, n = old.get("stargazers_count") or 0, rec.get("stargazers_count") or 0
            if o > 0 and abs(n - o) / o >= args.stars_threshold:
                findings["star_growth"].append(f"{name}: {o:,} -> {n:,} ({n - o:+,})")

        m = months_since(rec.get("pushed_at"))
        if m is not None and m >= args.stale_months and not rec.get("archived"):
            findings["stalled"].append(f"{name}: no push in {m:.0f} months")

        if args.with_releases:
            rels = fetch_releases(name, tok)
            if rels:
                current[name]["latest_releases"] = rels
                latest = rels[0].get("published_at")
                old_latest = ((old or {}).get("latest_releases") or [{}])[0].get("published_at")
                if latest and latest != old_latest:
                    findings["new_release"].append(f"{name}: {rels[0].get('tag')} ({latest[:10]})")

        print(f"[{i}/{len(names)}] {name} ok ({rec.get('stargazers_count'):,}★)", flush=True)
        time.sleep(0.35)

    snapshot = {
        "generated_at": now.isoformat(timespec="seconds"),
        "repo_count": len(current),
        "repos": current,
    }
    SNAPSHOT.parent.mkdir(parents=True, exist_ok=True)
    SNAPSHOT.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False, sort_keys=True),
                        encoding="utf-8")

    total = sum(len(v) for v in findings.values())
    if total:
        QUEUE_DIR.mkdir(parents=True, exist_ok=True)
        out = QUEUE_DIR / f"review-queue-{now.date().isoformat()}.md"
        lines = [
            f"# Weekly review queue — {now.date().isoformat()}",
            "",
            f"Generated by `scripts/update.py` against {len(names)} curated repositories.",
            f"{total} item(s) need a human decision. Nothing has been changed in `curation.yaml`.",
            "",
            "Curation is manual by design. Work each item, then edit `curation.yaml` and",
            "regenerate with `python scripts/generate_index.py`.",
            "",
        ]
        headings = {
            "gone": "Repository unreachable (deleted, renamed, or private)",
            "archived": "Archived upstream — consider removing or re-labelling",
            "unarchived": "No longer archived",
            "license_changed": "License changed — re-check redistribution status",
            "star_growth": "Notable star movement",
            "stalled": f"No push in over {args.stale_months:.0f} months",
            "new_release": "New release",
        }
        for key, title in headings.items():
            if findings[key]:
                lines += [f"## {title}", ""]
                lines += [f"- {item}" for item in sorted(findings[key])]
                lines.append("")
        out.write_text("\n".join(lines), encoding="utf-8")
        print(f"\nReview queue -> {out}")
    else:
        print("\nNo changes detected.")

    for key, items in findings.items():
        if items:
            print(f"  {key}: {len(items)}")
    print(f"Snapshot: {len(current)} repos -> {SNAPSHOT}")


if __name__ == "__main__":
    main()
