# Investment Analysis

_The maths between the meeting and the memo._

Startup and investment scoring, financial analysis, valuation, DCF, comparables, and scenario modelling.

**14 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-12

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

---

### OpenBB

> An open research platform for markets and financial data.

`OpenBB-finance/OpenBB` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Investment Analysis |
| **License** | unverified (Other) |
| **Stars** | 72.9k |
| **Forks** | 7.5k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

Public comparables work: pull financials, prices, and fundamentals for the listed companies a target competes with, then build the trading multiples that anchor a valuation conversation. Analysts use it to avoid rebuilding the same data plumbing at every fund.

**Why it's interesting**

It provides one interface across many data providers, so a comparable-set analysis does not depend on a single vendor's coverage. It also has a real extension system, which is how funds add their own private data.

**Good for**

- Comparable companies
- Public market research
- Valuation

**Limitations**

Most data providers behind it require their own keys and subscriptions, and the licence is not a standard SPDX identifier. Coverage of private companies is out of scope by design.

**Dependencies:** Python 3.9+

**Links:** [GitHub](https://github.com/OpenBB-finance/OpenBB) &nbsp;·&nbsp; [Site](https://openbb.co)

---

### yfinance

> Market data from Yahoo Finance in a few lines.

`ranaroussi/yfinance` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Investment Analysis |
| **License** | Apache-2.0 |
| **Stars** | 25.2k |
| **Forks** | 3.4k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-10) |
| **Self-hostable** | yes |

**VC use case**

The fastest way to get prices, financials, and history for a comparable set. Analysts reach for it to sanity-check a valuation or see how a sector has traded, without a data subscription.

**Why it's interesting**

It needs no key and no account, which makes it the standard starting point for any ad-hoc market analysis and the reason countless research notebooks exist.

**Good for**

- Comparable companies
- Market data
- Quick analysis

**Limitations**

Unofficial and dependent on an undocumented upstream, so it breaks occasionally and should not sit under anything production-critical. Not for licensed or regulated use.

**Dependencies:** Python 3.9+

**Links:** [GitHub](https://github.com/ranaroussi/yfinance) &nbsp;·&nbsp; [Site](https://ranaroussi.github.io/yfinance)

---

### edgartools

> Read SEC filings as structured Python objects.

`dgunning/edgartools` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Investment Analysis |
| **License** | MIT |
| **Stars** | 2.7k |
| **Forks** | 480 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

Public filings are the best free source on a listed company's real economics, and they are hostile to read. This turns a filing into data: financial statements, insider transactions, ownership. Analysts use it to build comparables or to read a competitor's actual numbers.

**Why it's interesting**

It handles XBRL properly, which is where most naive filings scrapers quietly produce wrong numbers, and it gives you the statements as dataframes rather than text.

**Good for**

- Public comparables
- Filings research
- Due diligence

**Limitations**

US filings only. Filing formats change and the library tracks them, so older versions break on new filings.

**Links:** [GitHub](https://github.com/dgunning/edgartools) &nbsp;·&nbsp; [Site](https://edgartools.readthedocs.io/)

---

### Qlib

> A platform for quantitative research and backtesting.

`microsoft/qlib` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Investment Analysis |
| **License** | MIT |
| **Stars** | 48.5k |
| **Forks** | 7.7k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-02) |
| **Self-hostable** | yes |

**VC use case**

Relevant beyond trading: backtesting a systematic signal or a scoring model before trusting it. If a fund claims a model predicts which companies succeed, this is the kind of machinery needed to test that claim honestly, including the parts that make backtests lie.

**Why it's interesting**

It handles the data pipeline, model training, and evaluation in one place with point-in-time correctness, which is where naive backtests go wrong.

**Good for**

- Signal testing
- Quantitative research
- Model validation

**Limitations**

Built for public market data, so applying it to venture outcomes means designing your own dataset and being honest about how few data points you have.

**Links:** [GitHub](https://github.com/microsoft/qlib) &nbsp;·&nbsp; [Site](https://qlib.readthedocs.io/en/latest/)

---

### AKShare

> Financial data for Chinese markets.

`akfamily/akshare` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Investment Analysis |
| **License** | MIT |
| **Stars** | 22.5k |
| **Forks** | 3.5k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-09) |
| **Self-hostable** | yes |

**VC use case**

Anyone looking at Chinese public comparables, or at a Chinese target's domestic competitors, hits a wall with Western data providers. This covers A-shares, funds, macro, and industry data for that market.

**Why it's interesting**

It covers a market that most open financial libraries ignore, and it wraps the sources behind a consistent interface so a comparable analysis can be written once.

**Good for**

- China market research
- Comparable companies
- Market data

**Limitations**

Documentation and community are largely Chinese-language, and it depends on upstream sites that change. Data licensing varies by source.

**Links:** [GitHub](https://github.com/akfamily/akshare) &nbsp;·&nbsp; [Site](https://akshare.akfamily.xyz)

---

### QuantStats

> Portfolio analytics and tear sheets.

`ranaroussi/quantstats` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Investment Analysis |
| **License** | Apache-2.0 |
| **Stars** | 7.6k |
| **Forks** | 1.2k |
| **Language** | Python |
| **Status** | Active (last push 2026-07-20) |
| **Self-hostable** | yes |

**VC use case**

For a fund reporting on performance, or an analyst assessing a strategy someone has pitched: returns, drawdown, volatility, and ratios with a generated report. Turns a column of monthly returns into something a partner can read.

**Why it's interesting**

It produces the standard performance report in one call, including the metrics people will ask about, which saves rebuilding the same charts each time.

**Good for**

- Performance reporting
- LP reporting
- Strategy assessment

**Limitations**

Equally precise outputs for a portfolio with three data points, so it invites over-reading on small samples, which venture always is.

**Links:** [GitHub](https://github.com/ranaroussi/quantstats)

---

### QuantLib

> A quantitative finance library for pricing and risk.

`lballabio/QuantLib` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Investment Analysis |
| **License** | unverified (Other) |
| **Stars** | 7.6k |
| **Forks** | 2.3k |
| **Language** | C++ |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

Relevant for structured and debt-like instruments: convertible notes, SAFEs with caps and discounts, and any instrument where the valuation depends on assumptions about volatility and time. Also how a fund values an option-heavy compensation pool.

**Why it's interesting**

Two decades of use with the methods documented and tested, ported across many languages. Where a valuation question needs defensible maths rather than a spreadsheet formula, this is what practitioners reach for.

**Good for**

- Instrument valuation
- Structured terms
- Risk analysis

**Limitations**

Steep learning curve, and it assumes the user understands the finance. Licence is not a standard SPDX identifier, so check terms.

**Links:** [GitHub](https://github.com/lballabio/QuantLib) &nbsp;·&nbsp; [Site](http://quantlib.org)

---

### Finance Toolkit

> A hundred-odd financial ratios and models in one library.

`JerBouma/FinanceToolkit` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Investment Analysis |
| **License** | MIT |
| **Stars** | 5.3k |
| **Forks** | 614 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-10) |
| **Self-hostable** | yes |

**VC use case**

The maths between a company's financial statements and a view on it: margins, returns, leverage, growth, and valuation multiples, computed consistently. Useful for turning a set of uploaded financials into a normalised picture before the modelling starts.

**Why it's interesting**

It computes around a hundred ratios with the formulas documented, so a number can be traced to its definition. That matters when two analysts disagree about what a metric means.

**Good for**

- Financial analysis
- Comparable companies
- Diligence models

**Limitations**

Assumes reasonably standard financial statements, so unusual business models need work. Not a modelling environment: output still goes into a spreadsheet or notebook.

**Links:** [GitHub](https://github.com/JerBouma/FinanceToolkit) &nbsp;·&nbsp; [Site](https://www.jeroenbouma.com/projects/financetoolkit)

---

### FinancePy

> Derivatives pricing and risk in Python.

`domokane/FinancePy` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Investment Analysis |
| **License** | GPL-3.0 |
| **Stars** | 3.1k |
| **Forks** | 437 |
| **Language** | Jupyter Notebook |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

The Python-native option for valuing instruments with optionality: convertibles, warrants, and option pools. Relevant to late-stage and structured deals where the headline valuation hides the terms.

**Why it's interesting**

It reads as a teaching library as much as a pricing one, with worked examples, which makes it usable by someone who is not a quant.

**Good for**

- Structured terms
- Instrument valuation
- Diligence models

**Limitations**

GPL-licensed, which affects how you can ship anything built on it. Smaller community than QuantLib.

**Links:** [GitHub](https://github.com/domokane/FinancePy)

---

### Financial Datasets MCP

> An MCP server that gives agents stock market data.

`financial-datasets/mcp-server` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Investment Analysis |
| **License** | MIT |
| **Stars** | 2.3k |
| **Forks** | 348 |
| **Language** | Python |
| **Status** | Dormant (last push 2025-06-05, 15mo) |
| **Self-hostable** | yes |

**VC use case**

Lets a research agent pull prices, financials, and fundamentals as a tool call rather than hallucinating them. Useful when building internal comparables tooling on top of an agent framework.

**Why it's interesting**

It takes the standard MCP approach, so it drops into any compatible agent instead of requiring a bespoke integration.

**Good for**

- Agent tooling
- Comparable companies
- Internal tools

**Limitations**

Built around a commercial API, so it is an open client to a paid data source. US public companies only.

**Links:** [GitHub](https://github.com/financial-datasets/mcp-server) &nbsp;·&nbsp; [Site](https://www.financialdatasets.ai/)

---

### SEC EDGAR Downloader

> Bulk-download filings from EDGAR.

`jadchaar/sec-edgar-downloader` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Investment Analysis |
| **License** | MIT |
| **Stars** | 717 |
| **Forks** | 166 |
| **Language** | Python |
| **Status** | Active (last push 2026-06-22) |
| **Self-hostable** | yes |

**VC use case**

When a diligence needs thirty companies' filings rather than one, someone has to fetch them all. This handles the downloading, including the rate limits EDGAR enforces, so the collection job is a script rather than an afternoon of clicking.

**Why it's interesting**

It respects EDGAR's rate limits by design, which is the difference between a collection job that runs and one that gets you blocked.

**Good for**

- Filings collection
- Public comparables
- Dataset building

**Limitations**

Downloading only: it does not parse the contents. Pair it with a parser.

**Links:** [GitHub](https://github.com/jadchaar/sec-edgar-downloader) &nbsp;·&nbsp; [Site](https://sec-edgar-downloader.readthedocs.io)

---

### Dexter

> An agent that does financial research and shows its work.

`virattt/dexter` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Investment Analysis |
| **License** | unknown |
| **Stars** | 27.6k |
| **Forks** | 3.4k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-08-04) |
| **Self-hostable** | yes |

**VC use case**

Ask a financial question about a public company and get an answer with the research steps it took. Useful for the early orientation an analyst does before a call, and as a model for what a diligence agent should look like.

**Why it's interesting**

It plans and executes research tasks rather than answering from memory, and it surfaces the reasoning, which is the only version of this worth using for anything that feeds a decision.

**Good for**

- Financial research
- Agent design
- Public comparables

**Limitations**

No licence file is present, so reuse terms are unclear. Depends on external APIs and an LLM key, and its answers need checking.

**Links:** [GitHub](https://github.com/virattt/dexter)

---

### AutoHedge

> A multi-agent system that runs a trading thesis end to end.

`The-Swarm-Corporation/AutoHedge` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Investment Analysis |
| **License** | MIT |
| **Stars** | 6k |
| **Forks** | 870 |
| **Language** | Python |
| **Status** | Active (last push 2026-05-11) |
| **Self-hostable** | yes |

**VC use case**

Worth reading as an architecture rather than deploying: it shows how to split a research question across an analyst, a risk reviewer, and an executor. That division of labour maps directly onto a diligence team.

**Why it's interesting**

The role separation is explicit, which is the useful idea. Single-agent financial tools tend to confuse analysis with decision.

**Good for**

- Agent architecture
- Internal tooling
- Research

**Limitations**

A demonstration, not an investment system, and anyone treating it as one deserves the result. Depends on market data APIs and model keys.

**Links:** [GitHub](https://github.com/The-Swarm-Corporation/AutoHedge) &nbsp;·&nbsp; [Site](https://swarms.xyz/)

---

### Prediction Market Analysis

> A framework and dataset for prediction market data.

`Jon-Becker/prediction-market-analysis` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; _dataset_

| | |
|---|---|
| **Category** | Investment Analysis |
| **License** | MIT |
| **Stars** | 3.8k |
| **Forks** | 539 |
| **Language** | Python |
| **Status** | Active (last push 2026-08-10) |
| **Self-hostable** | yes |

**VC use case**

Prediction markets price things that analysts only opine on: elections, rate moves, regulatory outcomes. This collects that data, so a thesis built on a political or macro assumption can be checked against a market price instead of a gut feel.

**Why it's interesting**

It publishes a real dataset alongside the collection code, which is unusual and means an analyst can start from data rather than from an empty pipeline.

**Good for**

- Macro research
- Forecast testing
- Dataset building

**Limitations**

Market prices reflect liquidity and sentiment, not truth, and thin markets are misleading. Coverage is limited to what the platforms list.

**Links:** [GitHub](https://github.com/Jon-Becker/prediction-market-analysis) &nbsp;·&nbsp; [Site](https://jbecker.dev/research/prediction-market-microstructure)

---
