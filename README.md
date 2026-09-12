<div align="center">

# Open Source VC

**A curated map of the open-source software, datasets, standards, and infrastructure that venture capital actually runs on.**

From sourcing a company to writing the memo to tracking it for ten years — what you can build yourself, and what it costs to rely on it.

<!-- BEGIN GENERATED:stats -->
**226** curated projects across **19** categories &nbsp;·&nbsp; 39 Essential &nbsp;·&nbsp; 117 Interesting &nbsp;·&nbsp; 20 Infrastructure &nbsp;·&nbsp; 36 Experimental &nbsp;·&nbsp; 14 Research
<!-- END GENERATED:stats -->

[**Starter Pack**](STARTER_PACK.md) · [**Hidden Gems**](HIDDEN_GEMS.md) · [**VC Workflow**](VC_WORKFLOW.md) · [**Comparison Matrix**](COMPARISON.md) · [**Methodology**](METHODOLOGY.md) · [**Contributing**](CONTRIBUTING.md)

<!-- BEGIN GENERATED:updated -->
2026-09-12
<!-- END GENERATED:updated -->

</div>

---

## What this is

A directory, not a product. Every entry is a real, inspectable repository you can clone, read, and run — plus an honest note about what it is good for, what it is not, and what the licence lets you do with it.

It answers one question:

> I work in venture capital. What open-source software can I use for sourcing, diligence, research, portfolio management, relationship intelligence, financial analysis, and legal work — and which of it is actually worth my time?

## Who it is for

Analysts, associates, principals, partners, emerging managers, angels, scouts, platform teams, people building internal fund tooling, and researchers studying the industry. If you are the only person at your fund who writes code, this was built for you.

## Start here

| If you want | Read |
|---|---|
| The shortlist — 32 projects, in the order a deal moves | [**STARTER_PACK.md**](STARTER_PACK.md) |
| The projects nobody has told you about yet | [**HIDDEN_GEMS.md**](HIDDEN_GEMS.md) |
| Every stage of the venture process, with tools under it | [**VC_WORKFLOW.md**](VC_WORKFLOW.md) |
| To choose between three tools that do the same thing | [**COMPARISON.md**](COMPARISON.md) |
| To understand how entries are judged, and why | [**METHODOLOGY.md**](METHODOLOGY.md) |
| To build a stack from scratch, end to end | [**guides/build-your-own-vc-stack.md**](guides/build-your-own-vc-stack.md) |

## Category index

<!-- BEGIN GENERATED:categories -->
| Category | Projects | What it covers |
|---|---:|---|
| [Knowledge Management](categories/knowledge-management.md) | 25 | Knowledge graphs |
| [Data Rooms & Document Intelligence](categories/document-intelligence.md) | 24 | PDF parsing |
| [Web Intelligence & OSINT](categories/osint.md) | 17 | OSINT frameworks |
| [Market & Industry Research](categories/market-research.md) | 16 | Market mapping |
| [Legal & Transaction Infrastructure](categories/legal.md) | 15 | SAFEs |
| [Investment Analysis](categories/investment-analysis.md) | 14 | Startup and investment scoring |
| [AI Agents for VC](categories/ai-agents.md) | 14 | Research agents |
| [Standards & Schemas](categories/standards.md) | 14 | Cap-table standards |
| [Relationship Intelligence](categories/relationship-intelligence.md) | 12 | CRMs |
| [Workflow & Automation](categories/automation.md) | 12 | Workflow automation |
| [Due Diligence](categories/due-diligence.md) | 10 | Financial |
| [Portfolio Management](categories/portfolio-management.md) | 9 | Portfolio monitoring |
| [Founder & Talent Discovery](categories/founder-discovery.md) | 8 | Founder discovery |
| [Company Discovery & Deal Sourcing](categories/company-discovery.md) | 7 | Startup and company databases |
| [LP & Fund Management](categories/lp-management.md) | 7 | LP CRM and intelligence |
| [Datasets & Open Data](categories/datasets.md) | 7 | Startup and company datasets |
| [Deal Sourcing & Pipeline](categories/deal-sourcing.md) | 6 | Sourcing workflow |
| [Investment Memo & IC](categories/investment-memos.md) | 6 | Memo generation |
| [Cap Tables & Equity](categories/cap-tables.md) | 3 | Cap table modelling |
<!-- END GENERATED:categories -->

## Essential projects

The short version. <span title="Tier definitions are in METHODOLOGY.md">⭐ Essential</span> means: broadly useful, well maintained, and something a competent analyst would get value from within an hour of installing it.

<!-- BEGIN GENERATED:essentials -->
| Project | Category | Stars | License | Why |
|---|---|---:|---|---|
| [n8n](https://github.com/n8n-io/n8n) | Workflow & Automation | 204.1k | unverified (Other) | The connective tissue a fund needs: a new deal lands in a form, gets enriched, appears in the pipeline, and pings the right partner. |
| [browser-use](https://github.com/browser-use/browser-use) | AI Agents for VC | 114.3k | MIT | The tool that makes research agents actually work, because most of the useful public information sits behind JavaScript, logins, and search boxes rather than an API. |
| [Whisper](https://github.com/openai/whisper) | Relationship Intelligence | 108.9k | MIT | Turn founder calls into a transcript you can search, quote in a memo, and keep as part of the record. |
| [Sherlock](https://github.com/sherlock-project/sherlock) | Founder & Talent Discovery | 91.4k | MIT | When a founder's name is common or their LinkedIn is thin, an analyst runs the handle they use elsewhere through Sherlock to see where else that handle exists. |
| [RAGFlow](https://github.com/infiniflow/ragflow) | Knowledge Management | 90.6k | Apache-2.0 | The knowledge layer a fund builds once so that memos, filings, and data-room material are answerable with citations. |
| [MCP Servers](https://github.com/modelcontextprotocol/servers) | AI Agents for VC | 90.3k | unverified (Other) | MCP is how an assistant gets access to real systems, and this is where the working patterns live: files, databases, git, search, and the plumbing for connecting them. |
| [OpenBB](https://github.com/OpenBB-finance/OpenBB) | Investment Analysis | 72.9k | unverified (Other) | Public comparables work: pull financials, prices, and fundamentals for the listed companies a target competes with, then build the trading multiples that anchor a valuation conversation. |
| [Docling](https://github.com/docling-project/docling) | Data Rooms & Document Intelligence | 66.3k | MIT | Financial statements and contracts are where layout carries meaning: which number sits in which column, which heading a clause falls under. |
| [NocoDB](https://github.com/nocodb/nocodb) | Deal Sourcing & Pipeline | 64.9k | unverified (Other) | The deals pipeline most small funds actually need: stages, owners, next actions, and notes, as a grid anyone on the team can edit, sitting on a real database you control. |
| [Twenty](https://github.com/twentyhq/twenty) | Relationship Intelligence | 56.6k | unverified (Other) | The team version: contacts, companies, and opportunities that match how a fund works, in a shared system rather than four analysts' personal notes. |
| [LlamaIndex](https://github.com/run-llama/llama_index) | AI Agents for VC | 52.1k | MIT | The most common foundation for a fund's document assistant: load a data room, build an index, and query it with citations. |
| [Metabase](https://github.com/metabase/metabase) | Portfolio Management | 49.2k | unverified (Other) | Portfolio dashboards a partner will actually open: capital deployed by vintage, sector exposure, KPI collection across the book, and which companies are behind plan. |
| [Cal.com](https://github.com/calcom/cal.diy) | Relationship Intelligence | 48.4k | MIT | Founder calls, LP check-ins, and office hours all live or die on scheduling. |
| [Apache Airflow](https://github.com/apache/airflow) | Workflow & Automation | 46.8k | Apache-2.0 | When a fund's data work becomes real: nightly collection jobs, enrichment pipelines, and reports that have to run in order and tell someone when they fail. |
| [Streamlit](https://github.com/streamlit/streamlit) | Portfolio Management | 45.7k | Apache-2.0 | The internal tool a fund builds once and uses daily: a company scorecard, an LP-return calculator, a portfolio KPI collector, a sourcing triage form. |
| [Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | Data Rooms & Document Intelligence | 45k | GPL-3.0 | The document archive for a fund or a family office: every contract, statement, and filing OCR'd, tagged, and full-text searchable, with the original file retained. |
| [LangGraph](https://github.com/langchain-ai/langgraph) | AI Agents for VC | 41.5k | MIT | The right shape for a diligence workflow, where steps depend on what earlier steps found and a human needs to approve before the next stage. |
| [Marker](https://github.com/datalab-to/marker) | Data Rooms & Document Intelligence | 39.7k | Apache-2.0 | The workhorse for converting a data room into text an analyst or a model can read. |
| [Khoj](https://github.com/khoj-ai/khoj) | Market & Industry Research | 37.3k | AGPL-3.0 | A fund's institutional memory problem: a hundred memos, data-room exports, and meeting notes that nobody can search. |
| [GraphRAG](https://github.com/microsoft/graphrag) | Knowledge Management | 36k | MIT | The questions a fund asks are relational: which companies in this sector share an investor, which founders came from the same company, where does this supply chain concentrate. |
| [Web-Check](https://github.com/lissy93/web-check) | Founder & Talent Discovery | 34.8k | MIT | Point it at a target company's domain and get its hosting, DNS and mail records, TLS configuration, exposed headers, and third-party services. |
| [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | Data Rooms & Document Intelligence | 34.7k | MPL-2.0 | The unglamorous step that makes everything else possible. |
| [changedetection.io](https://github.com/dgtlmoon/changedetection.io) | Deal Sourcing & Pipeline | 33.8k | Apache-2.0 | The narrow version of monitoring and the one analysts actually need: a competitor drops a price, adds a plan, edits a terms page, or a portfolio company quietly reshuffles its team page. |
| [STORM](https://github.com/stanford-oval/storm) | Market & Industry Research | 31.3k | MIT | Ask it to produce a briefing on a sector and it researches, outlines, and drafts with references. |
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher) | Market & Industry Research | 29.4k | Apache-2.0 | Hand it a market question, such as how many companies are selling continuous compliance tooling into European banks and who funded them, and it returns a written answer with the sources it used. |
| [Monica](https://github.com/monicahq/monica) | Relationship Intelligence | 25.3k | AGPL-3.0 | Every investor keeps the same private list: who introduced whom, what they care about, when you last spoke, what you promised. |
| [yfinance](https://github.com/ranaroussi/yfinance) | Investment Analysis | 25.2k | Apache-2.0 | The fastest way to get prices, financials, and history for a comparable set. |
| [SingleFile](https://github.com/gildas-lormeau/SingleFile) | Web Intelligence & OSINT | 22.4k | AGPL-3.0 | Evidence capture. |
| [Airbyte](https://github.com/airbytehq/airbyte) | Workflow & Automation | 22k | unverified (Other) | The ingestion layer: get data out of a CRM, a billing system, an accounting package, or a portfolio company's tooling and into the fund's own database. |
| [NetworkX](https://github.com/networkx/networkx) | Relationship Intelligence | 17.3k | unverified (Other) | The warm-introduction question that every fund asks and almost none can answer systematically: which of our contacts is closest to this founder, and through whom. |
| [Unstructured](https://github.com/Unstructured-IO/unstructured) | Data Rooms & Document Intelligence | 15.4k | Apache-2.0 | A data room is a pile of PDFs, slide decks, spreadsheets, and scans in no particular order. |
| [dbt](https://github.com/dbt-labs/dbt) | Workflow & Automation | 13.8k | Apache-2.0 | Turns a fund's raw company and portfolio tables into the clean models that reporting depends on, with tests that catch a broken number before it reaches a partner. |
| [PaperQA](https://github.com/Future-House/paper-qa) | Due Diligence | 9.2k | Apache-2.0 | Technical diligence on a deep-tech company: read the founders' papers and patents, then ask whether the claimed result holds up, with page-level citations. |
| [Mike](https://github.com/open-legal-products/mike) | Legal & Transaction Infrastructure | 4.2k | AGPL-3.0 | Contract review is the most expensive line item in a deal that nobody talks about. |
| [edgartools](https://github.com/dgunning/edgartools) | Investment Analysis | 2.7k | MIT | Public filings are the best free source on a listed company's real economics, and they are hostile to read. |
| [Captable](https://github.com/captableinc/captable) | Cap Tables & Equity | 822 | AGPL-3.0 | The cap table, dilution modelling, and stakeholder records that every fund currently pays a vendor for. |
| [Arelle](https://github.com/Arelle/Arelle) | Standards & Schemas | 236 | unverified (Other) | XBRL is how financial statements arrive from public companies and increasingly from private reporting. |
| [YC Open API](https://github.com/yc-oss/api) | Company Discovery & Deal Sourcing | 231 | unknown | Every YC company with its batch, industry, team size, status, and founders, plus a website field. |
| [Open Cap Format](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF) | Standards & Schemas | 188 | unverified (Other) | Cap tables currently move between founders, lawyers, and investors as spreadsheets in whatever shape the last person used. |
<!-- END GENERATED:essentials -->

Full reasoning for every one of these is on its category page.

---

## How projects are selected

The bar is deliberately high, and most things fail it. Every entry is inspected upstream — README, `LICENSE`, repository structure, commit history, releases, issues — and its metadata is read from the GitHub API rather than copied from a list.

Five labels, no fake precision:

| | Label | Meaning |
|---|---|---|
| ⭐ | **Essential** | Excellent and broadly useful. Recommended to anyone in the workflow. |
| 🔥 | **Interesting** | Particularly innovative or unusually well executed. |
| 🛠 | **Infrastructure** | Not VC-specific, but an excellent building block. |
| 🧪 | **Experimental** | Early, incomplete, possibly important. Use with your eyes open. |
| 📚 | **Research** | Useful for understanding an approach, dataset, or direction. |

There are no numeric scores. A `84/100` implies a methodology that does not exist. Full reasoning, including how licences are handled and what gets excluded, is in [METHODOLOGY.md](METHODOLOGY.md).

**This directory is not limited to software, and not limited to projects that mention venture capital.** A PDF parser does not need to know what a data room is. A crawler does not need to know what deal flow is. Where a project is not VC-native, the entry says so explicitly and explains the adaptation.

## What is not here

Closed-source products. Paid products with no meaningful open-source component. Abandoned repositories. Model wrappers with no engineering behind them. Prompt collections. SEO bait. Duplicate implementations. Anything whose licence does not permit the use you are about to make of it. Anything whose primary purpose is unethical or illegal. Security and OSINT tooling appears only where the legitimate research and defensive use case is clear.

## About local copies

This repository **links** to projects; it does not vendor them. No source code from any listed project is redistributed here, which is a deliberate decision rather than an omission — vendoring a few hundred independently maintained projects produces a large, stale, licence-entangled fork that helps nobody. See [docs/LOCAL_COPIES.md](docs/LOCAL_COPIES.md) for the reasoning and for `scripts/clone_repos.sh`, which will pull the projects you actually want onto your own machine.

## How often this is updated

Weekly. A scheduled workflow refreshes verified metadata, detects drift (archived, licence changes, dead links, notable star movement), and opens a pull request plus a review queue. Discovery is automated; **curation is not** — nothing is added, removed, or re-labelled without a human decision. Every change is recorded in [CHANGELOG.md](CHANGELOG.md).

To refresh it yourself:

```bash
pip install -r requirements.txt
python scripts/update.py           # refresh verified metadata from the GitHub API
python scripts/generate_index.py   # regenerate every derived page
python scripts/verify.py           # validate the lot
```

## Data

The whole directory is available as structured data — this repository is meant to be a source of truth, not just a page of links:

- [`metadata/repositories.json`](metadata/repositories.json)
- [`metadata/repositories.yaml`](metadata/repositories.yaml)
- [`metadata/schema.json`](metadata/schema.json) — field definitions

Build a search UI, a filter, a bot, or a recommendation engine off it. If you do, tell us and we will link it.

## Contributing

Corrections are more valuable than submissions, and they get priority. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening anything — the metadata requirements are strict and submissions that skip them are closed without ceremony.

## Licence

The directory — its prose, structure, metadata, and scripts — is [CC0-1.0](LICENSE): public domain, use it however you like.

**Each listed project keeps its own licence.** Those are reported per entry, taken from the project itself, and never assumed. Nothing here is legal advice; if a licence will decide something that matters, read the upstream `LICENSE` and talk to your counsel.

## Sources & acknowledgements

Discovery draws on GitHub search and topics, prior awesome-lists, Hacker News, Product Hunt, academic work, and the projects' own documentation. Everything in [SOURCES.md](SOURCES.md) was a starting point — every entry was then verified against the project itself. Credit belongs to the maintainers of every project listed here; this repository only points at their work.
