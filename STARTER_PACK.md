# The VC Open Source Starter Pack

If you are new to this — an analyst on week one, an emerging manager with no platform team, a scout with your own laptop — start here. Not with 200 repositories. With these.

**32 projects**, arranged in the order a deal actually moves through the fund. Each one earns its place by replacing a paid product you would otherwise need, or by doing something no paid product does.

```text
Find companies → Research founders → Research markets → Run diligence
   → Read the documents → Model the investment → Write the memo
   → Track the portfolio
```

Pair this with [VC_WORKFLOW.md](VC_WORKFLOW.md) for the full process map and [COMPARISON.md](COMPARISON.md) when you are choosing between options.

_2026-09-14_

---

## Sourcing

**[YC Open API](https://github.com/yc-oss/api)** — Y Combinator's own company and founder data, as an API.

`unknown` · 231★ · Essential · [Company Discovery & Deal Sourcing](categories/company-discovery.md)

Every YC company with its batch, industry, team size, status, and founders, plus a website field.

**[Sherlock](https://github.com/sherlock-project/sherlock)** — Find an account on 400+ sites from a username alone.

`MIT` · 91.5k★ · Essential · [Founder & Talent Discovery](categories/founder-discovery.md)

When a founder's name is common or their LinkedIn is thin, an analyst runs the handle they use elsewhere through Sherlock to see where else that handle exists.

**[Web-Check](https://github.com/lissy93/web-check)** — A full external read of any website from a single URL.

`MIT` · 34.8k★ · Essential · [Founder & Talent Discovery](categories/founder-discovery.md)

Point it at a target company's domain and get its hosting, DNS and mail records, TLS configuration, exposed headers, and third-party services.

**[NocoDB](https://github.com/nocodb/nocodb)** — Airtable-style database over Postgres, MySQL, or SQLite.

`unverified (Other)` · 65k★ · Essential · [Deal Sourcing & Pipeline](categories/deal-sourcing.md)

The deals pipeline most small funds actually need: stages, owners, next actions, and notes, as a grid anyone on the team can edit, sitting on a real database you control.

**[changedetection.io](https://github.com/dgtlmoon/changedetection.io)** — Tell me when a specific page changes.

`Apache-2.0` · 34.1k★ · Essential · [Deal Sourcing & Pipeline](categories/deal-sourcing.md)

The narrow version of monitoring and the one analysts actually need: a competitor drops a price, adds a plan, edits a terms page, or a portfolio company quietly reshuffles its team page.

---

## Founder research

**[Monica](https://github.com/monicahq/monica)** — A personal CRM for the relationships a fund actually runs on.

`AGPL-3.0` · 25.3k★ · Essential · [Relationship Intelligence](categories/relationship-intelligence.md)

Every investor keeps the same private list: who introduced whom, what they care about, when you last spoke, what you promised.

**[Whisper](https://github.com/openai/whisper)** — Speech to text that holds up on real calls.

`MIT` · 109.1k★ · Recommended · [Relationship Intelligence](categories/relationship-intelligence.md)

Turn founder calls into a transcript you can search, quote in a memo, and keep as part of the record.

**[Cal.com](https://github.com/calcom/cal.diy)** — Scheduling that you host yourself.

`MIT` · 48.4k★ · Essential · [Relationship Intelligence](categories/relationship-intelligence.md)

Founder calls, LP check-ins, and office hours all live or die on scheduling.

**[Playwright](https://github.com/microsoft/playwright)** — Drive Chrome, Firefox, and WebKit from code.

`Apache-2.0` · 96.1k★ · Recommended · [Web Intelligence & OSINT](categories/osint.md)

The foundation for any workflow that needs a real browser: logging into a portal and pulling a report, capturing a screenshot for evidence, or checking that a portfolio company's signup flow still works.

**[SingleFile](https://github.com/gildas-lormeau/SingleFile)** — Save a faithful, self-contained copy of a web page.

`AGPL-3.0` · 22.4k★ · Essential · [Web Intelligence & OSINT](categories/osint.md)

Evidence capture.

---

## Company research

**[GPT Researcher](https://github.com/assafelovic/gpt-researcher)** — An agent that researches a question across many sources and cites them.

`Apache-2.0` · 29.4k★ · Essential · [Market & Industry Research](categories/market-research.md)

Hand it a market question, such as how many companies are selling continuous compliance tooling into European banks and who funded them, and it returns a written answer with the sources it used.

**[STORM](https://github.com/stanford-oval/storm)** — Writes a cited article from scratch on any topic.

`MIT` · 31.3k★ · Essential · [Market & Industry Research](categories/market-research.md)

Ask it to produce a briefing on a sector and it researches, outlines, and drafts with references.

**[Khoj](https://github.com/khoj-ai/khoj)** — Search your own documents and the web from one place.

`AGPL-3.0` · 37.3k★ · Essential · [Market & Industry Research](categories/market-research.md)

A fund's institutional memory problem: a hundred memos, data-room exports, and meeting notes that nobody can search.

---

## Market research

**[RAGFlow](https://github.com/infiniflow/ragflow)** — A retrieval system built around deep document understanding.

`Apache-2.0` · 90.7k★ · Recommended · [Knowledge Management](categories/knowledge-management.md)

The knowledge layer a fund builds once so that memos, filings, and data-room material are answerable with citations.

---

## Initial screening

**[OpenBB](https://github.com/OpenBB-finance/OpenBB)** — An open research platform for markets and financial data.

`unverified (Other)` · 73k★ · Essential · [Investment Analysis](categories/investment-analysis.md)

Public comparables work: pull financials, prices, and fundamentals for the listed companies a target competes with, then build the trading multiples that anchor a valuation conversation.

**[Finance Toolkit](https://github.com/JerBouma/FinanceToolkit)** — A hundred-odd financial ratios and models in one library.

`MIT` · 5.3k★ · Recommended · [Investment Analysis](categories/investment-analysis.md)

The maths between a company's financial statements and a view on it: margins, returns, leverage, growth, and valuation multiples, computed consistently.

---

## Due diligence

**[PaperQA](https://github.com/Future-House/paper-qa)** — Answers questions from scientific documents with citations.

`Apache-2.0` · 9.2k★ · Essential · [Due Diligence](categories/due-diligence.md)

Technical diligence on a deep-tech company: read the founders' papers and patents, then ask whether the claimed result holds up, with page-level citations.

**[Unstructured](https://github.com/Unstructured-IO/unstructured)** — Turns documents of any format into structured elements.

`Apache-2.0` · 15.4k★ · Essential · [Data Rooms & Document Intelligence](categories/document-intelligence.md)

A data room is a pile of PDFs, slide decks, spreadsheets, and scans in no particular order.

**[Docling](https://github.com/docling-project/docling)** — Layout-aware conversion of PDFs and office documents.

`MIT` · 66.4k★ · Essential · [Data Rooms & Document Intelligence](categories/document-intelligence.md)

Financial statements and contracts are where layout carries meaning: which number sits in which column, which heading a clause falls under.

**[Marker](https://github.com/datalab-to/marker)** — Fast, accurate PDF to markdown and JSON.

`Apache-2.0` · 39.7k★ · Essential · [Data Rooms & Document Intelligence](categories/document-intelligence.md)

The workhorse for converting a data room into text an analyst or a model can read.

**[OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF)** — Adds a searchable text layer to scanned PDFs.

`MPL-2.0` · 34.8k★ · Essential · [Data Rooms & Document Intelligence](categories/document-intelligence.md)

The unglamorous step that makes everything else possible.

**[Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx)** — Scan, index, and search every document you own.

`GPL-3.0` · 45.1k★ · Essential · [Data Rooms & Document Intelligence](categories/document-intelligence.md)

The document archive for a fund or a family office: every contract, statement, and filing OCR'd, tagged, and full-text searchable, with the original file retained.

**[Mike](https://github.com/open-legal-products/mike)** — An open legal AI platform for document review.

`AGPL-3.0` · 4.2k★ · Essential · [Legal & Transaction Infrastructure](categories/legal.md)

Contract review is the most expensive line item in a deal that nobody talks about.

---

## Financial analysis

**[Captable](https://github.com/captableinc/captable)** — An open-source cap table management platform.

`AGPL-3.0` · 822★ · Essential · [Cap Tables & Equity](categories/cap-tables.md)

The cap table, dilution modelling, and stakeholder records that every fund currently pays a vendor for.

---

## Portfolio monitoring

**[Metabase](https://github.com/metabase/metabase)** — Business intelligence that non-technical people can use.

`unverified (Other)` · 49.2k★ · Essential · [Portfolio Management](categories/portfolio-management.md)

Portfolio dashboards a partner will actually open: capital deployed by vintage, sector exposure, KPI collection across the book, and which companies are behind plan.

**[Streamlit](https://github.com/streamlit/streamlit)** — Turn a Python script into a web app.

`Apache-2.0` · 45.7k★ · Essential · [Portfolio Management](categories/portfolio-management.md)

The internal tool a fund builds once and uses daily: a company scorecard, an LP-return calculator, a portfolio KPI collector, a sourcing triage form.

**[n8n](https://github.com/n8n-io/n8n)** — Workflow automation with a fair-code licence.

`unverified (Other)` · 204.2k★ · Recommended · [Workflow & Automation](categories/automation.md)

The connective tissue a fund needs: a new deal lands in a form, gets enriched, appears in the pipeline, and pings the right partner.

**[dbt](https://github.com/dbt-labs/dbt)** — Transform data with SQL that is tested and documented.

`Apache-2.0` · 13.8k★ · Recommended · [Workflow & Automation](categories/automation.md)

Turns a fund's raw company and portfolio tables into the clean models that reporting depends on, with tests that catch a broken number before it reaches a partner.

---

## Automation glue

**[browser-use](https://github.com/browser-use/browser-use)** — Let a model drive a real browser.

`MIT` · 114.6k★ · Recommended · [AI Agents for VC](categories/ai-agents.md)

The tool that makes research agents actually work, because most of the useful public information sits behind JavaScript, logins, and search boxes rather than an API.

**[LangGraph](https://github.com/langchain-ai/langgraph)** — Agents as explicit graphs with state.

`MIT` · 41.6k★ · Recommended · [AI Agents for VC](categories/ai-agents.md)

The right shape for a diligence workflow, where steps depend on what earlier steps found and a human needs to approve before the next stage.

**[LlamaIndex](https://github.com/run-llama/llama_index)** — Connect models to your own data.

`MIT` · 52.2k★ · Recommended · [AI Agents for VC](categories/ai-agents.md)

The most common foundation for a fund's document assistant: load a data room, build an index, and query it with citations.

---

## Other

**[Open Cap Format](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF)** — An open data standard for cap tables.

`unverified (Other)` · 188★ · Essential · [Standards & Schemas](categories/standards.md)

Cap tables currently move between founders, lawyers, and investors as spreadsheets in whatever shape the last person used.

---
