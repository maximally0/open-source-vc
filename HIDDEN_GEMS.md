# Hidden Gems

The most valuable page here, and the one that required the most work.

Every entry below is deliberately **not** ranked by stars. A repository with 900 stars that solves a specific analyst problem is worth more to you than a 20,000-star framework you will never deploy. These are the projects that make a VC analyst stop scrolling:

- built by people who actually work in venture, or in a domain adjacent enough that they understood the problem
- tiny but sharp — one idea, executed properly
- recently emerged and not yet obvious
- academically sound and not yet productised

**40 projects.** If you only read two pages of this repository, make it this one and the [Starter Pack](STARTER_PACK.md).

_2026-09-14_

---

## Beancount

> Double-entry accounting in plain text files.

`beancount/beancount` · `GPL-2.0` · 6k★ · Recommended · [LP & Fund Management](categories/lp-management.md)

**Why it is here:** Plain-text accounting means every entry is diffable, reviewable, and permanent. For a fund vehicle, an audit trail that lives in git is a genuine improvement over a proprietary accounting file.

**VC use case:** The honest answer for a fund's books at small scale: capital calls, management fees, expenses, and per-LP capital accounts, all as text files in version control. An SPV or a first fund can keep accurate books without an administrator for every transaction.

**Limitations:** No interface: you write entries in a text editor and run commands. It is double-entry accounting, so the user has to understand the method. Not a replacement for an administrator handling LP compliance.

[GitHub](https://github.com/beancount/beancount)

---

## Buffett Investment Research

> A research workflow that starts from primary sources.

`MichaelRochonnn/buffett-investment-research` · `MIT` · 63★ · Experimental · [Investment Memo & IC](categories/investment-memos.md)

**Why it is here:** It encodes a research standard rather than a prompt, and the primary-source insistence is exactly what diligence reviews are meant to enforce.

**VC use case:** A worked example of the discipline that separates real research from summarisation: go to the primary document, extract what matters, and structure a conclusion with the source attached. Readable as a method even if you never run it.

**Limitations:** Single-author project around one investor's approach, so treat the method as one valid style rather than a standard.

[GitHub](https://github.com/MichaelRochonnn/buffett-investment-research)

---

## Cap Table and Exit Waterfall

> Cap table plus exit waterfall modelling.

`tdavidson/cap-table-tool` · `unverified (Other)` · 47★ · Experimental · [Cap Tables & Equity](categories/cap-tables.md)

**Why it is here:** Exit waterfalls are where funds discover that their ownership percentage is not what they thought. Having an open model means the assumptions are visible.

**VC use case:** The question that decides whether a deal is worth doing at a given price is what the exit proceeds actually return to each class, after preferences and participation. This models that, which is harder than modelling the round.

**Limitations:** No licence file, so reuse terms are unclear. Research-grade, not maintained as a product.

[GitHub](https://github.com/tdavidson/cap-table-tool)

---

## Cap Table Worksheet

> A spreadsheet-native cap table that computes the maths properly.

`1984vc/cap-table` · `MIT` · 139★ · Recommended · [Cap Tables & Equity](categories/cap-tables.md)

**Why it is here:** Someone who understood the arithmetic released the working model. That is a small corner of the market that commercial tools charge a lot to occupy.

**VC use case:** Most cap tables in venture are spreadsheets, and most of those are subtly wrong. This implements the mechanics from the standards, so a round's dilution, option pool shuffle, and conversion outcomes are computed rather than typed in.

**Limitations:** Small project with limited maintenance history. Verify against a known-good model before relying on it for a real round.

[GitHub](https://github.com/1984vc/cap-table)

---

## Company Research Agent

> An agent that researches a company and returns a structured brief.

`guy-hartstein/company-research-agent` · `Apache-2.0` · 2.3k★ · Recommended · [Company Discovery & Deal Sourcing](categories/company-discovery.md)

**Why it is here:** It is built on a graph of research steps rather than one long prompt, so the output shows the retrieval path. That makes the result easier to spot-check than a single model answer.

**VC use case:** Feed it a company name and get back a summary of what the company does, its market, competitors, and recent news, with sources. This is the first-pass brief an analyst writes before a screening call, assembled in minutes.

**Limitations:** Requires a search API key and an LLM provider, so it costs money to run. Output quality tracks the underlying search results, and citations need checking.

[GitHub](https://github.com/guy-hartstein/company-research-agent)

---

## CorpusCustody

> Checks whether training data was legally usable.

`rishin-sharma/CorpusCustody` · `MIT` · 51★ · Experimental · [Due Diligence](categories/due-diligence.md)

**Why it is here:** It treats data provenance as a checkable gate with resolved obligations rather than a legal opinion, which is the right shape for a diligence workstream that has to be repeatable.

**VC use case:** For a fund underwriting an AI company, the question of where its training data came from and under what terms is now a real diligence item. This resolves licence obligations across a dataset and reports incompatibilities.

**Limitations:** Very early project. It reads what the licences say, which is a factual check, not legal advice on whether a particular use is defensible.

[GitHub](https://github.com/rishin-sharma/CorpusCustody)

---

## Datasette

> Publish any database as a browsable, queryable site.

`simonw/datasette` · `Apache-2.0` · 11.5k★ · Recommended · [Portfolio Management](categories/portfolio-management.md)

**Why it is here:** It turns a database file into an explorable interface with almost no work, including a JSON API, so the same thing serves humans and scripts.

**VC use case:** Publish the portfolio database internally so anyone can browse companies, filter by sector, and run their own queries without asking an engineer. Also useful for shipping a dataset alongside a memo so a partner can check the numbers themselves.

**Limitations:** Read-oriented: not an editing interface or a reporting suite. Needs care around permissions if the data is sensitive.

[GitHub](https://github.com/simonw/datasette)

---

## dedupe

> Record linkage and entity resolution for messy company lists.

`dedupeio/dedupe` · `MIT` · 4.5k★ · Recommended · [Company Discovery & Deal Sourcing](categories/company-discovery.md)

**Why it is here:** You label a handful of pairs and it learns the rest, which handles the cases exact string matching misses: "Acme AI Inc" against "Acme.ai", or a legal entity against its trading name.

**VC use case:** Two funds merge sourcing lists, or a CRM export meets a scraped dataset, and someone has to decide which rows describe the same company before anything can be counted. This does that match at a scale no one does by hand.

**Limitations:** Needs labelled training pairs to perform well, and gets slow on millions of rows without tuning. Python only.

[GitHub](https://github.com/dedupeio/dedupe)

---

## Dexter

> An agent that does financial research and shows its work.

`virattt/dexter` · `unknown` · 27.6k★ · Experimental · [Investment Analysis](categories/investment-analysis.md)

**Why it is here:** It plans and executes research tasks rather than answering from memory, and it surfaces the reasoning, which is the only version of this worth using for anything that feeds a decision.

**VC use case:** Ask a financial question about a public company and get an answer with the research steps it took. Useful for the early orientation an analyst does before a call, and as a model for what a diligence agent should look like.

**Limitations:** No licence file is present, so reuse terms are unclear. Depends on external APIs and an LLM key, and its answers need checking.

[GitHub](https://github.com/virattt/dexter)

---

## dnstwist

> Finds lookalike domains around a brand.

`elceef/dnstwist` · `Apache-2.0` · 5.7k★ · Recommended · [Web Intelligence & OSINT](categories/osint.md)

**Why it is here:** It generates permutations and then checks which resolve and what is behind them, so results are live domains rather than speculation.

**VC use case:** Detect typo-squatting and phishing sites aimed at a portfolio company, and check whether a target has been quietly buying defensible domain variants. A concrete, checkable input to a security review.

**Limitations:** Fuzz results include legitimate lookalikes, so each hit needs a look. Some detection features depend on external services.

[GitHub](https://github.com/elceef/dnstwist)

---

## Due Diligence Agents

> Agents that flag risks across legal and finance and link them.

`zoharbabin/due-diligence-agents` · `Apache-2.0` · 104★ · Experimental · [Due Diligence](categories/due-diligence.md)

**Why it is here:** The cross-referencing is the interesting part. Most diligence tooling produces parallel checklists that never touch, which is exactly how correlated risks get missed.

**VC use case:** Runs separate reviewers over a deal, one legal-flavoured and one financial, then connects the flags they raise. The use case is catching the risk that only becomes visible when two workstreams are read together.

**Limitations:** Small project, and the agents produce flags for a human to judge rather than conclusions. Nothing here replaces counsel.

[GitHub](https://github.com/zoharbabin/due-diligence-agents)

---

## edgartools

> Read SEC filings as structured Python objects.

`dgunning/edgartools` · `MIT` · 2.7k★ · Essential · [Investment Analysis](categories/investment-analysis.md)

**Why it is here:** It handles XBRL properly, which is where most naive filings scrapers quietly produce wrong numbers, and it gives you the statements as dataframes rather than text.

**VC use case:** Public filings are the best free source on a listed company's real economics, and they are hostile to read. This turns a filing into data: financial statements, insider transactions, ownership. Analysts use it to build comparables or to read a competitor's actual numbers.

**Limitations:** US filings only. Filing formats change and the library tracks them, so older versions break on new filings.

[GitHub](https://github.com/dgunning/edgartools)

---

## edinet-tools

> Japanese corporate disclosure data, parsed.

`matthelmer/edinet-tools` · `MIT` · 53★ · Experimental · [Standards & Schemas](categories/standards.md)

**Why it is here:** It documents and parses a disclosure system that is effectively closed to anyone outside the country, which is exactly the sort of access gap that matters to a fund looking at that market.

**VC use case:** Japanese filings are available publicly but in a form almost nothing can read. This turns dozens of document types into typed objects, which makes research on Japanese companies possible without a local data vendor.

**Limitations:** Japanese-language domain, and coverage depends on the filing types the maintainer has implemented. Small project.

[GitHub](https://github.com/matthelmer/edinet-tools)

---

## ExecSum Deal Brief

> A daily deal-flow brief with a ranked top three.

`kklounge/execsum-deal-brief` · `MIT` · 50★ · Experimental · [Deal Sourcing & Pipeline](categories/deal-sourcing.md)

**Why it is here:** It ranks rather than lists, which is the part most monitoring tools skip. Ranking is where the judgement goes, so it is worth reading the code to see how it decides.

**VC use case:** Assembles a morning brief that ranks the day's deals and attaches expert and banking commentary. The use case is a partner's inbox at 7am: what moved, and what deserves a look, without anyone compiling it.

**Limitations:** Depends on external news and data sources that may change or require keys, and the ranking logic is simple enough to disagree with. Small project.

[GitHub](https://github.com/kklounge/execsum-deal-brief)

---

## ExploreYC

> Browse the YC portfolio as a searchable, filterable site.

`KonstantinMB/exploreyc` · `MIT` · 44★ · Recommended · [Company Discovery & Deal Sourcing](categories/company-discovery.md)

**Why it is here:** It layers an idea validator, a hiring board, and a crude success signal over the same dataset, which shows how far a public company graph can be stretched.

**VC use case:** A fast way to walk the YC universe by batch, industry, and hiring status when you want to see a sector rather than query an API. Useful for an associate building a market map for a thesis in an afternoon.

**Limitations:** Small project with a narrow dataset behind it, and the predictive features are demonstration-grade rather than something to make decisions on.

[GitHub](https://github.com/KonstantinMB/exploreyc)

---

## Financial Datasets MCP

> An MCP server that gives agents stock market data.

`financial-datasets/mcp-server` · `MIT` · 2.3k★ · Recommended · [Investment Analysis](categories/investment-analysis.md)

**Why it is here:** It takes the standard MCP approach, so it drops into any compatible agent instead of requiring a bespoke integration.

**VC use case:** Lets a research agent pull prices, financials, and fundamentals as a tool call rather than hallucinating them. Useful when building internal comparables tooling on top of an agent framework.

**Limitations:** Built around a commercial API, so it is an open client to a paid data source. US public companies only.

[GitHub](https://github.com/financial-datasets/mcp-server)

---

## Flowsint

> Graph-based investigations you can see.

`reconurge/flowsint` · `Apache-2.0` · 8.1k★ · Recommended · [Web Intelligence & OSINT](categories/osint.md)

**Why it is here:** It makes the investigation itself the interface, so the path from a name to a conclusion is visible and reviewable rather than buried in a script.

**VC use case:** Investigate an entity by following the graph: a person to their companies, those to their addresses and domains. For competitive research or checking whether two startups share founders or investors, the visual graph finds links a spreadsheet hides.

**Limitations:** Early project. Built for security investigations, so some entity types and connectors need adapting for company research.

[GitHub](https://github.com/reconurge/flowsint)

---

## Google Patents Public Data

> Patent data at scale, queryable in BigQuery.

`google/patents-public-data` · `Apache-2.0` · 691★ · Research · [Datasets & Open Data](categories/datasets.md)

**Why it is here:** Global patent records with citations and classifications in one queryable dataset, which is otherwise a commercial product. If you are mapping a technology area for a thesis, this is the primary source.

**VC use case:** Patent filings are a lagging but hard-to-fake signal of where a company and its competitors are investing R&D. Useful for the technology landscape around a deep-tech target, including who else is filing in the same space.

**Limitations:** Requires BigQuery access and SQL, and the repository has not been updated recently, so check the current data loading path. Filing-to-publication lag is eighteen months or more.

[GitHub](https://github.com/google/patents-public-data)

---

## Grist

> A spreadsheet that behaves like a database.

`gristlabs/grist-core` · `Apache-2.0` · 11.8k★ · Recommended · [LP & Fund Management](categories/lp-management.md)

**Why it is here:** It keeps the spreadsheet mental model while making the data relational, which is the right trade for fund maths that will be revisited for a decade.

**VC use case:** Where fund models belong when they outgrow a spreadsheet: capital call schedules, distribution waterfalls, and per-LP allocation tables, with formulas that reference records rather than cell ranges. The model stays readable and auditable when someone else inherits it.

**Limitations:** Formula language differs from Excel, so existing models need porting. Some enterprise features are commercial.

[GitHub](https://github.com/gristlabs/grist-core)

---

## hledger

> Plain-text accounting with a serious command line.

`hledgerorg/hledger` · `GPL-3.0` · 4.7k★ · Recommended · [LP & Fund Management](categories/lp-management.md)

**Why it is here:** Mature and fast, with reporting commands that cover what a small fund actually needs to produce. Its author has maintained it for years, which matters in accounting.

**VC use case:** The same approach as Beancount with more reporting built in: fund-level and per-LP balance sheets, cash flow, and the reports a quarterly LP update draws on, generated from text files.

**Limitations:** Same learning curve as any double-entry system, and no graphical interface by default. Needs discipline to keep entries current.

[GitHub](https://github.com/hledgerorg/hledger)

---

## Idea Reality

> Checks whether a product idea already exists, across five sources.

`mnemox-ai/idea-reality-mcp` · `MIT` · 815★ · Experimental · [Company Discovery & Deal Sourcing](categories/company-discovery.md)

**Why it is here:** It queries the places where working software shows up first, rather than press coverage, so it catches prior art that predates the funding announcements.

**VC use case:** Before a first call with a startup claiming a new category, run the premise through this to see what already exists on GitHub, Hacker News, npm, PyPI, and Product Hunt. It is a five-minute sanity check on how novel the claim really is.

**Limitations:** It reports existence, not quality or traction. A hit means something similar is public, which is not the same as a competitor, and a miss proves nothing.

[GitHub](https://github.com/mnemox-ai/idea-reality-mcp)

---

## ixbrl-parse

> Get usable data out of inline XBRL files.

`kanedata/ixbrl-parse` · `MIT` · 72★ · Recommended · [Standards & Schemas](categories/standards.md)

**Why it is here:** Inline XBRL mixed into HTML breaks naive parsers, and this handles the transformation properly rather than treating the file as text.

**VC use case:** Practical extraction from UK-style iXBRL accounts, which is the format most non-US filings use. Relevant for comparing private or small companies that file publicly in those jurisdictions.

**Limitations:** Oriented to UK filings, so other jurisdictions need work. Small project.

[GitHub](https://github.com/kanedata/ixbrl-parse)

---

## JobSpy

> Job postings from five boards into one dataframe.

`speedyapply/JobSpy` · `MIT` · 4.3k★ · Recommended · [Founder & Talent Discovery](categories/founder-discovery.md)

**Why it is here:** It covers LinkedIn, Indeed, Glassdoor, Google, and ZipRecruiter behind one interface and returns a typed frame, so a hiring signal can be built in an afternoon rather than a data-engineering project.

**VC use case:** A fund watching a sector can track which startups are hiring, for which functions, and how fast, without buying a labour-market dataset. Headcount movement by team is one of the few signals a private company cannot easily dress up.

**Limitations:** Upstream layout changes break scrapers without warning, and collecting from these boards may breach their terms of service. Check that before running it at scale.

[GitHub](https://github.com/speedyapply/JobSpy)

---

## Memo Generator

> Generates a startup investment memorandum.

`dforwardfeed/memo_generator` · `MIT` · 95★ · Experimental · [Investment Memo & IC](categories/investment-memos.md)

**Why it is here:** It targets the actual deliverable of venture work, the memo, rather than the research that precedes it. That framing is rare.

**VC use case:** Assembles a first-draft investment memo from inputs about a company. The honest use is as a scaffold: it prompts the analyst for the sections a memo needs, which is usually where junior writing stalls.

**Limitations:** Last meaningful activity some time ago, so treat it as a reference implementation to read rather than a tool to adopt. Output needs an investor's judgement throughout.

[GitHub](https://github.com/dforwardfeed/memo_generator)

---

## MiraclePlus Gallery

> Five years of MiraclePlus (formerly YC China) demo-day companies.

`Nimbus318/miracle-plus-gallery` · `MIT` · 25★ · Experimental · [Company Discovery & Deal Sourcing](categories/company-discovery.md)

**Why it is here:** The data is in Chinese and nowhere else in a structured form. It is a reminder that a large part of the world's startup activity is invisible to English-language searches.

**VC use case:** A structured look at the portfolio of the accelerator that ran YC's China programme, including sector tags, school networks, and people links. For anyone investing in or researching Chinese AI, robotics, or cross-border companies this is otherwise hard to assemble.

**Limitations:** Interface and data are Chinese-language, coverage stops at the programme's end, and there is no licence file. Confirm terms before reuse.

[GitHub](https://github.com/Nimbus318/miracle-plus-gallery)

---

## NetworkX

> Graph analysis in plain Python.

`networkx/networkx` · `unverified (Other)` · 17.3k★ · Recommended · [Relationship Intelligence](categories/relationship-intelligence.md)

**Why it is here:** Co-investment graphs, board interlocks, and founder networks are all the same problem, and this is the standard tool for it. It needs no database and no infrastructure.

**VC use case:** The warm-introduction question that every fund asks and almost none can answer systematically: which of our contacts is closest to this founder, and through whom. Model people and companies as a graph and NetworkX computes the shortest paths instead of you asking around.

**Limitations:** In-memory, so very large graphs need more than networkx. You have to build and maintain the graph yourself; the quality of the answer depends entirely on the data you feed it.

[GitHub](https://github.com/networkx/networkx)

---

## OpenAlex API

> An open index of scholarly research.

`ourresearch/openalex-api` · `MIT` · 8★ · Experimental · [Datasets & Open Data](categories/datasets.md)

**Why it is here:** It replaced a proprietary index with an openly licensed one, including institutions, authors, and citations, which makes research credentialing automatable.

**VC use case:** For technical diligence on a research-driven company, this is how you check a founder's publication record, their citation impact, and who they worked with, without access to a paid bibliographic database.

**Limitations:** Author disambiguation is imperfect, so a name match needs confirming. Coverage of non-Western publication venues is improving but uneven.

[GitHub](https://github.com/ourresearch/openalex-api)

---

## OpenBook

> An open investor and venture database.

`iloveitaly/openbook` · `MIT` · 64★ · Experimental · [Company Discovery & Deal Sourcing](categories/company-discovery.md)

**Why it is here:** It is the only serious open attempt at this dataset that this research turned up, which makes it worth watching even at its current size.

**VC use case:** A community attempt at the investor-and-fund graph that normally sits behind a PitchBook licence: who invests at which stage, in which sectors, and alongside whom. Useful for building a target list of funds rather than companies.

**Limitations:** Early and thin compared with commercial alternatives, and coverage of any given sector is likely incomplete. Verify entries upstream before relying on them.

[GitHub](https://github.com/iloveitaly/openbook)

---

## PatentsView

> US patent data, queryable.

`PatentsView/PatentsView-API` · `BSD-2-Clause` · 20★ · Experimental · [Datasets & Open Data](categories/datasets.md)

**Why it is here:** The data is government-sourced and freely available, including assignees and citations, which is enough to map a technology landscape without a commercial patent database.

**VC use case:** Patent filings are a lagging but honest signal of where a company or a sector is investing. Useful for technical diligence on a deep-tech target and for mapping which institutions are active in a field.

**Limitations:** US patents only, with a lag of eighteen months or more between filing and publication. The repository is largely a client for the API rather than the dataset itself.

[GitHub](https://github.com/PatentsView/PatentsView-API)

---

## Prediction Market Analysis

> A framework and dataset for prediction market data.

`Jon-Becker/prediction-market-analysis` · `MIT` · 3.8k★ · Experimental · [Investment Analysis](categories/investment-analysis.md)

**Why it is here:** It publishes a real dataset alongside the collection code, which is unusual and means an analyst can start from data rather than from an empty pipeline.

**VC use case:** Prediction markets price things that analysts only opine on: elections, rate moves, regulatory outcomes. This collects that data, so a thesis built on a political or macro assumption can be checked against a market price instead of a gut feel.

**Limitations:** Market prices reflect liquidity and sentiment, not truth, and thin markets are misleading. Coverage is limited to what the platforms list.

[GitHub](https://github.com/Jon-Becker/prediction-market-analysis)

---

## PyPortfolioOpt

> Portfolio construction and optimisation in Python.

`PyPortfolio/PyPortfolioOpt` · `MIT` · 6k★ · Recommended · [LP & Fund Management](categories/lp-management.md)

**Why it is here:** The methods are documented with their assumptions stated, which matters when the output feeds an allocation decision and someone asks why a weight is what it is.

**VC use case:** Fund-level questions about portfolio construction: concentration limits, correlation across a book, and expected risk given position sizes. Also usable for a fund of funds sizing allocations across managers.

**Limitations:** Optimisers are sensitive to inputs, and small error in expected returns produces large changes in weights. Venture returns are not normally distributed, so classical assumptions fit badly.

[GitHub](https://github.com/PyPortfolio/PyPortfolioOpt)

---

## Python-Redlines

> Generate Word tracked changes from Python.

`JSv4/Python-Redlines` · `MIT` · 128★ · Recommended · [Legal & Transaction Infrastructure](categories/legal.md)

**Why it is here:** Producing genuine tracked changes rather than a PDF comparison is fiddly, and this solves it. There is almost nothing else open source that does it.

**VC use case:** The concrete deliverable in any negotiation is a redline. This produces native Word tracked changes programmatically, so a fund or its tooling can generate a marked-up draft a counterparty can open, comment on, and accept.

**Limitations:** Narrow tool: it produces the redline, it does not decide what should change. Word compatibility details matter.

[GitHub](https://github.com/JSv4/Python-Redlines)

---

## Rizzo PII

> Anonymise documents before they reach a model.

`Rizzo-AI-Academy/rizzo-pii` · `MIT` · 980★ · Recommended · [Due Diligence](categories/due-diligence.md)

**Why it is here:** It runs locally, which is the whole point. Most PII tooling assumes the document is going to a cloud service you have already decided to trust.

**VC use case:** Data rooms contain salaries, customer names, personal data, and contract terms that should not be pasted into a hosted model. This strips personal information locally first, so an analyst can use an LLM on diligence material without breaching an NDA or a privacy obligation.

**Limitations:** Detection will miss unusual identifiers, so a pass over the output is still needed. Anonymisation is not a legal substitute for an NDA.

[GitHub](https://github.com/Rizzo-AI-Academy/rizzo-pii)

---

## Runway Tool

> Runway and cash-budget forecasting for a startup.

`tdavidson/runway-tool` · `unverified (Other)` · 16★ · Experimental · [Portfolio Management](categories/portfolio-management.md)

**Why it is here:** Almost no open-source tooling exists for this, despite it being the most-asked portfolio question. It is a small model someone who understood the problem released.

**VC use case:** The single number a board watches: how many months of cash remain, under what hiring and spend assumptions. This models the scenario, which is what a fund needs when a portfolio company's bridge question arrives two months earlier than planned.

**Limitations:** Small project that has not been touched since 2020, and the licence is not a standard SPDX identifier. Read it as a model to adapt rather than a maintained tool.

[GitHub](https://github.com/tdavidson/runway-tool)

---

## shhgit

> Finds secrets committed to public repositories.

`eth0izzle/shhgit` · `MIT` · 4k★ · Experimental · [Due Diligence](categories/due-diligence.md)

**Why it is here:** It monitors commit streams rather than one-off scanning, so exposure gets caught when it happens rather than when someone remembers to look.

**VC use case:** Leaked keys and credentials in a company's public repositories are a diligence finding with two readings: a security problem to price, and occasionally a signal about engineering maturity. Check the target, and check whether a portfolio company is leaking.

**Limitations:** Public repositories only, and a match is a lead: many are test fixtures or rotated keys. Confirm before you write it into a memo.

[GitHub](https://github.com/eth0izzle/shhgit)

---

## subsignal

> Deal-flow monitoring built for funds.

`0xnyn/subsignal` · `unknown` · 29★ · Experimental · [Deal Sourcing & Pipeline](categories/deal-sourcing.md)

**Why it is here:** It is one of very few projects written for investors rather than adapted from a general monitoring tool, so the event model matches how a fund actually tracks a watchlist.

**VC use case:** Watches company and competitor signals so an analyst does not have to check the same sites weekly: new products, pricing changes, launches. The intended output is a shortlist of companies whose activity changed, which is the raw material of outbound sourcing.

**Limitations:** Early-stage with a small maintainer base, and no licence file is present, so terms for reuse are unclear. Expect to write your own connectors.

[GitHub](https://github.com/0xnyn/subsignal)

---

## TickerToThesis

> A research pipeline that produces an investment memo.

`jasonfdg/TickerToThesis` · `unknown` · 26★ · Experimental · [Investment Memo & IC](categories/investment-memos.md)

**Why it is here:** The pipeline is the point: it shows the sequence from raw filings to a written thesis, which is the process a fund is really trying to automate.

**VC use case:** Takes a ticker, gathers public research, and drafts a memo in the shape a buyside analyst would expect. Worth reading for the section structure alone, which translates to private deals.

**Limitations:** No licence file, so terms are unclear. Public-company inputs, and the writing still needs a human with a view.

[GitHub](https://github.com/jasonfdg/TickerToThesis)

---

## VC Reporting

> An AI-native platform for fund reporting and analysis.

`tdavidson/reporting` · `Apache-2.0` · 53★ · Experimental · [Investment Memo & IC](categories/investment-memos.md)

**Why it is here:** Most fund software is built by engineers guessing at investor workflows. This one started from the reporting obligation, which is the part with a deadline attached.

**VC use case:** Covers the recurring paperwork a fund owes its LPs and itself: portfolio updates, performance reporting, and the analysis that goes with them. Built by an investor, which shows in what it chooses to automate.

**Limitations:** Small project by an individual investor, so continuity is a real question. Early.

[GitHub](https://github.com/tdavidson/reporting)

---

## WhisperX

> Transcription with word timings and speaker labels.

`m-bain/whisperX` · `BSD-2-Clause` · 24k★ · Recommended · [Relationship Intelligence](categories/relationship-intelligence.md)

**Why it is here:** It adds speaker diarisation and accurate word-level timestamps on top of Whisper, which turns a transcript into something closer to a minute-by-minute record.

**VC use case:** The version you want for investment committee: a transcript that shows who said what and when. When a founder's claim gets discussed three months later, knowing which person made it matters.

**Limitations:** More setup than plain Whisper, and diarisation degrades when several people speak at once or the audio is poor.

[GitHub](https://github.com/m-bain/whisperX)

---

## World Intel MCP

> A large MCP toolset for global intelligence feeds.

`marc-shade/world-intel-mcp` · `MIT` · 638★ · Experimental · [Market & Industry Research](categories/market-research.md)

**Why it is here:** It packages a wide set of public data sources behind a standard agent interface, which is the difference between an agent that can look things up and one that just writes from memory.

**VC use case:** Gives an agent access to markets, filings, conflict, and macro feeds through one MCP server, so a research agent can pull current data instead of only reading web pages. Useful for funds whose theses depend on macro or geopolitical conditions.

**Limitations:** Young project with a large surface area, so individual tools vary in reliability. Some upstream sources require keys or rate-limit heavily.

[GitHub](https://github.com/marc-shade/world-intel-mcp)

---
