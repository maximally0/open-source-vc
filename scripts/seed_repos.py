#!/usr/bin/env python3
"""
Fetch verified metadata for a targeted seed list and merge it into the pool.

Broad GitHub search (scripts/discover.py) covers generic infrastructure well but
finds VC-native tooling badly — that tooling is rare and mostly does not use
searchable "VC" vocabulary. This script is the other half of discovery: it
resolves specific known/lead projects straight from the GitHub API.

Every entry is fetched, never assumed. Repositories that do not resolve are
reported and dropped — that report is the point, because a seed list written
from memory contains mistakes and this is how they get caught.

Usage:
    python scripts/seed_repos.py                      # research/seeds.txt
    python scripts/seed_repos.py --file other.txt
    python scripts/seed_repos.py --check              # report only, do not merge
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
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "research" / "candidates.json"
DEFAULT_SEEDS = ROOT / "research" / "seeds.txt"


def token() -> str:
    for env in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(env):
            return os.environ[env]
    try:
        return subprocess.run(["gh", "auth", "token"], capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception as exc:
        sys.exit(f"No GitHub token ({exc}). Set GITHUB_TOKEN or run `gh auth login`.")


def fetch(full_name: str, tok: str) -> tuple[dict | None, str | None]:
    req = urllib.request.Request(
        f"https://api.github.com/repos/{full_name}",
        headers={"Authorization": f"Bearer {tok}",
                 "Accept": "application/vnd.github+json",
                 "User-Agent": "open-source-vc-seed"},
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=25) as resp:
                return json.loads(resp.read().decode("utf-8")), None
        except urllib.error.HTTPError as exc:
            if exc.code in (404, 410):
                return None, f"not found ({exc.code})"
            if exc.code in (403, 429):
                time.sleep(12 * (attempt + 1))
                continue
            return None, f"HTTP {exc.code}"
        except Exception as exc:
            if attempt == 2:
                return None, type(exc).__name__
            time.sleep(3)
    return None, "exhausted"


def compact(item: dict) -> dict:
    lic = item.get("license") or {}
    return {
        "name": item["full_name"],
        "url": item["html_url"],
        "description": (item.get("description") or "").strip(),
        "stars": item.get("stargazers_count", 0),
        "forks": item.get("forks_count", 0),
        "open_issues": item.get("open_issues_count", 0),
        "language": item.get("language"),
        "license_spdx": lic.get("spdx_id"),
        "license_name": lic.get("name"),
        "archived": bool(item.get("archived")),
        "is_fork": bool(item.get("fork")),
        "created_at": item.get("created_at"),
        "pushed_at": item.get("pushed_at"),
        "topics": item.get("topics", []),
        "homepage": item.get("homepage") or "",
        "owner_type": (item.get("owner") or {}).get("type"),
        "owner": (item.get("owner") or {}).get("login"),
    }


def parse_seeds(path: Path) -> list[tuple[str, str]]:
    out = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        name, _, why = line.partition("#")
        name = name.strip()
        if "/" not in name:
            continue
        if name.endswith("?"):
            print(f"  (skipping placeholder: {name})")
            continue
        out.append((name, why.strip()))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default=str(DEFAULT_SEEDS))
    ap.add_argument("--check", action="store_true", help="report only; do not merge")
    args = ap.parse_args()

    seeds = parse_seeds(Path(args.file))
    tok = token()
    print(f"Resolving {len(seeds)} seed repositories...\n")

    resolved: dict[str, dict] = {}
    failed: list[tuple[str, str]] = []

    for i, (name, why) in enumerate(seeds, 1):
        data, err = fetch(name, tok)
        if data is None:
            failed.append((name, err or "unknown"))
            print(f"[{i}/{len(seeds)}] FAIL  {name:<48} {err}")
            continue
        rec = compact(data)
        rec["discovered_via"] = [f"seed:{why}" if why else "seed:targeted"]
        resolved[rec["name"].lower()] = rec
        flag = "ARCHIVED " if rec["archived"] else ""
        print(f"[{i}/{len(seeds)}] ok    {rec['name']:<48} {rec['stars']:>7,}★ "
              f"{rec.get('license_spdx') or 'no licence':<14} {flag}{(rec['description'] or '')[:40]}")
        time.sleep(0.25)

    print(f"\nresolved {len(resolved)} / {len(seeds)}")
    if failed:
        print(f"\nDID NOT RESOLVE ({len(failed)}) — these were wrong in the seed list:")
        for name, err in failed:
            print(f"  {name:<48} {err}")

    if args.check:
        print("\ncheck only; pool not modified")
        return

    doc = json.loads(CANDIDATES.read_text(encoding="utf-8")) if CANDIDATES.exists() else {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "candidates": [],
    }
    pool = {c["name"].lower(): c for c in doc["candidates"]}
    added = 0
    for key, rec in resolved.items():
        if key in pool:
            # keep the richer existing provenance
            pool[key].setdefault("discovered_via", [])
            merged = sorted(set(pool[key]["discovered_via"]) | set(rec["discovered_via"]))
            pool[key]["discovered_via"] = merged
            pool[key].update({k: v for k, v in rec.items() if k != "discovered_via"})
        else:
            pool[key] = rec
            added += 1

    doc["candidates"] = sorted(pool.values(), key=lambda r: -r["stars"])
    doc["candidate_count"] = len(pool)
    doc["seeds_merged_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    CANDIDATES.write_text(json.dumps(doc, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nmerged {added} new seed repos; pool now {len(pool)} -> {CANDIDATES}")


if __name__ == "__main__":
    main()
