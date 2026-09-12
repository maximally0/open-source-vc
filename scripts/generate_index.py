#!/usr/bin/env python3
"""
Build every generated artifact from two inputs:

    curation.yaml              ->  human judgement (category, tier, VC use case)
    metadata/snapshot.json     ->  GitHub-API-verified facts (stars, license, dates)

Outputs:
    categories/*.md            ->  one page per category
    metadata/repositories.json ->  machine-readable directory
    metadata/repositories.yaml ->  same, YAML
    README.md                  ->  regions between GENERATED markers

Markers are used rather than regenerating the README wholesale so that the
hand-written prose in the README is never clobbered by a script run.

Usage:
    python scripts/generate_index.py
    python scripts/generate_index.py --check    # verify inputs, write nothing
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CURATION = ROOT / "curation.yaml"
SNAPSHOT = ROOT / "metadata" / "snapshot.json"
CATEGORIES_DIR = ROOT / "categories"
README = ROOT / "README.md"

TIERS = {
    "essential": ("⭐", "Essential"),
    "interesting": ("🔥", "Interesting"),
    "experimental": ("🧪", "Experimental"),
    "infrastructure": ("🛠", "Infrastructure"),
    "research": ("📚", "Research"),
}

KINDS = ("software", "dataset", "framework", "standard", "research")

# Category slug -> (display title, one-line framing, "what it covers")
CATEGORY_META: dict[str, tuple[str, str, str]] = {
    "founder-discovery": (
        "Founder & Talent Discovery",
        "Finding the people before the round exists.",
        "Founder discovery, technical-talent search, GitHub intelligence, developer "
        "discovery, identity resolution, and talent graphs.",
    ),
    "company-discovery": (
        "Company Discovery & Deal Sourcing",
        "Turning the open web into a pipeline.",
        "Startup and company databases, funding data, company enrichment, inbound "
        "deal flow, and pipeline construction.",
    ),
    "deal-sourcing": (
        "Deal Sourcing & Pipeline",
        "Track, dedupe, and route opportunities without a $50k seat licence.",
        "Sourcing workflow, pipeline management, deduplication, and routing.",
    ),
    "market-research": (
        "Market & Industry Research",
        "Build the map before you take the meeting.",
        "Market mapping, competitive research, industry intelligence, company "
        "comparison, and trend detection.",
    ),
    "osint": (
        "Web Intelligence & OSINT",
        "Systematic collection from public sources.",
        "OSINT frameworks, crawling, scraping, domain intelligence, monitoring, and "
        "change detection.",
    ),
    "relationship-intelligence": (
        "Relationship Intelligence",
        "The actual moat in venture is the network.",
        "CRMs, personal CRMs, relationship graphs, email and calendar intelligence, "
        "warm-introduction paths, and network analysis.",
    ),
    "due-diligence": (
        "Due Diligence",
        "Replace the manual checklist with something repeatable.",
        "Financial, commercial, technical, legal, product, and AI/ML diligence, plus "
        "customer and competitive research.",
    ),
    "document-intelligence": (
        "Data Rooms & Document Intelligence",
        "Data rooms are PDFs. This is how you read 4,000 of them.",
        "PDF parsing, layout-aware extraction, OCR, contract extraction, document "
        "search, and multimodal document understanding.",
    ),
    "investment-analysis": (
        "Investment Analysis",
        "The maths between the meeting and the memo.",
        "Startup and investment scoring, financial analysis, valuation, DCF, "
        "comparables, and scenario modelling.",
    ),
    "cap-tables": (
        "Cap Tables & Equity",
        "Ownership, dilution, and the mechanics of the round.",
        "Cap table modelling, dilution, SAFEs, priced rounds, ownership, liquidation "
        "preferences, and equity standards.",
    ),
    "investment-memos": (
        "Investment Memo & IC",
        "From evidence to a decision the partnership can defend.",
        "Memo generation, IC workflow, scorecards, decision systems, and "
        "citation-backed evidence.",
    ),
    "portfolio-management": (
        "Portfolio Management",
        "The decade after the wire hits.",
        "Portfolio monitoring, KPI collection, dashboards, company updates, risk, "
        "analytics, and founder support.",
    ),
    "lp-management": (
        "LP & Fund Management",
        "Fund maths, LP relationships, and the paperwork in between.",
        "LP CRM and intelligence, fundraising, fund modelling, portfolio "
        "construction, reporting, capital calls, distributions, and waterfalls.",
    ),
    "legal": (
        "Legal & Transaction Infrastructure",
        "Documents that decide the deal.",
        "SAFEs, term sheets, legal NLP, contract analysis, clause extraction, and "
        "transaction infrastructure.",
    ),
    "knowledge-management": (
        "Knowledge Management",
        "Institutional memory beats individual memory.",
        "Knowledge graphs, RAG, semantic search, vector databases, research "
        "notebooks, and internal memory.",
    ),
    "ai-agents": (
        "AI Agents for VC",
        "Research that runs while you sleep.",
        "Research agents, browser agents, multi-agent systems, orchestration, MCP "
        "servers, document agents, and financial agents.",
    ),
    "automation": (
        "Workflow & Automation",
        "Glue. Unglamorous, and the difference between a stack and a folder of scripts.",
        "Workflow automation, ETL, connectors, notifications, integrations, scheduled "
        "research, and chat/email automation.",
    ),
    "standards": (
        "Standards & Schemas",
        "Formats worth adopting before you have to migrate off them.",
        "Cap-table standards, financial data standards, legal schemas, "
        "interoperability formats, and open investment data.",
    ),
    "datasets": (
        "Datasets & Open Data",
        "The raw material your analysis runs on.",
        "Startup and company datasets, developer and repository data, financial and "
        "legal corpora, patent and research indexes, and the tooling to work with them.",
    ),
}


def slug_to_title(slug: str) -> str:
    return CATEGORY_META.get(slug, (slug.replace("-", " ").title(), "", ""))[0]


def fmt_count(n: int | None) -> str:
    if n is None:
        return "unknown"
    if n >= 1000:
        return f"{n / 1000:.1f}k".replace(".0k", "k")
    return str(n)


def fmt_date(iso: str | None) -> str:
    if not iso:
        return "unknown"
    return iso[:10]


def status_of(rec: dict, stale_months: float = 12.0) -> str:
    """Status is derived only from verified fields — never guessed."""
    pushed = rec.get("pushed_at")
    if rec.get("archived"):
        return f"Archived (last push {fmt_date(pushed)})"
    if rec.get("disabled"):
        return "Disabled upstream"
    if not pushed:
        return "unknown"
    try:
        dt = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
    except ValueError:
        return f"Last push {fmt_date(pushed)}"
    months = (datetime.now(timezone.utc) - dt).days / 30.44
    if months >= stale_months:
        return f"Dormant (last push {fmt_date(pushed)}, {months:.0f}mo)"
    return f"Active (last push {fmt_date(pushed)})"


def license_of(rec: dict) -> str:
    spdx = rec.get("license_spdx")
    name = rec.get("license_name")
    if not spdx or spdx in ("NOASSERTION", "NONE"):
        return f"unverified ({name})" if name else "unknown"
    if spdx == "NOASSERTION":
        return "unknown"
    return spdx


def restrictions_of(lic: str, rec: dict) -> str:
    """Report what the licence implies for redistribution. Not legal advice."""
    if lic.startswith("unverified") or lic == "unknown":
        return "unknown - verify upstream before redistributing"
    if lic in ("MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "Unlicense", "0BSD", "CC0-1.0"):
        return f"None stated - {lic} permits redistribution with attribution"
    if lic in ("GPL-2.0", "GPL-3.0", "LGPL-2.1", "LGPL-3.0", "MPL-2.0", "AGPL-3.0", "EUPL-1.2"):
        return f"Copyleft ({lic}) - redistribution permitted, derivative works must carry the same licence"
    if lic.startswith("CC-BY-NC") or "NC" in lic:
        return f"Non-commercial ({lic}) - check before any commercial use"
    if lic in ("CC-BY-4.0", "CC-BY-SA-4.0"):
        return f"Attribution required ({lic})"
    return f"Read the upstream licence ({lic}) - not verified for redistribution"


def fmt_self_host(v) -> str:
    """Render the self-hostable flag as words rather than a Python boolean."""
    if v is True:
        return "yes"
    if v is False:
        return "no"
    if isinstance(v, str) and v.lower() == "partial":
        return "partial (open core)"
    return "unknown"


def entry_md(slug: str, item: dict, rec: dict) -> str:
    tier_key = (item.get("tier") or "interesting").lower()
    icon, tier_label = TIERS.get(tier_key, ("🔥", "Interesting"))
    kind = (item.get("kind") or "software").lower()
    lic = license_of(rec)
    stars = fmt_count(rec.get("stargazers_count"))
    forks = fmt_count(rec.get("forks_count"))
    name = rec.get("full_name") or item["name"]
    display = item.get("display_name") or name.split("/")[-1]

    out: list[str] = []
    out.append(f"### {display}")
    out.append("")
    out.append(f"> {item.get('tagline') or rec.get('description') or 'No description provided upstream.'}")
    out.append("")
    out.append(f"`{name}` &nbsp;·&nbsp; {icon} **{tier_label}** &nbsp;·&nbsp; _{kind}_")
    out.append("")
    out.append("| | |")
    out.append("|---|---|")
    out.append(f"| **Category** | {slug_to_title(slug)} |")
    out.append(f"| **License** | {lic} |")
    out.append(f"| **Stars** | {stars} |")
    out.append(f"| **Forks** | {forks} |")
    out.append(f"| **Language** | {rec.get('language') or 'unknown'} |")
    out.append(f"| **Status** | {status_of(rec)} |")
    out.append(f"| **Self-hostable** | {fmt_self_host(item.get('self_hostable'))} |")
    out.append("")
    out.append("**VC use case**")
    out.append("")
    out.append(str(item.get("vc_use_case", "")).strip())
    out.append("")
    out.append("**Why it's interesting**")
    out.append("")
    out.append(str(item.get("why_interesting", "")).strip())
    out.append("")
    good_for = item.get("good_for") or []
    if good_for:
        out.append("**Good for**")
        out.append("")
        out.extend(f"- {g}" for g in good_for)
        out.append("")
    if item.get("limitations"):
        out.append("**Limitations**")
        out.append("")
        out.append(str(item["limitations"]).strip())
        out.append("")
    if item.get("dependencies"):
        out.append(f"**Dependencies:** {item['dependencies']}")
        out.append("")
    if item.get("notes"):
        out.append(f"**Notes:** {str(item['notes']).strip()}")
        out.append("")
    links = [f"[GitHub]({rec.get('html_url') or item['name']})"]
    if item.get("docs"):
        links.append(f"[Docs]({item['docs']})")
    if item.get("demo"):
        links.append(f"[Demo]({item['demo']})")
    if rec.get("homepage"):
        links.append(f"[Site]({rec['homepage']})")
    out.append("**Links:** " + " &nbsp;·&nbsp; ".join(links))
    out.append("")
    out.append("---")
    out.append("")
    return "\n".join(out)


# Honest notes on coverage. Some parts of the venture workflow simply have very
# little open-source tooling, and saying so is more useful to a reader than
# padding the category with adjacent projects that do not really fit.
CATEGORY_NOTES: dict[str, str] = {
    "cap-tables": (
        "**Coverage note.** This is the thinnest category in the directory, and that is a "
        "finding rather than an oversight. Cap-table software is one of the most commercially "
        "successful niches in venture tooling, and almost none of it is open source: what "
        "exists here is a handful of self-hosted platforms and spreadsheet models, several of "
        "which are not actively maintained. The relevant standard, "
        "[Open Cap Format](../categories/standards.md), is more mature than the tools that "
        "implement it. If you are choosing a cap-table system today, the honest advice is that "
        "this is one place where paying for software is probably the right call, and the open "
        "options are worth knowing about for SPVs, rolling funds, and small vehicles where "
        "per-company pricing does not make sense."
    ),
    "lp-management": (
        "**Coverage note.** Fund and LP administration is the other thin area, and the reason "
        "is structural: this work is regulated, audit-facing, and carries liability, which "
        "makes it a poor fit for hobbyist software. What is genuinely missing from open source "
        "is fund-specific tooling: capital account ledgers with carried interest and waterfall "
        "mechanics, ILPA-style reporting templates, and LP CRM. What does exist, listed here, "
        "is general accounting and modelling machinery that a small fund or SPV can run its "
        "books on with some assembly. Treat this category as a starting point for building "
        "something, not as a replacement for a fund administrator."
    ),
    "datasets": (
        "**Coverage note.** Open datasets relevant to venture are thinner than the software "
        "here, and the licensing is messier: non-commercial clauses and attribution "
        "requirements are common in data where they are rare in code, so check each one before "
        "you use it. The datasets that would be most valuable, compiled private-company "
        "funding and cap-table data, are precisely the ones no one gives away. What you find "
        "here is public, government, and academic data plus the tooling to work with it, which "
        "is enough to build a sourcing or diligence dataset of your own but not enough to skip "
        "the commercial providers."
    ),
    "deal-sourcing": (
        "**Coverage note.** Deal-flow tooling splits cleanly in two, and open source only "
        "covers one half. The generic half, monitoring, change detection, databases, and "
        "notification, is well served and listed here. The specific half, the compiled "
        "private-company graphs where most sourcing actually happens, is entirely commercial. "
        "Expect to combine these tools with a paid data source rather than replacing it."
    ),
    "founder-discovery": (
        "**Coverage note.** The tools here are general-purpose people and web research rather "
        "than venture-specific talent software. There is no open equivalent of a technical "
        "talent graph or a founder database, because those are built on proprietary "
        "professional-network data. What an analyst gets from this category is the ability to "
        "verify and enrich a person's public footprint independently, which is often enough."
    ),
    "company-discovery": (
        "**Coverage note.** Company discovery in open source means building your own company "
        "graph from public sources, and the best starting material is the one authoritative "
        "dataset here: Y Combinator's own API. Beyond that, coverage of private companies is a "
        "function of what you collect. Nothing in this category replaces a commercial database, "
        "but several of these entries make a homemade one viable for a specific sector."
    ),
    "investment-memos": (
        "**Coverage note.** Memo tooling is the least mature area here, and the reason is "
        "straightforward: a memo is the part of the process that most resists automation, "
        "because its value is the judgement in it. What these entries offer is scaffolding, "
        "typesetting, and reproducibility, which removes the blank-page problem and the "
        "copy-paste errors without pretending to make the argument for you."
    ),
    "standards": (
        "**Coverage note.** Two important open standards are deliberately absent because they "
        "are not hosted on a code forge: the Series Seed document set and the GLEIF Legal "
        "Entity Identifier registry. Both are genuine standards worth knowing, both live on "
        "their own websites rather than as repositories, and this directory links "
        "repositories, so they are noted here rather than listed. What is included is the "
        "financial-reporting toolchain around XBRL, which is the format through which most "
        "structured financial data reaches a fund."
    ),
}


def write_category_page(slug: str, items: list[tuple[dict, dict]], updated: str) -> int:
    title, framing, covers = CATEGORY_META.get(slug, (slug_to_title(slug), "", ""))
    lines = [
        f"# {title}",
        "",
        f"_{framing}_",
        "",
        covers,
        "",
        f"**{len(items)} project(s)** &nbsp;·&nbsp; [← back to index](../README.md) "
        f"&nbsp;·&nbsp; metadata updated {updated}",
        "",
        "> Every field below is read from the GitHub API at the date stamped above. "
        "The VC use case and tier are editorial judgement. See "
        "[METHODOLOGY.md](../METHODOLOGY.md).",
        "",
    ]
    if slug in CATEGORY_NOTES:
        lines += [CATEGORY_NOTES[slug], ""]
    lines += ["---", ""]
    order = {"essential": 0, "interesting": 1, "infrastructure": 2, "experimental": 3, "research": 4}
    for item, rec in sorted(items, key=lambda p: (order.get((p[0].get("tier") or "").lower(), 9),
                                                 -(p[1].get("stargazers_count") or 0))):
        lines.append(entry_md(slug, item, rec))
    CATEGORIES_DIR.mkdir(parents=True, exist_ok=True)
    (CATEGORIES_DIR / f"{slug}.md").write_text("\n".join(lines), encoding="utf-8")
    return len(items)


def build_records(curation: dict, snapshot: dict) -> list[dict]:
    records = []
    missing = []
    for item in curation["repos"]:
        name = item["name"]
        rec = snapshot["repos"].get(name)
        if rec is None:
            missing.append(name)
            rec = {"full_name": name, "html_url": f"https://github.com/{name}", "archived": None}
        lic = license_of(rec)
        records.append({
            "name": rec.get("full_name") or name,
            "display_name": item.get("display_name") or name.split("/")[-1],
            "github": rec.get("html_url") or f"https://github.com/{name}",
            "description": item.get("tagline") or rec.get("description") or "",
            "category": item["category"],
            "tier": (item.get("tier") or "interesting").lower(),
            "kind": (item.get("kind") or "software").lower(),
            "vc_native": bool(item.get("vc_native", False)),
            "ai": bool(item.get("ai", False)),
            "best_for": item.get("best_for") or (item.get("good_for") or [""])[0],
            "starter": bool(item.get("starter", False)),
            "hidden_gem": bool(item.get("hidden_gem", False)),
            "starter_order": item.get("starter_order"),
            "vc_use_case": str(item.get("vc_use_case", "")).strip(),
            "why_it_is_interesting": str(item.get("why_interesting", "")).strip(),
            "good_for": item.get("good_for") or [],
            "limitations": str(item.get("limitations", "")).strip() or None,
            "license": lic,
            "license_name": rec.get("license_name") or "unknown",
            "stars": rec.get("stargazers_count"),
            "forks": rec.get("forks_count"),
            "open_issues": rec.get("open_issues_count"),
            "contributors": item.get("contributors", "unknown"),
            "last_commit": fmt_date(rec.get("pushed_at")),
            "created": fmt_date(rec.get("created_at")),
            "language": rec.get("language") or "unknown",
            "status": status_of(rec) if rec.get("pushed_at") is not None or rec.get("archived") else "unknown",
            "archived": rec.get("archived"),
            "installation": item.get("installation", "See upstream README"),
            "documentation": item.get("docs") or "unknown",
            "demo": item.get("demo") or "unknown",
            "dependencies": item.get("dependencies", "unknown"),
            "self_hostable": item.get("self_hostable", "unknown"),
            "commercial_restrictions": item.get("commercial_restrictions") or restrictions_of(lic, rec),
            "owner_type": rec.get("owner_type", "unknown"),
            "links_verified": item.get("links_verified", "unknown"),
            "notes": str(item.get("notes", "")).strip() or None,
        })
    return records, missing


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="validate inputs without writing")
    args = ap.parse_args()

    if not CURATION.exists():
        sys.exit(f"Missing {CURATION}")
    if not SNAPSHOT.exists():
        sys.exit(f"Missing {SNAPSHOT}. Run `python scripts/update.py` first.")

    curation = yaml.safe_load(CURATION.read_text(encoding="utf-8"))
    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    repos = curation.get("repos") or []
    if not repos:
        sys.exit("curation.yaml has no repos.")

    records, missing = build_records(curation, snapshot)
    updated = (snapshot.get("generated_at") or "")[:10] or datetime.now(timezone.utc).date().isoformat()

    by_cat: dict[str, list] = {}
    for item, rec in zip(repos, records):
        by_cat.setdefault(item["category"], []).append((item, snapshot["repos"].get(item["name"], {})))

    unknown_cats = sorted(set(by_cat) - set(CATEGORY_META))
    unknown_tiers = sorted({r["tier"] for r in records} - set(TIERS))
    unknown_kinds = sorted({r["kind"] for r in records} - set(KINDS))

    print(f"repos: {len(records)}  categories: {len(by_cat)}")
    if missing:
        print(f"  ! {len(missing)} repo(s) absent from snapshot: {', '.join(missing[:10])}")
    if unknown_cats:
        print(f"  ! unknown categories: {unknown_cats}")
    if unknown_tiers:
        print(f"  ! unknown tiers: {unknown_tiers}")
    if unknown_kinds:
        print(f"  ! unknown kinds: {unknown_kinds}")
    if args.check:
        print("check only; nothing written")
        return

    # metadata/
    meta_dir = ROOT / "metadata"
    meta_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": snapshot.get("generated_at"),
        "generator": "scripts/generate_index.py",
        "repo_count": len(records),
        "categories": {slug: len(v) for slug, v in sorted(by_cat.items())},
        "tiers": {t: sum(1 for r in records if r["tier"] == t) for t in TIERS},
        "kinds": {k: sum(1 for r in records if r["kind"] == k) for k in KINDS},
        "repositories": records,
    }
    (meta_dir / "repositories.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=False), encoding="utf-8")

    yaml_payload = {
        "generated_at": snapshot.get("generated_at"),
        "repo_count": len(records),
        "repositories": records,
    }
    (meta_dir / "repositories.yaml").write_text(
        yaml.safe_dump(yaml_payload, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8")

    # categories/
    for slug, items in sorted(by_cat.items()):
        n = write_category_page(slug, items, updated)
        print(f"  categories/{slug}.md  ({n})")

    # top-level generated pages
    write_comparison(records, updated)
    write_workflow(records, updated)
    write_starter_pack(records, updated)
    write_hidden_gems(records, updated)

    # README generated regions
    if README.exists():
        text = README.read_text(encoding="utf-8")

        cat_lines = ["| Category | Projects | What it covers |", "|---|---:|---|"]
        for slug in sorted(by_cat, key=lambda s: -len(by_cat[s])):
            title, _, covers = CATEGORY_META.get(slug, (slug_to_title(slug), "", ""))
            short = covers.split(",")[0].strip().rstrip(".")
            cat_lines.append(f"| [{title}](categories/{slug}.md) | {len(by_cat[slug])} | {short} |")
        text = replace_region(text, "categories", "\n".join(cat_lines))

        ess = [r for r in records if r["tier"] == "essential"]
        ess.sort(key=lambda r: -(r["stars"] or 0))
        ess_lines = ["| Project | Category | Stars | License | Why |", "|---|---|---:|---|---|"]
        for r in ess:
            first = re.split(r"(?<=[.!?])\s", r["vc_use_case"])[0]
            ess_lines.append(
                f"| [{r['display_name']}]({r['github']}) | {slug_to_title(r['category'])} | "
                f"{fmt_count(r['stars'])} | {r['license']} | {first} |")
        text = replace_region(text, "essentials", "\n".join(ess_lines))

        tier_counts = payload["tiers"]
        stats = (f"**{len(records)}** curated projects across **{len(by_cat)}** categories "
                 f"&nbsp;·&nbsp; {tier_counts.get('essential', 0)} Essential "
                 f"&nbsp;·&nbsp; {tier_counts.get('interesting', 0)} Interesting "
                 f"&nbsp;·&nbsp; {tier_counts.get('infrastructure', 0)} Infrastructure "
                 f"&nbsp;·&nbsp; {tier_counts.get('experimental', 0)} Experimental "
                 f"&nbsp;·&nbsp; {tier_counts.get('research', 0)} Research")
        text = replace_region(text, "stats", stats)
        text = replace_region(text, "updated", updated)
        README.write_text(text, encoding="utf-8")
        print("  README.md regions updated")

    print(f"\nWrote {len(records)} records.")


WORKFLOW_STAGES: list[tuple[str, str, list[str]]] = [
    ("Sourcing", "Surface companies before they are on anyone's list.",
     ["company-discovery", "deal-sourcing", "founder-discovery"]),
    ("Founder research", "Who is this person, what have they built, can I reach them.",
     ["founder-discovery", "osint", "relationship-intelligence"]),
    ("Company research", "What does the product actually do, and how is it built.",
     ["company-discovery", "osint", "market-research"]),
    ("Market research", "Size the market, map the competition, find the wedge.",
     ["market-research", "knowledge-management"]),
    ("Initial screening", "Decide whether this deserves a meeting.",
     ["investment-analysis", "investment-memos", "company-discovery"]),
    ("Meeting", "Notes, context, and the relationship record afterwards.",
     ["relationship-intelligence", "knowledge-management"]),
    ("Due diligence", "Financial, commercial, technical, and legal workstreams.",
     ["due-diligence", "document-intelligence", "legal", "osint"]),
    ("Financial analysis", "Model the business, the round, and the outcomes.",
     ["investment-analysis", "cap-tables"]),
    ("Legal DD", "Contracts, cap table, corporate structure, encumbrances.",
     ["legal", "document-intelligence", "cap-tables"]),
    ("Investment memo", "Turn evidence into a written recommendation.",
     ["investment-memos", "knowledge-management"]),
    ("IC", "Score, debate, decide, and record why.",
     ["investment-memos", "knowledge-management"]),
    ("Investment", "Documents, signatures, and the money moving.",
     ["legal", "cap-tables"]),
    ("Portfolio monitoring", "Track KPIs, updates, and risk across the book.",
     ["portfolio-management", "relationship-intelligence", "automation"]),
    ("Follow-on", "Double down or pass, with the data to justify it.",
     ["portfolio-management", "cap-tables", "investment-analysis"]),
    ("Exit", "Secondary, acquisition, or IPO — plus the LP side of the proceeds.",
     ["investment-analysis", "lp-management", "legal"]),
    ("Fund & LP operations", "Fund maths, LP reporting, capital calls, waterfalls.",
     ["lp-management", "investment-analysis"]),
    ("Knowledge & memory", "Everything above, remembered and searchable.",
     ["knowledge-management", "document-intelligence"]),
    ("Automation glue", "Make the rest of it run without a human.",
     ["automation", "ai-agents", "osint"]),
]


def write_comparison(records: list[dict], updated: str) -> None:
    """The comparison matrix. Every column is derived, not asserted by hand."""
    lines = [
        "# Comparison Matrix",
        "",
        "One row per curated project, flattened so you can sort and filter it. "
        "This is the page to open when you are choosing between three tools that "
        "all claim to do the same thing.",
        "",
        "**How to read it**",
        "",
        "- **VC native** — built explicitly for venture capital or private markets. "
        "`No` does not make it worse; it means you are adapting a general tool, "
        "usually at a much lower price.",
        "- **OSS** — the licence as published upstream. `unverified` means the repo "
        "has no detectable licence file, so treat redistribution as off-limits. "
        "See [METHODOLOGY.md](METHODOLOGY.md#licensing).",
        "- **Self-host** — can you run it on your own infrastructure without a paid "
        "tier. `partial` means an open core with commercial hosted extras.",
        "- **AI** — the tool's core function depends on a model, rather than AI being "
        "a bolted-on feature.",
        "- **Tier** — editorial label. See [METHODOLOGY.md](METHODOLOGY.md#tiers).",
        "",
        f"_{len(records)} projects · metadata updated {updated}_",
        "",
        "| Project | Category | Tier | VC native | OSS | Self-host | AI | Kind | Stars | Best for |",
        "|---|---|---|---|---|---|---|---|---:|---|",
    ]
    order = {"essential": 0, "interesting": 1, "infrastructure": 2, "experimental": 3, "research": 4}
    for r in sorted(records, key=lambda r: (order.get(r["tier"], 9), -(r["stars"] or 0))):
        lines.append(
            f"| [{r['display_name']}]({r['github']}) "
            f"| [{slug_to_title(r['category'])}](categories/{r['category']}.md) "
            f"| {TIERS.get(r['tier'], ('', r['tier']))[1]} "
            f"| {'Yes' if r['vc_native'] else 'No'} "
            f"| {r['license']} "
            f"| {r['self_hostable'] if isinstance(r['self_hostable'], str) else ('yes' if r['self_hostable'] else 'no')} "
            f"| {'Yes' if r['ai'] else 'No'} "
            f"| {r['kind']} "
            f"| {fmt_count(r['stars'])} "
            f"| {r['best_for']} |")
    lines += [
        "",
        "---",
        "",
        "## Filtering this table",
        "",
        "`metadata/repositories.json` carries the same fields as structured data, so "
        "you can rebuild any view you want:",
        "",
        "```bash",
        "# every self-hostable, AI-native tool in diligence",
        "python -c \"import json;d=json.load(open('metadata/repositories.json'));\\",
        "[print(r['name']) for r in d['repositories'] \\",
        " if r['category']=='due-diligence' and r['ai'] and r['self_hostable'] is True]\"",
        "```",
        "",
    ]
    (ROOT / "COMPARISON.md").write_text("\n".join(lines), encoding="utf-8")
    print("  COMPARISON.md")


def write_workflow(records: list[dict], updated: str, per_stage: int = 6) -> None:
    """The VC workflow map: every stage of the process, with real projects under it."""
    by_cat: dict[str, list[dict]] = {}
    for r in records:
        by_cat.setdefault(r["category"], []).append(r)
    for v in by_cat.values():
        v.sort(key=lambda r: ({"essential": 0, "interesting": 1, "infrastructure": 2,
                               "experimental": 3, "research": 4}.get(r["tier"], 9),
                              -(r["stars"] or 0)))

    lines = [
        "# The VC Workflow, Mapped to Open Source",
        "",
        "Venture is a pipeline with a dozen stages, and most funds buy a different "
        "SaaS product for each one. This page maps the whole process and shows what "
        "open source covers at every step — including the stages nobody sells software for.",
        "",
        "```text",
        "Sourcing → Founder research → Company research → Market research",
        "   → Screening → Meeting → Due diligence → Financial analysis",
        "   → Legal DD → Memo → IC → Investment → Portfolio monitoring",
        "   → Follow-on → Exit → (and back to Sourcing)",
        "```",
        "",
        f"_{updated} · {len(records)} projects mapped_",
        "",
        "---",
        "",
    ]
    for stage, blurb, cats in WORKFLOW_STAGES:
        pool: list[dict] = []
        for c in cats:
            pool.extend(by_cat.get(c, []))
        seen, unique = set(), []
        for r in pool:
            if r["name"] not in seen:
                seen.add(r["name"])
                unique.append(r)
        if not unique:
            continue
        lines += [
            f"## {stage}",
            "",
            f"_{blurb}_",
            "",
            "| Project | Tier | Stars | License | VC use case |",
            "|---|---|---:|---|---|",
        ]
        for r in unique[:per_stage]:
            first = re.split(r"(?<=[.!?])\s", r["vc_use_case"])[0]
            lines.append(
                f"| [{r['display_name']}]({r['github']}) "
                f"| {TIERS.get(r['tier'], ('', r['tier']))[1]} "
                f"| {fmt_count(r['stars'])} | {r['license']} | {first} |")
        lines.append("")
        related = ", ".join(f"[{slug_to_title(c)}](categories/{c}.md)" for c in cats
                            if by_cat.get(c))
        if related:
            lines += [f"Full category pages: {related}", ""]
        lines.append("---")
        lines.append("")

    lines += [
        "## What open source does *not* cover",
        "",
        "Worth saying plainly, because the gaps are where your budget goes:",
        "",
        "- **Proprietary deal-flow databases.** The compiled private-company graphs "
        "(funding rounds, valuations, cap tables) are the moat of the incumbents. "
        "Open source gives you the tools to build your own; it does not hand you "
        "the data.",
        "- **Compliance and fund administration.** Regulated, audit-facing processes "
        "with real liability. Nobody serious runs a fund's books on a hobby project.",
        "- **Network effects.** The best deal flow is a byproduct of being known. No "
        "repository fixes that.",
        "",
    ]
    (ROOT / "VC_WORKFLOW.md").write_text("\n".join(lines), encoding="utf-8")
    print("  VC_WORKFLOW.md")


def write_starter_pack(records: list[dict], updated: str) -> None:
    """The 20-30 project on-ramp, ordered the way the work actually happens."""
    picked = [r for r in records if r["starter"]]
    picked.sort(key=lambda r: (r["starter_order"] if r["starter_order"] is not None else 999,
                               -(r["stars"] or 0)))

    # group by the workflow stage each project's category belongs to
    stage_of: dict[str, int] = {}
    for idx, (stage, _, cats) in enumerate(WORKFLOW_STAGES):
        for c in cats:
            stage_of.setdefault(c, idx)

    groups: dict[str, list[dict]] = {}
    for r in picked:
        key = next((s for s, _, cats in WORKFLOW_STAGES if r["category"] in cats), "Other")
        groups.setdefault(key, []).append(r)

    ordered = sorted(groups.items(), key=lambda kv: stage_of.get(
        next((c for _, _, cats in WORKFLOW_STAGES for c in cats if c in
              {r["category"] for r in kv[1]}), ""), 99))

    lines = [
        "# The VC Open Source Starter Pack",
        "",
        "If you are new to this — an analyst on week one, an emerging manager with no "
        "platform team, a scout with your own laptop — start here. Not with 200 "
        "repositories. With these.",
        "",
        f"**{len(picked)} projects**, arranged in the order a deal actually moves through "
        "the fund. Each one earns its place by replacing a paid product you would "
        "otherwise need, or by doing something no paid product does.",
        "",
        "```text",
        "Find companies → Research founders → Research markets → Run diligence",
        "   → Read the documents → Model the investment → Write the memo",
        "   → Track the portfolio",
        "```",
        "",
        "Pair this with [VC_WORKFLOW.md](VC_WORKFLOW.md) for the full process map and "
        "[COMPARISON.md](COMPARISON.md) when you are choosing between options.",
        "",
        f"_{updated}_",
        "",
        "---",
        "",
    ]
    for stage, items in ordered:
        lines += [f"## {stage}", ""]
        for r in items:
            first = re.split(r"(?<=[.!?])\s", r["vc_use_case"])[0]
            lines += [
                f"**[{r['display_name']}]({r['github']})** — {r['description'] or 'no description'}",
                "",
                f"`{r['license']}` · {fmt_count(r['stars'])}★ · "
                f"{TIERS.get(r['tier'], ('', r['tier']))[1]} · "
                f"[{slug_to_title(r['category'])}](categories/{r['category']}.md)",
                "",
                f"{first}",
                "",
            ]
        lines += ["---", ""]
    (ROOT / "STARTER_PACK.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"  STARTER_PACK.md ({len(picked)})")


def write_hidden_gems(records: list[dict], updated: str) -> None:
    """Small, brilliant, or underrepresented projects. Explicitly not star-ranked."""
    gems = [r for r in records if r["hidden_gem"]]
    gems.sort(key=lambda r: (r["display_name"].lower()))

    lines = [
        "# Hidden Gems",
        "",
        "The most valuable page here, and the one that required the most work.",
        "",
        "Every entry below is deliberately **not** ranked by stars. A repository with "
        "900 stars that solves a specific analyst problem is worth more to you than a "
        "20,000-star framework you will never deploy. These are the projects that make "
        "a VC analyst stop scrolling:",
        "",
        "- built by people who actually work in venture, or in a domain adjacent enough "
        "that they understood the problem",
        "- tiny but sharp — one idea, executed properly",
        "- recently emerged and not yet obvious",
        "- academically sound and not yet productised",
        f"",
        f"**{len(gems)} projects.** If you only read two pages of this repository, make "
        "it this one and the [Starter Pack](STARTER_PACK.md).",
        "",
        f"_{updated}_",
        "",
        "---",
        "",
    ]
    for r in gems:
        lines += [
            f"## {r['display_name']}",
            "",
            f"> {r['description'] or 'No description provided upstream.'}",
            "",
            f"`{r['name']}` · `{r['license']}` · {fmt_count(r['stars'])}★ · "
            f"{TIERS.get(r['tier'], ('', r['tier']))[1]} · "
            f"[{slug_to_title(r['category'])}](categories/{r['category']}.md)",
            "",
            f"**Why it is here:** {r['why_it_is_interesting']}",
            "",
            f"**VC use case:** {r['vc_use_case']}",
            "",
        ]
        if r["limitations"]:
            lines += [f"**Limitations:** {r['limitations']}", ""]
        lines += [f"[GitHub]({r['github']})", "", "---", ""]
    (ROOT / "HIDDEN_GEMS.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"  HIDDEN_GEMS.md ({len(gems)})")


def replace_region(text: str, key: str, body: str) -> str:
    start = f"<!-- BEGIN GENERATED:{key} -->"
    end = f"<!-- END GENERATED:{key} -->"
    if start not in text or end not in text:
        print(f"  ! README region '{key}' markers missing; skipped")
        return text
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    return pattern.sub(f"{start}\n{body}\n{end}", text)


if __name__ == "__main__":
    main()
