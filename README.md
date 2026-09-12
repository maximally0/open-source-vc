<div align="center">

# Open Source VC

**What open-source software can a venture investor actually use — and what should you install first?**

Not another list of repositories. A map of the investment workflow, with an honest note about what each tool is for, what it costs you, and where nothing exists at all.

<!-- BEGIN GENERATED:stats -->
**236** projects across **19** categories &nbsp;·&nbsp; **14 built for venture** &nbsp;·&nbsp; 141 adaptable &nbsp;·&nbsp; 81 infrastructure<br>28 Essential &nbsp;·&nbsp; 152 Recommended &nbsp;·&nbsp; 40 Experimental &nbsp;·&nbsp; 16 Research
<!-- END GENERATED:stats -->

[**22 projects that give a solo VC an unfair advantage**](UNFAIR_ADVANTAGE.md) · [**The 32 to install**](STARTER_PACK.md) · [**Workflow map**](VC_WORKFLOW.md) · [**Where nothing exists**](GAPS.md) · [**Comparison matrix**](COMPARISON.md) · [**Methodology**](METHODOLOGY.md)

<!-- BEGIN GENERATED:updated -->
2026-09-12
<!-- END GENERATED:updated -->

</div>

---

## Read this in three passes

You do not want a list of repositories. You want to know what to install. So:

| Pass | What it is | Read |
|---|---|---|
| **1. The unfair advantage** | 22 projects that replace a licence, unlock expensive data, or automate a week of work. Almost none of them are famous. | [**UNFAIR_ADVANTAGE.md**](UNFAIR_ADVANTAGE.md) |
| **2. The install list** | 32 projects in the order a deal moves through a fund, for someone on week one. | [**STARTER_PACK.md**](STARTER_PACK.md) |
| **3. Everything else** | The full directory, by workflow stage and by category, with the reasoning on every entry. | [below](#the-workflow) |

And one page to read before you build anything: [**GAPS.md**](GAPS.md) documents twelve sub-tasks of venture work where **no usable open-source tool exists**. Knowing where the map is blank is worth as much as the map.

## The genuinely venture-native tools

**Only a small fraction of what is listed here was built for venture capital.** The exact split is in the line at the top of this page, and it is the number worth knowing: everything else is a general tool a fund adapts, or a building block a fund assembles.

That ratio is the finding. Venture-specific software is a commercial category, and almost none of it is open source.

<!-- BEGIN GENERATED:vcnative -->
| Project | What it is | Category | Stars |
|---|---|---|---:|
| [Captable](https://github.com/captableinc/captable) | An open-source cap table management platform. | Cap Tables & Equity | 822 |
| [Open Cap Format](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF) | An open data standard for cap tables. | Standards & Schemas | 188 |
| [YC Open API](https://github.com/yc-oss/api) | Y Combinator's own company and founder data, as an API. | Company Discovery & Deal Sourcing | 231 |
| [Cap Table Worksheet](https://github.com/1984vc/cap-table) | A spreadsheet-native cap table that computes the maths properly. | Cap Tables & Equity | 139 |
| [ExploreYC](https://github.com/KonstantinMB/exploreyc) | Browse the YC portfolio as a searchable, filterable site. | Company Discovery & Deal Sourcing | 44 |
| [Cap Table and Exit Waterfall](https://github.com/tdavidson/cap-table-tool) | Cap table plus exit waterfall modelling. | Cap Tables & Equity | 47 |
| [Due Diligence Agents](https://github.com/zoharbabin/due-diligence-agents) | Agents that flag risks across legal and finance and link them. | Due Diligence | 103 |
| [ExecSum Deal Brief](https://github.com/kklounge/execsum-deal-brief) | A daily deal-flow brief with a ranked top three. | Deal Sourcing & Pipeline | 50 |
| [Memo Generator](https://github.com/dforwardfeed/memo_generator) | Generates a startup investment memorandum. | Investment Memo & IC | 95 |
| [MiraclePlus Gallery](https://github.com/Nimbus318/miracle-plus-gallery) | Five years of MiraclePlus (formerly YC China) demo-day companies. | Company Discovery & Deal Sourcing | 25 |
| [OpenBook](https://github.com/iloveitaly/openbook) | An open investor and venture database. | Company Discovery & Deal Sourcing | 64 |
| [Runway Tool](https://github.com/tdavidson/runway-tool) | Runway and cash-budget forecasting for a startup. | Portfolio Management | 16 |
| [subsignal](https://github.com/0xnyn/subsignal) | Deal-flow monitoring built for funds. | Deal Sourcing & Pipeline | 29 |
| [VC Reporting](https://github.com/tdavidson/reporting) | An AI-native platform for fund reporting and analysis. | Investment Memo & IC | 52 |
<!-- END GENERATED:vcnative -->

Everything else is labelled on its entry as **VC-adaptable** (a general tool with a direct venture application) or **Infrastructure** (a building block). Those labels are independent of quality — a document parser can be the best tool here for a data room and still have no idea what a data room is.

## The workflow

Tools are organised by where they sit in the investment process, because that is how people look for them. Nobody wakes up wanting a vector database.

<!-- BEGIN GENERATED:stages -->
| Stage | Subcategories | Projects |
|---|---|---:|
| **[Source](stages/01-source.md)** | [Founder & Talent Discovery](categories/founder-discovery.md), [Company Discovery & Deal Sourcing](categories/company-discovery.md), [Deal Sourcing & Pipeline](categories/deal-sourcing.md) | 25 |
| **[Research](stages/02-research.md)** | [Market & Industry Research](categories/market-research.md), [Web Intelligence & OSINT](categories/osint.md) | 33 |
| **[Diligence](stages/03-diligence.md)** | [Due Diligence](categories/due-diligence.md), [Data Rooms & Document Intelligence](categories/document-intelligence.md), [Cap Tables & Equity](categories/cap-tables.md) | 37 |
| **[Underwrite](stages/04-underwrite.md)** | [Investment Analysis](categories/investment-analysis.md) | 14 |
| **[IC & Memo](stages/05-ic.md)** | [Investment Memo & IC](categories/investment-memos.md), [Knowledge Management](categories/knowledge-management.md) | 31 |
| **[Close](stages/06-close.md)** | [Legal & Transaction Infrastructure](categories/legal.md) | 17 |
| **[Portfolio](stages/07-portfolio.md)** | [Portfolio Management](categories/portfolio-management.md) | 10 |
| **[Relationships](stages/08-relationships.md)** | [Relationship Intelligence](categories/relationship-intelligence.md) | 13 |
| **[Fund](stages/09-fund.md)** | [LP & Fund Management](categories/lp-management.md), [Standards & Schemas](categories/standards.md) | 21 |
<!-- END GENERATED:stages -->

Each stage page carries its subcategories, its shortlist, and the shape of how the pieces fit together.

## The Essential list

`⭐ Essential` means one specific thing: **an analyst installs this in week one and it unblocks real work.** Quality, not popularity. Ranked with the venture-native tools first, which is why the top of this table looks nothing like a GitHub trending page.

<!-- BEGIN GENERATED:essentials -->
| Project | Relevance | Category | Stars | License | Why |
|---|---|---|---:|---|---|
| [Captable](https://github.com/captableinc/captable) | VC-native | Cap Tables & Equity | 822 | AGPL-3.0 | The cap table, dilution modelling, and stakeholder records that every fund currently pays a vendor for. |
| [YC Open API](https://github.com/yc-oss/api) | VC-native | Company Discovery & Deal Sourcing | 231 | unknown | Every YC company with its batch, industry, team size, status, and founders, plus a website field. |
| [Open Cap Format](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF) | VC-native | Standards & Schemas | 188 | unverified (Other) | Cap tables currently move between founders, lawyers, and investors as spreadsheets in whatever shape the last person used. |
| [Sherlock](https://github.com/sherlock-project/sherlock) | VC-adaptable | Founder & Talent Discovery | 91.4k | MIT | When a founder's name is common or their LinkedIn is thin, an analyst runs the handle they use elsewhere through Sherlock to see where else that handle exists. |
| [OpenBB](https://github.com/OpenBB-finance/OpenBB) | VC-adaptable | Investment Analysis | 72.9k | unverified (Other) | Public comparables work: pull financials, prices, and fundamentals for the listed companies a target competes with, then build the trading multiples that anchor a valuation conversation. |
| [NocoDB](https://github.com/nocodb/nocodb) | VC-adaptable | Deal Sourcing & Pipeline | 64.9k | unverified (Other) | The deals pipeline most small funds actually need: stages, owners, next actions, and notes, as a grid anyone on the team can edit, sitting on a real database you control. |
| [Twenty](https://github.com/twentyhq/twenty) | VC-adaptable | Relationship Intelligence | 56.6k | unverified (Other) | The team version: contacts, companies, and opportunities that match how a fund works, in a shared system rather than four analysts' personal notes. |
| [Metabase](https://github.com/metabase/metabase) | VC-adaptable | Portfolio Management | 49.2k | unverified (Other) | Portfolio dashboards a partner will actually open: capital deployed by vintage, sector exposure, KPI collection across the book, and which companies are behind plan. |
| [Cal.com](https://github.com/calcom/cal.diy) | VC-adaptable | Relationship Intelligence | 48.4k | MIT | Founder calls, LP check-ins, and office hours all live or die on scheduling. |
| [Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | VC-adaptable | Data Rooms & Document Intelligence | 45k | GPL-3.0 | The document archive for a fund or a family office: every contract, statement, and filing OCR'd, tagged, and full-text searchable, with the original file retained. |
| [Khoj](https://github.com/khoj-ai/khoj) | VC-adaptable | Market & Industry Research | 37.3k | AGPL-3.0 | A fund's institutional memory problem: a hundred memos, data-room exports, and meeting notes that nobody can search. |
| [Web-Check](https://github.com/lissy93/web-check) | VC-adaptable | Founder & Talent Discovery | 34.8k | MIT | Point it at a target company's domain and get its hosting, DNS and mail records, TLS configuration, exposed headers, and third-party services. |
| [changedetection.io](https://github.com/dgtlmoon/changedetection.io) | VC-adaptable | Deal Sourcing & Pipeline | 33.8k | Apache-2.0 | The narrow version of monitoring and the one analysts actually need: a competitor drops a price, adds a plan, edits a terms page, or a portfolio company quietly reshuffles its team page. |
| [STORM](https://github.com/stanford-oval/storm) | VC-adaptable | Market & Industry Research | 31.3k | MIT | Ask it to produce a briefing on a sector and it researches, outlines, and drafts with references. |
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher) | VC-adaptable | Market & Industry Research | 29.4k | Apache-2.0 | Hand it a market question, such as how many companies are selling continuous compliance tooling into European banks and who funded them, and it returns a written answer with the sources it used. |
| [Monica](https://github.com/monicahq/monica) | VC-adaptable | Relationship Intelligence | 25.3k | AGPL-3.0 | Every investor keeps the same private list: who introduced whom, what they care about, when you last spoke, what you promised. |
| [yfinance](https://github.com/ranaroussi/yfinance) | VC-adaptable | Investment Analysis | 25.2k | Apache-2.0 | The fastest way to get prices, financials, and history for a comparable set. |
| [SingleFile](https://github.com/gildas-lormeau/SingleFile) | VC-adaptable | Web Intelligence & OSINT | 22.4k | AGPL-3.0 | Evidence capture. |
| [PaperQA](https://github.com/Future-House/paper-qa) | VC-adaptable | Due Diligence | 9.2k | Apache-2.0 | Technical diligence on a deep-tech company: read the founders' papers and patents, then ask whether the claimed result holds up, with page-level citations. |
| [Mike](https://github.com/open-legal-products/mike) | VC-adaptable | Legal & Transaction Infrastructure | 4.2k | AGPL-3.0 | Contract review is the most expensive line item in a deal that nobody talks about. |
| [edgartools](https://github.com/dgunning/edgartools) | VC-adaptable | Investment Analysis | 2.7k | MIT | Public filings are the best free source on a listed company's real economics, and they are hostile to read. |
| [CourtListener](https://github.com/freelawproject/courtlistener) | VC-adaptable | Legal & Transaction Infrastructure | 1k | unverified (Other) | Litigation is a diligence question almost nobody checks properly: is the target or its founders party to a lawsuit, has a competitor sued them, is there an IP dispute waiting. |
| [Arelle](https://github.com/Arelle/Arelle) | VC-adaptable | Standards & Schemas | 236 | unverified (Other) | XBRL is how financial statements arrive from public companies and increasingly from private reporting. |
| [Docling](https://github.com/docling-project/docling) | Infrastructure | Data Rooms & Document Intelligence | 66.3k | MIT | Financial statements and contracts are where layout carries meaning: which number sits in which column, which heading a clause falls under. |
| [Streamlit](https://github.com/streamlit/streamlit) | Infrastructure | Portfolio Management | 45.7k | Apache-2.0 | The internal tool a fund builds once and uses daily: a company scorecard, an LP-return calculator, a portfolio KPI collector, a sourcing triage form. |
| [Marker](https://github.com/datalab-to/marker) | Infrastructure | Data Rooms & Document Intelligence | 39.7k | Apache-2.0 | The workhorse for converting a data room into text an analyst or a model can read. |
| [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | Infrastructure | Data Rooms & Document Intelligence | 34.7k | MPL-2.0 | The unglamorous step that makes everything else possible. |
| [Unstructured](https://github.com/Unstructured-IO/unstructured) | Infrastructure | Data Rooms & Document Intelligence | 15.4k | Apache-2.0 | A data room is a pile of PDFs, slide decks, spreadsheets, and scans in no particular order. |
<!-- END GENERATED:essentials -->

Ranked by purpose, not by stars. The most useful project in this entire directory has 231 stars.

## Full category index

<!-- BEGIN GENERATED:categories -->
| Category | Projects | What it covers |
|---|---:|---|
| [Knowledge Management](categories/knowledge-management.md) | 25 | Knowledge graphs |
| [Data Rooms & Document Intelligence](categories/document-intelligence.md) | 24 | PDF parsing |
| [Web Intelligence & OSINT](categories/osint.md) | 17 | OSINT frameworks |
| [Legal & Transaction Infrastructure](categories/legal.md) | 17 | SAFEs |
| [Market & Industry Research](categories/market-research.md) | 16 | Market mapping |
| [Investment Analysis](categories/investment-analysis.md) | 14 | Startup and investment scoring |
| [AI Agents for VC](categories/ai-agents.md) | 14 | Research agents |
| [Standards & Schemas](categories/standards.md) | 14 | Cap-table standards |
| [Relationship Intelligence](categories/relationship-intelligence.md) | 13 | CRMs |
| [Workflow & Automation](categories/automation.md) | 12 | Workflow automation |
| [Company Discovery & Deal Sourcing](categories/company-discovery.md) | 11 | Startup and company databases |
| [Due Diligence](categories/due-diligence.md) | 10 | Financial |
| [Portfolio Management](categories/portfolio-management.md) | 10 | Portfolio monitoring |
| [Datasets & Open Data](categories/datasets.md) | 9 | Startup and company datasets |
| [Founder & Talent Discovery](categories/founder-discovery.md) | 8 | Founder discovery |
| [LP & Fund Management](categories/lp-management.md) | 7 | LP CRM and intelligence |
| [Deal Sourcing & Pipeline](categories/deal-sourcing.md) | 6 | Sourcing workflow |
| [Investment Memo & IC](categories/investment-memos.md) | 6 | Memo generation |
| [Cap Tables & Equity](categories/cap-tables.md) | 3 | Cap table modelling |
<!-- END GENERATED:categories -->

---

## How projects are selected

The bar is high and most things fail it. Every entry was opened upstream — README, `LICENSE`, structure, commit history, releases, issues — and every metadata field comes from the GitHub API rather than a search snippet or a list.

Four quality labels and three relevance labels, deliberately on separate axes:

| | Quality | Meaning |
|---|---|---|
| ⭐ | **Essential** | Install in week one. Unblocks a core task. |
| 🔥 | **Recommended** | Strong fit, narrower, or better once you have a stack. |
| 🧪 | **Experimental** | Early, incomplete, possibly important. Eyes open. |
| 📚 | **Research** | Read it rather than deploy it. |

| | Relevance | Meaning |
|---|---|---|
| ◆ | **VC-native** | Built for venture, private markets, or fund operations. |
| ◇ | **VC-adaptable** | A general tool with a direct venture application. |
| ▫ | **Infrastructure** | A building block you assemble venture tooling with. |

There are no numeric scores. An `84/100` implies a methodology that does not exist, and this directory would rather state its reasoning than invent a number. Full detail, including the licence policy and the known blind spots, is in [METHODOLOGY.md](METHODOLOGY.md).

**This directory deliberately includes projects that have never heard of venture capital.** A PDF parser does not need to know what a data room is. What matters is that the entry says which kind of tool it is and exactly how a fund would use it — which is what the relevance axis is for.

## What is not here

Closed-source products. Paid products whose open-source component is marketing. Abandoned repositories. Model wrappers with no engineering. Prompt collections. SEO bait. Duplicate implementations. Anything whose licence does not permit the use you are about to make of it, or whose purpose is unethical or illegal.

And, deliberately, no filler to make thin categories look full. Where open source has nothing, [GAPS.md](GAPS.md) says so.

## About local copies

This repository **links** to projects; it does not vendor them. No third-party source code is redistributed here, which is a decision rather than an omission — vendoring two hundred independently maintained projects produces a large, stale, licence-entangled fork that helps nobody. See [docs/LOCAL_COPIES.md](docs/LOCAL_COPIES.md) for the reasoning, and `scripts/clone_repos.sh` to pull the ones you want onto your own machine.

## How often this is updated

Weekly. A scheduled workflow refreshes verified metadata, separates real drift from routine movement (an archived project or a licence change escalates; star counts do not), and either commits a routine refresh or opens a pull request for review. **It never edits the curated list.** Discovery is automated; curation is not, and that boundary is enforced in code.

```bash
pip install -r requirements.txt
python scripts/update.py           # refresh verified metadata from the GitHub API
python scripts/generate_index.py   # regenerate every derived page
python scripts/verify.py           # validate the lot
```

## Data

The whole directory is structured data, meant to be a source of truth rather than a page of links:

- [`metadata/repositories.json`](metadata/repositories.json)
- [`metadata/repositories.yaml`](metadata/repositories.yaml)
- [`metadata/schema.json`](metadata/schema.json)

Every field carries either a machine-verified value or a stated editorial judgement. Build a search UI, a filter, a bot, or a recommendation engine on it — and tell us if you do, so we can link it.

## Contributing

Corrections are more valuable than submissions and they get priority. The most useful thing you can send is a repository for something listed in [GAPS.md](GAPS.md). Read [CONTRIBUTING.md](CONTRIBUTING.md) first — the metadata requirements are strict.

## Licence

The directory — its prose, structure, metadata, and scripts — is [CC0-1.0](LICENSE): public domain.

**Each listed project keeps its own licence**, reported per entry and never assumed. Nothing here is legal advice. If a licence decision matters, read the upstream `LICENSE` and talk to your counsel.

## Sources

Discovery drew on GitHub search and topics, prior lists, Hacker News, communities, papers, and the projects' own documentation. Everything in [SOURCES.md](SOURCES.md) was a lead, and every entry was verified against the project itself. Credit belongs to the maintainers of every project listed; this repository only points at their work.
