#!/usr/bin/env python3
"""
Turn the raw candidate pool into a readable shortlist.

research/candidates.json is deliberately large and unfiltered — it is the raw
output of broad search. This script applies mechanical quality filters and
prints a compact, grouped shortlist for human curation.

This script does NOT decide what belongs in the directory. It removes things
that cannot possibly qualify (archived, no description, obvious spam) and
presents the rest so a human can judge them. Curation is manual by design.

Usage:
    python scripts/shortlist.py                     # grouped shortlist
    python scripts/shortlist.py --group legal       # one group
    python scripts/shortlist.py --min-stars 500
    python scripts/shortlist.py --csv research/shortlist.csv
    python scripts/shortlist.py --stats
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "research" / "candidates.json"

# Descriptions that reliably indicate a project which cannot qualify, regardless
# of stars. Kept narrow on purpose: this is a spam filter, not a taste filter.
SPAM_PATTERNS = [
    r"\bawesome list\b", r"\bawesome-list\b", r"^a list of\b", r"^list of\b",
    r"\bcheat ?sheet\b", r"\broadmap\b", r"\binterview questions?\b",
    r"\bmy (?:portfolio|resume|cv)\b", r"\b100 days of\b", r"\btutorial series\b",
    r"\bprompt(s)? (?:collection|library|list)\b", r"\bcurso\b", r"\bnotes?\b$",
    r"\bawesome\b", r"\bexamples? (?:for|of) learning\b", r"\bpractice\b",
    r"\blearn(?:ing)? (?:python|javascript|rust|go|java)\b",
    r"\bcoding challenges?\b", r"\bdotfiles\b", r"\bconfig(?:uration)? files\b",
]

# Names that are almost never a curated recommendation.
SPAM_NAMES = re.compile(r"(awesome|cheatsheet|cheat-sheet|interview|dotfiles|"
                        r"tutorial|course|exercises|playground|sandbox|"
                        r"boilerplate|template)$", re.I)

GROUPS = [
    "vc-native", "sourcing", "market-research", "web-intel", "documents",
    "finance", "legal", "relationships", "knowledge", "agents", "automation",
    "datasets", "standards",
]


def months_since(iso: str | None) -> float | None:
    if not iso:
        return None
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except ValueError:
        return None
    return (datetime.now(timezone.utc) - dt).days / 30.44


def primary_group(rec: dict) -> str:
    """The first query group that surfaced this repo, in taxonomy order."""
    tags = rec.get("discovered_via") or []
    for g in GROUPS:
        if any(t.startswith(g + ":") for t in tags):
            return g
    return "other"


def spammy(rec: dict) -> bool:
    desc = (rec.get("description") or "").lower()
    if not desc:
        return True
    if SPAM_NAMES.search(rec["name"].split("/")[-1]):
        return True
    return any(re.search(p, desc, re.I) for p in SPAM_PATTERNS)


def load() -> list[dict]:
    if not CANDIDATES.exists():
        raise SystemExit(f"{CANDIDATES} not found. Run `python scripts/discover.py` first.")
    return json.loads(CANDIDATES.read_text(encoding="utf-8"))["candidates"]


def filter_pool(recs: list[dict], min_stars: int, max_age_months: float) -> tuple[list[dict], Counter]:
    kept, reasons = [], Counter()
    for rec in recs:
        if rec.get("archived"):
            reasons["archived"] += 1
            continue
        if spammy(rec):
            reasons["no description / looks like a list, tutorial, or template"] += 1
            continue
        if (rec.get("stars") or 0) < min_stars:
            reasons["below star floor"] += 1
            continue
        age = months_since(rec.get("pushed_at"))
        if age is not None and age > max_age_months:
            reasons["stale"] += 1
            continue
        kept.append(rec)
    return kept, reasons


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--group", help="only this group")
    ap.add_argument("--min-stars", type=int, default=150)
    ap.add_argument("--max-age-months", type=float, default=30.0)
    ap.add_argument("--limit", type=int, default=0, help="cap rows per group (0 = no cap)")
    ap.add_argument("--csv", help="write the shortlist to CSV")
    ap.add_argument("--stats", action="store_true", help="print filter statistics only")
    args = ap.parse_args()

    raw = load()
    kept, reasons = filter_pool(raw, args.min_stars, args.max_age_months)

    if args.stats:
        print(f"raw candidates      {len(raw)}")
        print(f"after filtering     {len(kept)}")
        print()
        print("rejected:")
        for reason, n in reasons.most_common():
            print(f"  {n:5d}  {reason}")
        print()
        print("by group (kept):")
        for g, n in Counter(primary_group(r) for r in kept).most_common():
            print(f"  {n:5d}  {g}")
        print()
        print("licence availability:")
        lic = Counter((r.get("license_spdx") or "none") for r in kept)
        for k, n in lic.most_common(12):
            print(f"  {n:5d}  {k}")
        return

    if args.csv:
        out = Path(args.csv)
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["group", "name", "stars", "forks", "language", "license",
                        "created", "pushed", "url", "description"])
            for r in sorted(kept, key=lambda r: (primary_group(r), -(r["stars"] or 0))):
                w.writerow([primary_group(r), r["name"], r["stars"], r["forks"],
                            r.get("language") or "", r.get("license_spdx") or "none",
                            (r.get("created_at") or "")[:10], (r.get("pushed_at") or "")[:10],
                            r["url"], r["description"]])
        print(f"Wrote {len(kept)} rows -> {out}")
        return

    groups = [args.group] if args.group else GROUPS + ["other"]
    for g in groups:
        rows = [r for r in kept if primary_group(r) == g]
        if not rows:
            continue
        rows.sort(key=lambda r: -(r["stars"] or 0))
        if args.limit:
            rows = rows[: args.limit]
        print(f"\n=== {g} ({len(rows)}) ===")
        for r in rows:
            stars = f"{r['stars']:>7,}"
            lang = (r.get("language") or "-")[:12].ljust(12)
            lic = (r.get("license_spdx") or "none")[:14].ljust(14)
            pushed = (r.get("pushed_at") or "----------")[:10]
            desc = (r["description"] or "")[:96]
            print(f"{stars} {lang} {lic} {pushed} {r['name']:<42} {desc}")


if __name__ == "__main__":
    main()
