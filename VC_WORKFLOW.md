# The VC Workflow, Mapped to Open Source

Venture is a pipeline with a dozen stages, and most funds buy a different SaaS product for each one. This page maps the whole process and shows what open source covers at every step — including the stages nobody sells software for.

```text
Sourcing → Founder research → Company research → Market research
   → Screening → Meeting → Due diligence → Financial analysis
   → Legal DD → Memo → IC → Investment → Portfolio monitoring
   → Follow-on → Exit → (and back to Sourcing)
```

_2026-09-12 · 226 projects mapped_

---

## Sourcing

_Surface companies before they are on anyone's list._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [YC Open API](https://github.com/yc-oss/api) | Essential | 231 | unknown | Every YC company with its batch, industry, team size, status, and founders, plus a website field. |
| [dedupe](https://github.com/dedupeio/dedupe) | Interesting | 4.5k | MIT | Two funds merge sourcing lists, or a CRM export meets a scraped dataset, and someone has to decide which rows describe the same company before anything can be counted. |
| [Company Research Agent](https://github.com/guy-hartstein/company-research-agent) | Interesting | 2.3k | Apache-2.0 | Feed it a company name and get back a summary of what the company does, its market, competitors, and recent news, with sources. |
| [ExploreYC](https://github.com/KonstantinMB/exploreyc) | Interesting | 44 | MIT | A fast way to walk the YC universe by batch, industry, and hiring status when you want to see a sector rather than query an API. |
| [Idea Reality](https://github.com/mnemox-ai/idea-reality-mcp) | Experimental | 815 | MIT | Before a first call with a startup claiming a new category, run the premise through this to see what already exists on GitHub, Hacker News, npm, PyPI, and Product Hunt. |
| [OpenBook](https://github.com/iloveitaly/openbook) | Experimental | 64 | MIT | A community attempt at the investor-and-fund graph that normally sits behind a PitchBook licence: who invests at which stage, in which sectors, and alongside whom. |

Full category pages: [Company Discovery & Deal Sourcing](categories/company-discovery.md), [Deal Sourcing & Pipeline](categories/deal-sourcing.md), [Founder & Talent Discovery](categories/founder-discovery.md)

---

## Founder research

_Who is this person, what have they built, can I reach them._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [Sherlock](https://github.com/sherlock-project/sherlock) | Essential | 91.4k | MIT | When a founder's name is common or their LinkedIn is thin, an analyst runs the handle they use elsewhere through Sherlock to see where else that handle exists. |
| [Web-Check](https://github.com/lissy93/web-check) | Essential | 34.8k | MIT | Point it at a target company's domain and get its hosting, DNS and mail records, TLS configuration, exposed headers, and third-party services. |
| [Maigret](https://github.com/soxoj/maigret) | Interesting | 37.5k | MIT | Produces a report across 3,000+ sites from a single handle, including account metadata and extracted profile fields where the site exposes them. |
| [theHarvester](https://github.com/laramies/theHarvester) | Interesting | 17.4k | unknown | A first pass on a company you have no relationship with: it collects public emails, hostnames, and employee names from search engines and certificate logs. |
| [OSINT Framework](https://github.com/lockfale/OSINT-Framework) | Interesting | 12.1k | MIT | When a background check feels incomplete, this is the checklist that tells you what other public sources exist for the thing you hold: a username, an email, a domain, a phone number. |
| [JobSpy](https://github.com/speedyapply/JobSpy) | Interesting | 4.3k | MIT | A fund watching a sector can track which startups are hiring, for which functions, and how fast, without buying a labour-market dataset. |

Full category pages: [Founder & Talent Discovery](categories/founder-discovery.md), [Web Intelligence & OSINT](categories/osint.md), [Relationship Intelligence](categories/relationship-intelligence.md)

---

## Company research

_What does the product actually do, and how is it built._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [YC Open API](https://github.com/yc-oss/api) | Essential | 231 | unknown | Every YC company with its batch, industry, team size, status, and founders, plus a website field. |
| [dedupe](https://github.com/dedupeio/dedupe) | Interesting | 4.5k | MIT | Two funds merge sourcing lists, or a CRM export meets a scraped dataset, and someone has to decide which rows describe the same company before anything can be counted. |
| [Company Research Agent](https://github.com/guy-hartstein/company-research-agent) | Interesting | 2.3k | Apache-2.0 | Feed it a company name and get back a summary of what the company does, its market, competitors, and recent news, with sources. |
| [ExploreYC](https://github.com/KonstantinMB/exploreyc) | Interesting | 44 | MIT | A fast way to walk the YC universe by batch, industry, and hiring status when you want to see a sector rather than query an API. |
| [Idea Reality](https://github.com/mnemox-ai/idea-reality-mcp) | Experimental | 815 | MIT | Before a first call with a startup claiming a new category, run the premise through this to see what already exists on GitHub, Hacker News, npm, PyPI, and Product Hunt. |
| [OpenBook](https://github.com/iloveitaly/openbook) | Experimental | 64 | MIT | A community attempt at the investor-and-fund graph that normally sits behind a PitchBook licence: who invests at which stage, in which sectors, and alongside whom. |

Full category pages: [Company Discovery & Deal Sourcing](categories/company-discovery.md), [Web Intelligence & OSINT](categories/osint.md), [Market & Industry Research](categories/market-research.md)

---

## Market research

_Size the market, map the competition, find the wedge._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [Khoj](https://github.com/khoj-ai/khoj) | Essential | 37.3k | AGPL-3.0 | A fund's institutional memory problem: a hundred memos, data-room exports, and meeting notes that nobody can search. |
| [STORM](https://github.com/stanford-oval/storm) | Essential | 31.3k | MIT | Ask it to produce a briefing on a sector and it researches, outlines, and drafts with references. |
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher) | Essential | 29.4k | Apache-2.0 | Hand it a market question, such as how many companies are selling continuous compliance tooling into European banks and who funded them, and it returns a written answer with the sources it used. |
| [TrendRadar](https://github.com/sansan0/TrendRadar) | Interesting | 62.2k | GPL-3.0 | Tracks what is rising across social platforms, news, and RSS and sends alerts on chosen keywords. |
| [Tongyi DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | Interesting | 19.9k | Apache-2.0 | For funds that cannot send research questions to a hosted API, this runs research loops against a self-hosted model. |
| [deep-research](https://github.com/dzhng/deep-research) | Interesting | 19.7k | MIT | The version to read if you want to build your own research agent: it searches, reads, generates follow-up questions, and recurses to a depth you set. |

Full category pages: [Market & Industry Research](categories/market-research.md), [Knowledge Management](categories/knowledge-management.md)

---

## Initial screening

_Decide whether this deserves a meeting._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [OpenBB](https://github.com/OpenBB-finance/OpenBB) | Essential | 72.9k | unverified (Other) | Public comparables work: pull financials, prices, and fundamentals for the listed companies a target competes with, then build the trading multiples that anchor a valuation conversation. |
| [yfinance](https://github.com/ranaroussi/yfinance) | Essential | 25.2k | Apache-2.0 | The fastest way to get prices, financials, and history for a comparable set. |
| [edgartools](https://github.com/dgunning/edgartools) | Essential | 2.7k | MIT | Public filings are the best free source on a listed company's real economics, and they are hostile to read. |
| [Qlib](https://github.com/microsoft/qlib) | Interesting | 48.5k | MIT | Relevant beyond trading: backtesting a systematic signal or a scoring model before trusting it. |
| [AKShare](https://github.com/akfamily/akshare) | Interesting | 22.5k | MIT | Anyone looking at Chinese public comparables, or at a Chinese target's domestic competitors, hits a wall with Western data providers. |
| [QuantStats](https://github.com/ranaroussi/quantstats) | Interesting | 7.6k | Apache-2.0 | For a fund reporting on performance, or an analyst assessing a strategy someone has pitched: returns, drawdown, volatility, and ratios with a generated report. |

Full category pages: [Investment Analysis](categories/investment-analysis.md), [Investment Memo & IC](categories/investment-memos.md), [Company Discovery & Deal Sourcing](categories/company-discovery.md)

---

## Meeting

_Notes, context, and the relationship record afterwards._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [Whisper](https://github.com/openai/whisper) | Essential | 108.9k | MIT | Turn founder calls into a transcript you can search, quote in a memo, and keep as part of the record. |
| [Twenty](https://github.com/twentyhq/twenty) | Essential | 56.6k | unverified (Other) | The team version: contacts, companies, and opportunities that match how a fund works, in a shared system rather than four analysts' personal notes. |
| [Cal.com](https://github.com/calcom/cal.diy) | Essential | 48.4k | MIT | Founder calls, LP check-ins, and office hours all live or die on scheduling. |
| [Monica](https://github.com/monicahq/monica) | Essential | 25.3k | AGPL-3.0 | Every investor keeps the same private list: who introduced whom, what they care about, when you last spoke, what you promised. |
| [NetworkX](https://github.com/networkx/networkx) | Essential | 17.3k | unverified (Other) | The warm-introduction question that every fund asks and almost none can answer systematically: which of our contacts is closest to this founder, and through whom. |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Interesting | 25.4k | MIT | What makes transcribing every call practical rather than aspirational. |

Full category pages: [Relationship Intelligence](categories/relationship-intelligence.md), [Knowledge Management](categories/knowledge-management.md)

---

## Due diligence

_Financial, commercial, technical, and legal workstreams._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [PaperQA](https://github.com/Future-House/paper-qa) | Essential | 9.2k | Apache-2.0 | Technical diligence on a deep-tech company: read the founders' papers and patents, then ask whether the claimed result holds up, with page-level citations. |
| [Label Studio](https://github.com/HumanSignal/label-studio) | Interesting | 28.3k | Apache-2.0 | Customer research and commercial diligence often mean reading a hundred support tickets, reviews, or contracts and coding them consistently. |
| [Cleanlab](https://github.com/cleanlab/cleanlab) | Interesting | 11.7k | Apache-2.0 | A target claims its model works because of proprietary data. |
| [Phoenix](https://github.com/Arize-ai/phoenix) | Interesting | 11.4k | unverified (Other) | Ask a target to show you traces of its model in production: what users asked, what the model answered, where it failed. |
| [doccano](https://github.com/doccano/doccano) | Interesting | 10.8k | MIT | When a diligence finding needs a number rather than an impression, such as how many of a target's contracts contain an unusual termination clause, someone has to read them all consistently. |
| [LangWatch](https://github.com/langwatch/langwatch) | Interesting | 3.5k | Apache-2.0 | The diligence question for any AI-native company is whether the product actually works when inputs vary. |

Full category pages: [Due Diligence](categories/due-diligence.md), [Data Rooms & Document Intelligence](categories/document-intelligence.md), [Legal & Transaction Infrastructure](categories/legal.md), [Web Intelligence & OSINT](categories/osint.md)

---

## Financial analysis

_Model the business, the round, and the outcomes._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [OpenBB](https://github.com/OpenBB-finance/OpenBB) | Essential | 72.9k | unverified (Other) | Public comparables work: pull financials, prices, and fundamentals for the listed companies a target competes with, then build the trading multiples that anchor a valuation conversation. |
| [yfinance](https://github.com/ranaroussi/yfinance) | Essential | 25.2k | Apache-2.0 | The fastest way to get prices, financials, and history for a comparable set. |
| [edgartools](https://github.com/dgunning/edgartools) | Essential | 2.7k | MIT | Public filings are the best free source on a listed company's real economics, and they are hostile to read. |
| [Qlib](https://github.com/microsoft/qlib) | Interesting | 48.5k | MIT | Relevant beyond trading: backtesting a systematic signal or a scoring model before trusting it. |
| [AKShare](https://github.com/akfamily/akshare) | Interesting | 22.5k | MIT | Anyone looking at Chinese public comparables, or at a Chinese target's domestic competitors, hits a wall with Western data providers. |
| [QuantStats](https://github.com/ranaroussi/quantstats) | Interesting | 7.6k | Apache-2.0 | For a fund reporting on performance, or an analyst assessing a strategy someone has pitched: returns, drawdown, volatility, and ratios with a generated report. |

Full category pages: [Investment Analysis](categories/investment-analysis.md), [Cap Tables & Equity](categories/cap-tables.md)

---

## Legal DD

_Contracts, cap table, corporate structure, encumbrances._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [Mike](https://github.com/open-legal-products/mike) | Essential | 4.2k | AGPL-3.0 | Contract review is the most expensive line item in a deal that nobody talks about. |
| [OpenContracts](https://github.com/Open-Source-Legal/OpenContracts) | Interesting | 1.5k | MIT | A fund that signs many similar agreements accumulates a corpus nobody can query. |
| [Claude Legal Skill](https://github.com/evolsb/claude-legal-skill) | Interesting | 438 | MIT | Reviews a contract against a stated risk framework and produces output a lawyer can work from. |
| [Python-Redlines](https://github.com/JSv4/Python-Redlines) | Interesting | 128 | MIT | The concrete deliverable in any negotiation is a redline. |
| [OpenNyAI](https://github.com/OpenNyAI/Opennyai) | Interesting | 101 | MIT | For anyone working in or investing into India, court judgments and legal documents in that jurisdiction were largely unprocessable by Western legal NLP. |
| [Open US Law](https://github.com/Vaquill-AI/open-us-law) | Interesting | 59 | Apache-2.0 | Millions of sections of state codes, the US Code, and regulations in a structured form. |

Full category pages: [Legal & Transaction Infrastructure](categories/legal.md), [Data Rooms & Document Intelligence](categories/document-intelligence.md), [Cap Tables & Equity](categories/cap-tables.md)

---

## Investment memo

_Turn evidence into a written recommendation._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [Typst](https://github.com/typst/typst) | Interesting | 56k | Apache-2.0 | The output quality question that nobody prices: a memo typeset properly reads as considered work, and a Word document with inconsistent spacing does not. |
| [Quarto](https://github.com/quarto-dev/quarto-cli) | Interesting | 6k | unverified (Other) | A diligence report where the numbers come from the data rather than being pasted in, so a corrected input updates every figure downstream. |
| [Memo Generator](https://github.com/dforwardfeed/memo_generator) | Experimental | 95 | MIT | Assembles a first-draft investment memo from inputs about a company. |
| [Buffett Investment Research](https://github.com/MichaelRochonnn/buffett-investment-research) | Experimental | 63 | MIT | A worked example of the discipline that separates real research from summarisation: go to the primary document, extract what matters, and structure a conclusion with the source attached. |
| [VC Reporting](https://github.com/tdavidson/reporting) | Experimental | 52 | Apache-2.0 | Covers the recurring paperwork a fund owes its LPs and itself: portfolio updates, performance reporting, and the analysis that goes with them. |
| [TickerToThesis](https://github.com/jasonfdg/TickerToThesis) | Experimental | 26 | unknown | Takes a ticker, gathers public research, and drafts a memo in the shape a buyside analyst would expect. |

Full category pages: [Investment Memo & IC](categories/investment-memos.md), [Knowledge Management](categories/knowledge-management.md)

---

## IC

_Score, debate, decide, and record why._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [Typst](https://github.com/typst/typst) | Interesting | 56k | Apache-2.0 | The output quality question that nobody prices: a memo typeset properly reads as considered work, and a Word document with inconsistent spacing does not. |
| [Quarto](https://github.com/quarto-dev/quarto-cli) | Interesting | 6k | unverified (Other) | A diligence report where the numbers come from the data rather than being pasted in, so a corrected input updates every figure downstream. |
| [Memo Generator](https://github.com/dforwardfeed/memo_generator) | Experimental | 95 | MIT | Assembles a first-draft investment memo from inputs about a company. |
| [Buffett Investment Research](https://github.com/MichaelRochonnn/buffett-investment-research) | Experimental | 63 | MIT | A worked example of the discipline that separates real research from summarisation: go to the primary document, extract what matters, and structure a conclusion with the source attached. |
| [VC Reporting](https://github.com/tdavidson/reporting) | Experimental | 52 | Apache-2.0 | Covers the recurring paperwork a fund owes its LPs and itself: portfolio updates, performance reporting, and the analysis that goes with them. |
| [TickerToThesis](https://github.com/jasonfdg/TickerToThesis) | Experimental | 26 | unknown | Takes a ticker, gathers public research, and drafts a memo in the shape a buyside analyst would expect. |

Full category pages: [Investment Memo & IC](categories/investment-memos.md), [Knowledge Management](categories/knowledge-management.md)

---

## Investment

_Documents, signatures, and the money moving._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [Mike](https://github.com/open-legal-products/mike) | Essential | 4.2k | AGPL-3.0 | Contract review is the most expensive line item in a deal that nobody talks about. |
| [OpenContracts](https://github.com/Open-Source-Legal/OpenContracts) | Interesting | 1.5k | MIT | A fund that signs many similar agreements accumulates a corpus nobody can query. |
| [Claude Legal Skill](https://github.com/evolsb/claude-legal-skill) | Interesting | 438 | MIT | Reviews a contract against a stated risk framework and produces output a lawyer can work from. |
| [Python-Redlines](https://github.com/JSv4/Python-Redlines) | Interesting | 128 | MIT | The concrete deliverable in any negotiation is a redline. |
| [OpenNyAI](https://github.com/OpenNyAI/Opennyai) | Interesting | 101 | MIT | For anyone working in or investing into India, court judgments and legal documents in that jurisdiction were largely unprocessable by Western legal NLP. |
| [Open US Law](https://github.com/Vaquill-AI/open-us-law) | Interesting | 59 | Apache-2.0 | Millions of sections of state codes, the US Code, and regulations in a structured form. |

Full category pages: [Legal & Transaction Infrastructure](categories/legal.md), [Cap Tables & Equity](categories/cap-tables.md)

---

## Portfolio monitoring

_Track KPIs, updates, and risk across the book._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [Metabase](https://github.com/metabase/metabase) | Essential | 49.2k | unverified (Other) | Portfolio dashboards a partner will actually open: capital deployed by vintage, sector exposure, KPI collection across the book, and which companies are behind plan. |
| [Streamlit](https://github.com/streamlit/streamlit) | Essential | 45.7k | Apache-2.0 | The internal tool a fund builds once and uses daily: a company scorecard, an LP-return calculator, a portfolio KPI collector, a sourcing triage form. |
| [Apache Superset](https://github.com/apache/superset) | Interesting | 74.7k | Apache-2.0 | The heavier option when a fund's data questions have outgrown a simple dashboard: SQL exploration, scheduled reports to LPs, row-level access so a partner sees only their deals. |
| [Gradio](https://github.com/gradio-app/gradio) | Interesting | 43.5k | Apache-2.0 | When a fund wants to let colleagues try a scoring model, a classifier over inbound deals, or a document extractor, without anyone installing anything. |
| [Redash](https://github.com/getredash/redash) | Interesting | 28.8k | BSD-2-Clause | The middle ground: write SQL against the portfolio database, save the query, put a chart on it, share the link. |
| [Datasette](https://github.com/simonw/datasette) | Interesting | 11.5k | Apache-2.0 | Publish the portfolio database internally so anyone can browse companies, filter by sector, and run their own queries without asking an engineer. |

Full category pages: [Portfolio Management](categories/portfolio-management.md), [Relationship Intelligence](categories/relationship-intelligence.md), [Workflow & Automation](categories/automation.md)

---

## Follow-on

_Double down or pass, with the data to justify it._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [Metabase](https://github.com/metabase/metabase) | Essential | 49.2k | unverified (Other) | Portfolio dashboards a partner will actually open: capital deployed by vintage, sector exposure, KPI collection across the book, and which companies are behind plan. |
| [Streamlit](https://github.com/streamlit/streamlit) | Essential | 45.7k | Apache-2.0 | The internal tool a fund builds once and uses daily: a company scorecard, an LP-return calculator, a portfolio KPI collector, a sourcing triage form. |
| [Apache Superset](https://github.com/apache/superset) | Interesting | 74.7k | Apache-2.0 | The heavier option when a fund's data questions have outgrown a simple dashboard: SQL exploration, scheduled reports to LPs, row-level access so a partner sees only their deals. |
| [Gradio](https://github.com/gradio-app/gradio) | Interesting | 43.5k | Apache-2.0 | When a fund wants to let colleagues try a scoring model, a classifier over inbound deals, or a document extractor, without anyone installing anything. |
| [Redash](https://github.com/getredash/redash) | Interesting | 28.8k | BSD-2-Clause | The middle ground: write SQL against the portfolio database, save the query, put a chart on it, share the link. |
| [Datasette](https://github.com/simonw/datasette) | Interesting | 11.5k | Apache-2.0 | Publish the portfolio database internally so anyone can browse companies, filter by sector, and run their own queries without asking an engineer. |

Full category pages: [Portfolio Management](categories/portfolio-management.md), [Cap Tables & Equity](categories/cap-tables.md), [Investment Analysis](categories/investment-analysis.md)

---

## Exit

_Secondary, acquisition, or IPO — plus the LP side of the proceeds._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [OpenBB](https://github.com/OpenBB-finance/OpenBB) | Essential | 72.9k | unverified (Other) | Public comparables work: pull financials, prices, and fundamentals for the listed companies a target competes with, then build the trading multiples that anchor a valuation conversation. |
| [yfinance](https://github.com/ranaroussi/yfinance) | Essential | 25.2k | Apache-2.0 | The fastest way to get prices, financials, and history for a comparable set. |
| [edgartools](https://github.com/dgunning/edgartools) | Essential | 2.7k | MIT | Public filings are the best free source on a listed company's real economics, and they are hostile to read. |
| [Qlib](https://github.com/microsoft/qlib) | Interesting | 48.5k | MIT | Relevant beyond trading: backtesting a systematic signal or a scoring model before trusting it. |
| [AKShare](https://github.com/akfamily/akshare) | Interesting | 22.5k | MIT | Anyone looking at Chinese public comparables, or at a Chinese target's domestic competitors, hits a wall with Western data providers. |
| [QuantStats](https://github.com/ranaroussi/quantstats) | Interesting | 7.6k | Apache-2.0 | For a fund reporting on performance, or an analyst assessing a strategy someone has pitched: returns, drawdown, volatility, and ratios with a generated report. |

Full category pages: [Investment Analysis](categories/investment-analysis.md), [LP & Fund Management](categories/lp-management.md), [Legal & Transaction Infrastructure](categories/legal.md)

---

## Fund & LP operations

_Fund maths, LP reporting, capital calls, waterfalls._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [Grist](https://github.com/gristlabs/grist-core) | Interesting | 11.8k | Apache-2.0 | Where fund models belong when they outgrow a spreadsheet: capital call schedules, distribution waterfalls, and per-LP allocation tables, with formulas that reference records rather than cell ranges. |
| [Ledger](https://github.com/ledger/ledger) | Interesting | 6k | unverified (Other) | The tool that established the format the others follow. |
| [PyPortfolioOpt](https://github.com/PyPortfolio/PyPortfolioOpt) | Interesting | 6k | MIT | Fund-level questions about portfolio construction: concentration limits, correlation across a book, and expected risk given position sizes. |
| [Beancount](https://github.com/beancount/beancount) | Interesting | 6k | GPL-2.0 | The honest answer for a fund's books at small scale: capital calls, management fees, expenses, and per-LP capital accounts, all as text files in version control. |
| [hledger](https://github.com/hledgerorg/hledger) | Interesting | 4.7k | GPL-3.0 | The same approach as Beancount with more reporting built in: fund-level and per-LP balance sheets, cash flow, and the reports a quarterly LP update draws on, generated from text files. |
| [GnuCash](https://github.com/Gnucash/gnucash) | Interesting | 4.3k | unverified (Other) | For a fund or family office whose finance person wants proper accounting software rather than a command line: double-entry books, invoicing, and reports for a fund vehicle, with the data held locally. |

Full category pages: [LP & Fund Management](categories/lp-management.md), [Investment Analysis](categories/investment-analysis.md)

---

## Knowledge & memory

_Everything above, remembered and searchable._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [RAGFlow](https://github.com/infiniflow/ragflow) | Essential | 90.6k | Apache-2.0 | The knowledge layer a fund builds once so that memos, filings, and data-room material are answerable with citations. |
| [GraphRAG](https://github.com/microsoft/graphrag) | Essential | 36k | MIT | The questions a fund asks are relational: which companies in this sector share an investor, which founders came from the same company, where does this supply chain concentrate. |
| [Mem0](https://github.com/mem0ai/mem0) | Interesting | 65.2k | Apache-2.0 | Stops an internal research assistant from forgetting everything between sessions: a fund's preferences, prior conclusions, and who asked what. |
| [Logseq](https://github.com/logseq/logseq) | Interesting | 44.9k | AGPL-3.0 | Where an analyst's own thinking accumulates: meeting notes linked to companies, which link to sectors, which link to a thesis. |
| [Outline](https://github.com/outline/outline) | Interesting | 40.5k | unverified (Other) | The internal knowledge base a fund needs: sector theses, process documentation, and what everyone learned about a market, written down somewhere findable. |
| [LightRAG](https://github.com/HKUDS/LightRAG) | Interesting | 39.6k | MIT | The pragmatic middle: entity and relationship retrieval over a fund's document set without the indexing bill that makes graph RAG impractical at small scale. |

Full category pages: [Knowledge Management](categories/knowledge-management.md), [Data Rooms & Document Intelligence](categories/document-intelligence.md)

---

## Automation glue

_Make the rest of it run without a human._

| Project | Tier | Stars | License | VC use case |
|---|---|---:|---|---|
| [n8n](https://github.com/n8n-io/n8n) | Essential | 204.1k | unverified (Other) | The connective tissue a fund needs: a new deal lands in a form, gets enriched, appears in the pipeline, and pings the right partner. |
| [Apache Airflow](https://github.com/apache/airflow) | Essential | 46.8k | Apache-2.0 | When a fund's data work becomes real: nightly collection jobs, enrichment pipelines, and reports that have to run in order and tell someone when they fail. |
| [Airbyte](https://github.com/airbytehq/airbyte) | Essential | 22k | unverified (Other) | The ingestion layer: get data out of a CRM, a billing system, an accounting package, or a portfolio company's tooling and into the fund's own database. |
| [dbt](https://github.com/dbt-labs/dbt) | Essential | 13.8k | Apache-2.0 | Turns a fund's raw company and portfolio tables into the clean models that reporting depends on, with tests that catch a broken number before it reaches a partner. |
| [ToolJet](https://github.com/ToolJet/ToolJet) | Interesting | 40.9k | AGPL-3.0 | The same job as Appsmith with a different data model and a wider self-hosting story. |
| [Appsmith](https://github.com/appsmithorg/appsmith) | Interesting | 40.9k | Apache-2.0 | The internal screens a fund ends up needing: a deal review form, a portfolio data entry page, an admin view over the pipeline. |

Full category pages: [Workflow & Automation](categories/automation.md), [AI Agents for VC](categories/ai-agents.md), [Web Intelligence & OSINT](categories/osint.md)

---

## What open source does *not* cover

Worth saying plainly, because the gaps are where your budget goes:

- **Proprietary deal-flow databases.** The compiled private-company graphs (funding rounds, valuations, cap tables) are the moat of the incumbents. Open source gives you the tools to build your own; it does not hand you the data.
- **Compliance and fund administration.** Regulated, audit-facing processes with real liability. Nobody serious runs a fund's books on a hobby project.
- **Network effects.** The best deal flow is a byproduct of being known. No repository fixes that.
