#!/usr/bin/env python3
"""
Discovery pass for the Open Source VC directory.

Queries the GitHub Search API across a broad set of VC-workflow and adjacent
infrastructure terms, then writes a de-duplicated candidate pool.

Design notes:
  * This script only DISCOVERS and records verified metadata. It never decides
    what belongs in the curated list. Curation lives in curation.yaml and is
    human-controlled by design (see CONTRIBUTING.md).
  * Every field written here comes from the GitHub API response. Nothing is
    inferred, estimated, or guessed.

Usage:
    python scripts/discover.py                 # run the full query set
    python scripts/discover.py --queries a,b   # run a subset
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
OUT = ROOT / "research" / "candidates.json"

API = "https://api.github.com/search/repositories"

# ---------------------------------------------------------------------------
# Query set.
#
# Grouped so that gaps are visible. `sort` is either "stars" (mature, adopted
# projects) or "updated" (recently active, which is how emerging 2025-2026
# projects surface without being drowned out by decade-old 20k-star repos).
# `qualifier` is appended verbatim so we can scope results per group.
# ---------------------------------------------------------------------------

QUERIES: list[tuple[str, str, str, str]] = [
    # (group, q, sort, why)

    # --- VC-native -----------------------------------------------------------
    ("vc-native", "venture capital", "stars", "Explicit VC tooling"),
    ("vc-native", "topic:venture-capital", "stars", "GitHub topic"),
    ("vc-native", "topic:vc", "stars", "GitHub topic"),
    ("vc-native", "topic:startups", "stars", "Adjacent to VC"),
    ("vc-native", "cap table", "stars", "Cap table tooling"),
    ("vc-native", "topic:cap-table", "stars", "Cap table tools"),
    ("vc-native", "equity management", "stars", "Equity / ESOP"),
    ("vc-native", "deal flow", "stars", "Sourcing pipeline"),
    ("vc-native", "investment memo", "stars", "Memo generation"),
    ("vc-native", "startup due diligence", "stars", "Diligence tooling"),
    ("vc-native", "fund management venture", "stars", "Fund ops"),
    ("vc-native", "investor database", "stars", "Investor data"),
    ("vc-native", "startup database", "stars", "Company data"),
    ("vc-native", "vc fund reporting", "stars", "LP reporting"),
    ("vc-native", "topic:fundraising", "stars", "Fundraise infra"),
    ("vc-native", "accelerator open source", "stars", "Program tooling"),

    # --- Sourcing / founder & talent discovery -------------------------------
    ("sourcing", "topic:osint", "stars", "People + company recon"),
    ("sourcing", "people search engine", "stars", "Talent discovery"),
    ("sourcing", "developer search engine", "stars", "GitHub intelligence"),
    ("sourcing", "github analytics developers", "stars", "Dev discovery"),
    ("sourcing", "talent graph", "stars", "Talent mapping"),
    ("sourcing", "entity resolution", "stars", "Identity resolution"),
    ("sourcing", "company enrichment", "stars", "Company data enrichment"),
    ("sourcing", "linkedin scraper", "stars", "People sourcing"),
    ("sourcing", "founder discovery", "updated", "Emerging founder tools"),
    ("sourcing", "startup discovery", "updated", "Emerging startup tools"),
    ("sourcing", "email finder verification", "stars", "Contact data"),

    # --- Market & competitive research ---------------------------------------
    ("market-research", "competitive intelligence", "stars", "Market mapping"),
    ("market-research", "market intelligence", "stars", "Industry research"),
    ("market-research", "deep research agent", "stars", "Automated research"),
    ("market-research", "topic:market-research", "stars", "Research tooling"),
    ("market-research", "trend detection", "stars", "Trend signals"),
    ("market-research", "news monitoring", "stars", "Signal monitoring"),
    ("market-research", "web research agent", "updated", "Emerging research"),
    ("market-research", "topic:competitive-intelligence", "stars", "Comp intel"),

    # --- Web intelligence / crawling / OSINT ---------------------------------
    ("web-intel", "web crawler", "stars", "Crawl sources at scale"),
    ("web-intel", "web scraping framework", "stars", "Structured extraction"),
    ("web-intel", "browser automation", "stars", "Headless browsing"),
    ("web-intel", "headless browser", "stars", "JS-rendered pages"),
    ("web-intel", "change detection website", "stars", "Monitor competitors"),
    ("web-intel", "screenshot api", "stars", "Visual capture"),
    ("web-intel", "domain intelligence", "stars", "Domain recon"),
    ("web-intel", "topic:osint", "updated", "Emerging OSINT"),
    ("web-intel", "archive web pages", "stars", "Archival evidence"),
    ("web-intel", "topic:web-scraping", "stars", "Scraping ecosystem"),

    # --- Document intelligence / data rooms ---------------------------------
    ("documents", "pdf parsing", "stars", "Data-room documents"),
    ("documents", "document extraction layout", "stars", "Structured extraction"),
    ("documents", "ocr engine", "stars", "Scanned documents"),
    ("documents", "document rag", "stars", "Document Q&A"),
    ("documents", "table extraction", "stars", "Financial tables"),
    ("documents", "contract analysis nlp", "stars", "Legal DD"),
    ("documents", "topic:document-ai", "stars", "Document AI"),
    ("documents", "topic:ocr", "stars", "OCR ecosystem"),
    ("documents", "multimodal document understanding", "updated", "Emerging doc AI"),

    # --- Financial analysis / modeling ---------------------------------------
    ("finance", "financial modeling", "stars", "Deal models"),
    ("finance", "valuation", "stars", "Valuation"),
    ("finance", "dcf discounted cash flow", "stars", "DCF"),
    ("finance", "monte carlo simulation", "stars", "Scenario analysis"),
    ("finance", "portfolio analytics", "stars", "Portfolio maths"),
    ("finance", "stock market analysis", "stars", "Public comparables"),
    ("finance", "financial data api", "stars", "Market data"),
    ("finance", "topic:quantitative-finance", "stars", "Quant ecosystem"),
    ("finance", "sec filings", "stars", "Public filings"),
    ("finance", "topic:financial-analysis", "stars", "Fin analysis"),

    # --- Legal ---------------------------------------------------------------
    ("legal", "legal nlp", "stars", "Legal DD"),
    ("legal", "contract review llm", "updated", "Emerging contract AI"),
    ("legal", "clause extraction", "stars", "Clause analysis"),
    ("legal", "topic:legal-tech", "stars", "Legal tech ecosystem"),
    ("legal", "legal document dataset", "stars", "Legal corpora"),
    ("legal", "know your customer compliance", "stars", "KYC / compliance"),

    # --- Relationship intelligence / CRM ------------------------------------
    ("relationships", "personal crm", "stars", "Relationship memory"),
    ("relationships", "crm self hosted", "stars", "Open CRM"),
    ("relationships", "email analytics", "stars", "Inbox intelligence"),
    ("relationships", "calendar scheduling open source", "stars", "Meeting infra"),
    ("relationships", "network analysis graph", "stars", "Network graph"),
    ("relationships", "topic:crm", "stars", "CRM ecosystem"),
    ("relationships", "contact management", "stars", "Contact graph"),

    # --- Knowledge management / retrieval -----------------------------------
    ("knowledge", "knowledge graph", "stars", "Knowledge graphs"),
    ("knowledge", "retrieval augmented generation", "stars", "RAG"),
    ("knowledge", "vector database", "stars", "Vector search"),
    ("knowledge", "graphrag", "stars", "Graph RAG"),
    ("knowledge", "semantic search", "stars", "Semantic retrieval"),
    ("knowledge", "topic:knowledge-management", "stars", "KM ecosystem"),
    ("knowledge", "graph database", "stars", "Graph storage"),
    ("knowledge", "personal knowledge base", "stars", "Institutional memory"),

    # --- AI agents / orchestration ------------------------------------------
    ("agents", "ai agent framework", "stars", "Agent frameworks"),
    ("agents", "llm agent orchestration", "stars", "Orchestration"),
    ("agents", "multi-agent framework", "stars", "Multi-agent"),
    ("agents", "browser agent", "stars", "Browser agents"),
    ("agents", "topic:mcp", "stars", "MCP servers"),
    ("agents", "model context protocol server", "stars", "MCP servers"),
    ("agents", "research agent", "updated", "Emerging research agents"),
    ("agents", "autonomous agent", "stars", "Autonomy"),
    ("agents", "document agent", "updated", "Document agents"),
    ("agents", "topic:llm-agents", "stars", "Agent ecosystem"),
    ("agents", "rag agent memory", "updated", "Agent memory"),

    # --- Workflow / automation / data plumbing -------------------------------
    ("automation", "workflow automation", "stars", "Automation"),
    ("automation", "etl pipeline", "stars", "Data pipelines"),
    ("automation", "topic:workflow-automation", "stars", "Automation ecosystem"),
    ("automation", "topic:etl", "stars", "ETL ecosystem"),
    ("automation", "scheduled jobs scheduler", "stars", "Scheduling"),
    ("automation", "slack bot automation", "stars", "Deal-flow alerts"),
    ("automation", "topic:data-pipeline", "stars", "Pipelines"),

    # --- Datasets ------------------------------------------------------------
    ("datasets", "startup funding dataset", "stars", "Funding data"),
    ("datasets", "github dataset", "stars", "Developer data"),
    ("datasets", "company dataset", "stars", "Company data"),
    ("datasets", "financial dataset", "stars", "Financial data"),
    ("datasets", "legal dataset", "stars", "Legal data"),
    ("datasets", "patent dataset", "stars", "IP / patent data"),
    ("datasets", "topic:datasets", "stars", "Open datasets"),

    # --- Standards -----------------------------------------------------------
    ("standards", "open financial data standard", "stars", "Data standards"),
    ("standards", "xbrl", "stars", "Financial reporting std"),
    ("standards", "openapi specification tooling", "stars", "API standards"),
]


def token() -> str:
    """Prefer an explicit env var, fall back to the gh CLI keyring."""
    for env in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(env):
            return os.environ[env]
    try:
        return subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True, check=True
        ).stdout.strip()
    except Exception as exc:  # pragma: no cover - environment dependent
        sys.exit(f"No GitHub token available ({exc}). Set GITHUB_TOKEN or run `gh auth login`.")


def search(q: str, sort: str, tok: str, per_page: int = 100) -> tuple[list[dict], int | None]:
    params = {"q": q, "sort": sort, "order": "desc", "per_page": str(per_page)}
    url = f"{API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {tok}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "open-source-vc-discovery",
        },
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
                return payload.get("items", []), None
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", "replace")[:200]
            if exc.code in (403, 429):
                wait = 20 * (attempt + 1)
                print(f"    rate limited ({exc.code}); sleeping {wait}s", flush=True)
                time.sleep(wait)
                continue
            if exc.code == 422:
                return [], f"422 unprocessable: {body}"
            return [], f"HTTP {exc.code}: {body}"
        except Exception as exc:
            time.sleep(5)
            if attempt == 3:
                return [], f"{type(exc).__name__}: {exc}"
    return [], "rate limited after retries"


def compact(item: dict) -> dict:
    """Keep only fields we can verify and cite. No inference."""
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


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--queries", help="comma-separated group names to run")
    ap.add_argument("--sleep", type=float, default=2.2, help="seconds between search calls")
    args = ap.parse_args()

    queries = QUERIES
    if args.queries:
        want = {g.strip() for g in args.queries.split(",")}
        queries = [q for q in QUERIES if q[0] in want]

    tok = token()
    pool: dict[str, dict] = {}
    provenance: dict[str, list[str]] = {}
    errors: list[dict] = []

    for i, (group, q, sort, why) in enumerate(queries, 1):
        print(f"[{i}/{len(queries)}] {group:15s} {q!r} (sort={sort})", flush=True)
        items, err = search(q, sort, tok)
        if err:
            errors.append({"group": group, "q": q, "error": err})
            print(f"    ! {err}", flush=True)
        added = 0
        for item in items:
            if item.get("fork"):
                continue  # forks are duplicates by definition
            rec = compact(item)
            key = rec["name"].lower()
            if key not in pool:
                pool[key] = rec
                provenance[key] = []
                added += 1
            provenance[key].append(f"{group}:{q}")
        print(f"    +{added} new (pool={len(pool)})", flush=True)
        if i < len(queries):
            time.sleep(args.sleep)

    for key, rec in pool.items():
        rec["discovered_via"] = sorted(set(provenance.get(key, [])))

    doc = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "query_count": len(queries),
        "candidate_count": len(pool),
        "errors": errors,
        "candidates": sorted(pool.values(), key=lambda r: -r["stars"]),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote {len(pool)} candidates -> {OUT}")
    if errors:
        print(f"{len(errors)} queries errored")


if __name__ == "__main__":
    main()
