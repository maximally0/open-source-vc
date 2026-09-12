# Changelog

Every update to the directory, newest first. Generated metadata is refreshed weekly; entries are added, removed, and re-classified by hand.

Format: added, removed, updated, and what turned up during the pass that was worth recording.

---

## 2026-09-12 — v1.1.0: Restructured around the investment workflow

A review of v1.0.0 landed one criticism that could not be argued with: it was **a collection of tools that could be useful to a VC, rather than a map of what a VC should use at each step**. Three specific problems, all confirmed by measuring the released data rather than by opinion.

### The problems, measured

| Finding | Evidence |
|---|---|
| Popularity was driving the top tier | Essential median was **35,952 stars**; only 4 of 39 Essentials had under 1,000 |
| The VC-specific layer was almost invisible | `vc_native` was true for **12 of 226** (5%), and all 12 sat between 25 and 822 stars |
| The tier scale conflated quality with kind | The `infrastructure` tier held **odoo/odoo** (an ERP) and a GraphQL engine, with 0 of 20 entries under 1,000 stars |

The third is the root cause of the first two. "Infrastructure" is not a quality level, so using it as one meant the scale was answering two different questions at once — and the answer it gave was whichever project had the most stars.

### Changed

**Split the axes.** `tier` is now quality only: Essential, Recommended, Experimental, Research. A new `vc_relevance` field answers the separate question — `native` (built for venture, private markets, or fund operations), `adaptable` (a general tool with a direct venture application), or `infrastructure` (a building block you assemble tooling with). The retired `infrastructure` tier was remapped to Recommended across 20 entries.

Current shape: **14 native, 141 adaptable, 81 infrastructure.**

**Rebuilt the navigation around nine workflow stages.** Source, Research, Diligence, Underwrite, IC & Memo, Close, Portfolio, Relationships, Fund. The 19 category pages remain as the granular level; [VC_WORKFLOW.md](VC_WORKFLOW.md) is now the stage index and each stage has its own page with its subcategories, its shortlist, and how the pieces fit together.

**Rebalanced the Essential tier.** 12 entries demoted to Recommended, including n8n (204k stars), Whisper (108k), browser-use (114k), Airflow, dbt, LangGraph, Qdrant, and Playwright. Not because they are weak — they are excellent — but because none of them is what an analyst installs in week one. Essential is now 28 entries, sorted with the venture-native tools first, and the README says explicitly that the ranking is by purpose, not by stars.

**Added [UNFAIR_ADVANTAGE.md](UNFAIR_ADVANTAGE.md).** 22 projects that replace a licence, unlock expensive data, or automate a week of work, selected by hand against three stated tests and explicitly not by star count. The most useful entry has 231 stars; the second has 29.

**Reframed the README.** It now opens with "what should you install first" and a three-pass reading order, rather than a count of repositories. Comprehensiveness moved below usefulness.

**Added 13 entries** closing gaps found by testing the directory against the sub-tasks of venture work rather than against its own categories:

- [CourtListener](categories/legal.md) (1,012★) and [Juriscraper](categories/legal.md) — litigation and court records, previously nothing at all
- [OSS Insight](categories/company-discovery.md) (2,505★) and [Star History](categories/company-discovery.md) (9,483★) — GitHub traction as a diligence input
- [Meetily](categories/relationship-intelligence.md) (30,673★) — self-hosted meeting intelligence, which v1.0.0 lacked entirely
- [Google Patents Public Data](categories/datasets.md) and the [Harvard USPTO dataset](categories/datasets.md) — patent analysis beyond a single API client
- [Fire Enrich](categories/company-discovery.md) — company enrichment from an email or domain
- [Runway Tool](categories/portfolio-management.md) — runway and burn forecasting
- [OpenRegistry](categories/company-discovery.md) — entity and registry checking
- [Due Diligence Agents](categories/due-diligence.md), [Rizzo PII](categories/due-diligence.md), [CorpusCustody](categories/due-diligence.md) were already present; the AI-diligence cluster is now cross-referenced from the stage page

**Added [GAPS.md](GAPS.md).** The sub-tasks of venture work where **no usable open-source tool exists**, with the search performed and the result recorded: incorporation and entity analysis, funding round data, investor databases, cohort analysis, unit economics, investment scoring frameworks, private comparables, portfolio benchmarking, fund accounting and waterfalls, cap-table tooling, product launch tracking, and warm-introduction graphs. Twelve gaps, each with the reason it is empty. This is the most useful page the review produced, because it turns "you are missing X" into a documented finding.

### Fixed

- **`--repos-only` dropped the rest of the directory.** A partial metadata refresh wrote a snapshot containing only the repositories it fetched, silently removing every other entry from the metadata. Found while adding the 13 new entries.
- **A curated name could diverge from the snapshot without blocking.** `calcom/cal.com` was renamed upstream to `calcom/cal.diy`; the published entry was correct, but nothing caught it. A curated name absent from the snapshot is now a build error rather than a warning.
- **Archived repositories had no documented exception path.** `google/patents-public-data` is archived upstream while the BigQuery dataset it documents remains live. Entries can now set `archived_ok` with a stated reason, which downgrades the check to a warning so the fact stays visible instead of being either hidden or fatal.

### Added to the automation

- `vc_relevance` is validated in CI, and using the same value for both tier and relevance is an error — the specific mistake this release exists to correct.
- `vc_native` is now derived from `vc_relevance` rather than hand-set, so the two cannot drift apart.
- Six new required README regions, including the stage table and the venture-native list.

### Notes

- Median stars in the Essential tier moved from 35,952 to 32,563. That is a smaller change than it sounds: the demotions removed the most egregious cases, and the remaining Essentials are popular **because they are the best available tool for the task** — a different claim from "stars made them Essential." The tiny, purpose-built tools are now surfaced in [UNFAIR_ADVANTAGE.md](UNFAIR_ADVANTAGE.md) where stars are explicitly not the criterion.
- The 8-dimension numeric scoring proposed in review was not implemented. Each dimension is a fair question and they are now reflected in the stated inclusion tests and in the `vc_relevance` label, but publishing 236 × 8 scores would produce a precision the judgements do not support. [METHODOLOGY.md](METHODOLOGY.md#why-no-84100) explains why.

---

## 2026-09-12 — v1.0.0: Initial release

The first published version. **226 projects** across **19 categories**, every one inspected upstream and every metadata field read from the GitHub API rather than copied from a list.

### Added

The whole directory. Highlights by category:

- **Founder & talent discovery (8)** — Sherlock, Maigret, Web-Check, JobSpy, the OSINT Framework, theHarvester, linkedin_scraper, Instaloader
- **Company discovery (7)** — the YC Open API, ExploreYC, company-research-agent, dedupe, idea-reality-mcp, OpenBook, MiraclePlus Gallery
- **Deal sourcing (6)** — subsignal, ExecSum Deal Brief, NocoDB, Huginn, changedetection.io, Dub
- **Market research (16)** — GPT Researcher, STORM, Khoj, Tongyi DeepResearch, deep-research, DocsGPT, TrendRadar, SurfSense, MiroThinker, WebThinker, DeepResearch Bench, Deep Searcher, DeepResearchAgent, Hyperresearch, World Intel MCP, Situation Monitor
- **Web intelligence & OSINT (17)** — Scrapy, Crawlee, Firecrawl, Playwright, SingleFile, SpiderFoot, BBOT, OpenCTI, Flowsint, reNgine, Osmedeus, IVRE, dnstwist, subfinder, httpx, Photon, Puppeteer
- **Relationship intelligence (12)** — Monica, Twenty, Frappe CRM, EspoCRM, Krayin, Odoo, Cal.com, NetworkX, Whisper, WhisperX, faster-whisper, CiviCRM
- **Due diligence (10)** — PaperQA, due-diligence-agents, CorpusCustody, Cleanlab, Phoenix, LangWatch, shhgit, Rizzo PII, Label Studio, doccano
- **Data rooms & document intelligence (24)** — Unstructured, Docling, MinerU, Marker, Surya, PaddleOCR, Tesseract, OCRmyPDF, Camelot, pdfplumber, PyMuPDF, Tika, Stirling PDF, Paperless-ngx, DocuSeal, Documenso, EasyOCR, Unstract, MarkItDown, PageIndex, Kotaemon, Pandoc, Zerox, Chandra
- **Investment analysis (14)** — OpenBB, Finance Toolkit, Qlib, yfinance, QuantStats, QuantLib, FinancePy, Dexter, AKShare, edgartools, SEC EDGAR Downloader, AutoHedge, Financial Datasets MCP, Prediction Market Analysis
- **Cap tables (3)** — Captable, the 1984.vc worksheet, Cap Table and Exit Waterfall
- **Investment memo & IC (6)** — VC Reporting, Memo Generator, TickerToThesis, Typst, Quarto, Buffett Investment Research
- **Portfolio management (9)** — Metabase, Superset, Redash, Streamlit, Baserow, Datasette, Directus, ROAPI, Gradio
- **LP & fund management (7)** — Beancount, hledger, Ledger, GnuCash, Grist, PyPortfolioOpt, ERPNext
- **Legal (15)** — Mike, OpenContracts, Python-Redlines, LexNLP, Blackstone, LexGLUE, Open US Law, OpenNyAI, Claude Legal Skill, doc-haus, DocuChat, OpenSpecter, Awesome Legal NLP, LeSICiN, Open Australian Legal Corpus
- **Knowledge management (25)** — RAGFlow, GraphRAG, LightRAG, Milvus, Qdrant, pgvector, Weaviate, Chroma, Neo4j, Graphiti, Cognee, Haystack, Onyx, RAG Techniques, txtai, Mem0, Outline, Wiki.js, Docmost, Logseq, Zotero, SurrealDB, Dgraph, Jupyter Book, Marimo
- **AI agents (14)** — browser-use, LangGraph, MCP Servers, Awesome MCP Servers, AutoGen, CrewAI, OpenAI Agents SDK, OpenHands, Dify, DSPy, LlamaIndex, LangChain, AutoGPT, Heuristic Agent Framework
- **Workflow & automation (12)** — n8n, Activepieces, Windmill, Kestra, Airflow, Dagster, Prefect, Airbyte, Meltano, dbt, Appsmith, ToolJet
- **Standards & schemas (14)** — Open Cap Format, Arelle, python-xbrl, py-xbrl, ixbrl-parse, edinet-tools, Xule, Brel, xbrl-parser, iXBRL Viewer, pystock-crawler, EFRAG Digital Template Converter, iXBRL Reporter, OpenCLI
- **Datasets (7)** — Awesome Public Datasets, Hugging Face Datasets, PatentsView, OpenAlex, TensorFlow Datasets, Open Graph Benchmark, Loghub

Also shipped:

- [STARTER_PACK.md](STARTER_PACK.md) — 32 projects ordered the way a deal moves through a fund
- [HIDDEN_GEMS.md](HIDDEN_GEMS.md) — 38 projects selected without reference to star count
- [COMPARISON.md](COMPARISON.md) — every project as one row, with derived columns
- [VC_WORKFLOW.md](VC_WORKFLOW.md) — 18 process stages mapped to tools
- [METHODOLOGY.md](METHODOLOGY.md), [CONTRIBUTING.md](CONTRIBUTING.md), [ROADMAP.md](ROADMAP.md), [SOURCES.md](SOURCES.md)
- Five guides: [analyst](guides/analyst-stack.md), [sourcing](guides/sourcing-stack.md), [diligence](guides/diligence-stack.md), [research](guides/research-stack.md), and [build-your-own-vc-stack](guides/build-your-own-vc-stack.md)
- Verification pipeline: `discover.py` (search), `seed_repos.py` (targeted verification), `shortlist.py` (filtering), `update.py` (drift detection), `generate_index.py` (build), `verify.py` (CI validation)
- Weekly GitHub Action that refreshes metadata and opens a pull request with a review queue, never touching the curated list
- Structured export at `metadata/repositories.json` and `.yaml`, with a schema

### Notes from the research pass

Recorded because the process matters as much as the result, and because these are the things a reader cannot see in the final list:

**The search was broader than the vocabulary.** Searching only for venture-capital terms returns a thin set, largely abandoned. Most of what an analyst actually uses has no idea venture capital exists: PDF parsers, entity resolution, change detection, vector stores. The productive queries were the adjacent ones.

**A targeted seed pass caught real errors.** Broad search found generic infrastructure well and VC-native tooling badly, so 168 specific repositories were verified directly through the API. That pass caught two repositories that do not exist (`seriesseed/seriesseed`, `gleif/lei`), one archived project (`commoncrawl/commoncrawl`), one renamed organisation (`JSv4/OpenContracts` → `Open-Source-Legal/OpenContracts`), and one archived workflow tool (`FlowiseAI/Flowise`). Every one of those would have been a wrong entry if the list had been written from memory.

**Cap tables and LP management are the gaps.** Both are commercially well-served and barely served by open source at all. That finding is documented on the category pages rather than padded over, because knowing where open source stops is as useful as knowing where it starts.

**Licence reporting found 48 projects with no standard licence.** Forty with a non-standard licence and eight with none at all. They are listed with that fact stated and flagged as not safe to redistribute, which is exactly what the licence policy requires.

**Star counts were treated as a fact, not a quality signal.** Several of the highest-starred repositories surfaced by search were excluded: apparent SEO projects, prompt collections, and abandoned tutorials. Several of the most useful entries have fewer than a thousand stars.

**Ten projects had no licence file.** Worth stating plainly since the directory links them: `laramies/theHarvester`, `joeyism/linkedin_scraper`, `0xnyn/subsignal`, `hipcityreg/situation-monitor`, `virattt/dexter`, `jasonfdg/TickerToThesis`, `tdavidson/cap-table-tool`, `coastalcph/lex-glue`, `Law-AI/LeSICiN`, `yc-oss/api`. Included because the tool is useful and the licence gap is disclosed in the entry; check terms before building on any of them.

**Sixteen entries are dormant.** Flagged automatically by the weekly validator and visible in `metadata/repositories.json` via the `status` field. Two of them, `captableinc/captable` and `tdavidson/cap-table-tool`, are the entire cap-table category, which is why the coverage note exists rather than a quiet removal.

---

## Upcoming

See [ROADMAP.md](ROADMAP.md). The next priorities are the coverage gaps that public search cannot reach, and replacing `unknown` contributor counts for Essential-tier entries.

<!--
Template for the next entry:

## YYYY-MM-DD

### Added
- name — what it is, one line

### Removed
- name — why

### Updated
- name — licence changed, archived, dormant, major release

### Interesting discoveries
- What turned up during the pass and is not in the list yet.
-->
