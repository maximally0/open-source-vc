# Portfolio Management

_The decade after the wire hits._

Portfolio monitoring, KPI collection, dashboards, company updates, risk, analytics, and founder support.

**10 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-14

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

---

### Metabase

> Business intelligence that non-technical people can use.

`metabase/metabase` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Portfolio Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unverified (Other) |
| **Stars** | 49.2k |
| **Forks** | 6.8k |
| **Language** | Clojure |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | partial (open core) |

**VC use case**

Portfolio dashboards a partner will actually open: capital deployed by vintage, sector exposure, KPI collection across the book, and which companies are behind plan. Connects to the database where portfolio data already lives.

**Why it's interesting**

It is built so that someone who does not write SQL can ask a question and make a chart. For a fund, that is the difference between having a dashboard and having a dashboard nobody uses.

**Good for**

- Portfolio dashboards
- LP reporting
- KPI collection

**Limitations**

Visualization and embedded features sit behind a commercial tier. Needs a warehouse behind it and someone to keep the models right.

**Links:** [GitHub](https://github.com/metabase/metabase) &nbsp;·&nbsp; [Site](https://metabase.com)

---

### Streamlit

> Turn a Python script into a web app.

`streamlit/streamlit` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Portfolio Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 45.7k |
| **Forks** | 4.4k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | yes |

**VC use case**

The internal tool a fund builds once and uses daily: a company scorecard, an LP-return calculator, a portfolio KPI collector, a sourcing triage form. An analyst with Python writes it in an afternoon and it runs.

**Why it's interesting**

No front-end knowledge needed and no routing, styling, or deployment boilerplate. The speed from idea to something usable is why it became the default for internal data tools.

**Good for**

- Internal tools
- Portfolio dashboards
- Scorecards

**Limitations**

Not suited to large multi-user applications, and state handling gets awkward as an app grows. Recreating it in a real framework is often the eventual path.

**Dependencies:** Python 3.9+

**Links:** [GitHub](https://github.com/streamlit/streamlit) &nbsp;·&nbsp; [Site](https://streamlit.io)

---

### Apache Superset

> A full BI platform at Apache scale.

`apache/superset` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Portfolio Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 74.8k |
| **Forks** | 18.3k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | yes |

**VC use case**

The heavier option when a fund's data questions have outgrown a simple dashboard: SQL exploration, scheduled reports to LPs, row-level access so a partner sees only their deals. Runs on infrastructure a platform team already understands.

**Why it's interesting**

Apache governance and very broad database support mean it will still be here in a decade, which is what a fund should want from the layer holding its reporting.

**Good for**

- BI and reporting
- LP reporting
- Portfolio analytics

**Limitations**

Substantial deployment and a real learning curve. Overkill for a fund of one.

**Links:** [GitHub](https://github.com/apache/superset) &nbsp;·&nbsp; [Site](https://superset.apache.org/)

---

### Gradio

> Quick web interfaces for models and functions.

`gradio-app/gradio` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Portfolio Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 43.5k |
| **Forks** | 3.6k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | yes |

**VC use case**

When a fund wants to let colleagues try a scoring model, a classifier over inbound deals, or a document extractor, without anyone installing anything. Useful for getting feedback on an internal tool before investing in building it properly.

**Why it's interesting**

A working interface in a few lines, including file upload and streaming output, which makes it the fastest way to show a non-technical colleague what a model does.

**Good for**

- Model demos
- Internal tools
- Prototyping

**Limitations**

Demo-oriented: authentication, access control, and state are limited. Not a production application framework.

**Links:** [GitHub](https://github.com/gradio-app/gradio) &nbsp;·&nbsp; [Site](http://www.gradio.app)

---

### Directus

> An admin layer over any SQL database.

`directus/directus` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Portfolio Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | unverified (Other) |
| **Stars** | 37.9k |
| **Forks** | 4.9k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | partial (open core) |

**VC use case**

When a fund needs a real internal system, portfolio data entry, document records, deal workflow, without building a back end, this puts a usable interface and API on top of a database the platform team already runs.

**Why it's interesting**

It sits on your existing database rather than creating its own, so the data stays portable and queryable by everything else you run.

**Good for**

- Internal systems
- Data entry
- Portfolio data

**Limitations**

Licence is not a standard SPDX identifier, with commercial tiers for some features. More engineering than a spreadsheet replacement warrants.

**Links:** [GitHub](https://github.com/directus/directus) &nbsp;·&nbsp; [Site](https://directus.com)

---

### Redash

> Query, visualize, and share data quickly.

`getredash/redash` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Portfolio Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | BSD-2-Clause |
| **Stars** | 28.8k |
| **Forks** | 4.6k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-03) |
| **Self-hostable** | yes |

**VC use case**

The middle ground: write SQL against the portfolio database, save the query, put a chart on it, share the link. Fast enough that an analyst does not have to file a request with anyone.

**Why it's interesting**

It prioritises time-to-first-answer over modelling depth, which matches how analysts actually work when a partner asks a question mid-meeting.

**Good for**

- Ad-hoc analysis
- Portfolio analytics
- Internal reporting

**Limitations**

Development is slower than it once was, and it is less suited to governed reporting than the larger BI platforms.

**Links:** [GitHub](https://github.com/getredash/redash) &nbsp;·&nbsp; [Site](http://redash.io/)

---

### Datasette

> Publish any database as a browsable, queryable site.

`simonw/datasette` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Portfolio Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 11.5k |
| **Forks** | 902 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

Publish the portfolio database internally so anyone can browse companies, filter by sector, and run their own queries without asking an engineer. Also useful for shipping a dataset alongside a memo so a partner can check the numbers themselves.

**Why it's interesting**

It turns a database file into an explorable interface with almost no work, including a JSON API, so the same thing serves humans and scripts.

**Good for**

- Internal data access
- Portfolio data
- Data publishing

**Limitations**

Read-oriented: not an editing interface or a reporting suite. Needs care around permissions if the data is sensitive.

**Links:** [GitHub](https://github.com/simonw/datasette) &nbsp;·&nbsp; [Site](https://datasette.io)

---

### Baserow

> An open Airtable for structured portfolio data.

`baserow/baserow` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Portfolio Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unverified (Other) |
| **Stars** | 5.9k |
| **Forks** | 723 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | partial (open core) |

**VC use case**

Where the portfolio KPI collection actually lands: one row per company, columns for the metrics a fund tracks, forms for founders to submit updates, and a view per partner. Structured enough to report from, simple enough that nobody needs training.

**Why it's interesting**

It handles the unglamorous part of portfolio monitoring, which is getting consistent data out of founders every quarter without a spreadsheet arriving in four formats.

**Good for**

- KPI collection
- Portfolio tracking
- Company updates

**Limitations**

Advanced features and some integrations are commercial. Large bases need proper database tuning.

**Links:** [GitHub](https://github.com/baserow/baserow) &nbsp;·&nbsp; [Site](https://baserow.io)

---

### ROAPI

> Serve any dataset as an API without writing code.

`roapi/roapi` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Portfolio Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 3.4k |
| **Forks** | 209 |
| **Language** | Rust |
| **Status** | Active (last push 2026-03-25) |
| **Self-hostable** | yes |

**VC use case**

Point it at a CSV or Parquet file of portfolio or market data and get a queryable API. Useful for the awkward middle stage where a fund has data in files and needs a dashboard or a script to read it.

**Why it's interesting**

It removes the write-a-service step entirely, which is the step that stops small teams from shipping internal tools.

**Good for**

- Internal APIs
- Data access
- Prototyping

**Limitations**

Read-only and not a database: no transactions, no complex writes. Fine for serving datasets, wrong for a system of record.

**Links:** [GitHub](https://github.com/roapi/roapi) &nbsp;·&nbsp; [Site](https://roapi.github.io/docs)

---

### Runway Tool

> Runway and cash-budget forecasting for a startup.

`tdavidson/runway-tool` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◆ **VC-native** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Portfolio Management |
| **VC relevance** | VC-native — built for venture capital, private markets, fund operations, or startup investing. |
| **License** | unverified (Other) |
| **Stars** | 16 |
| **Forks** | 2 |
| **Language** | unknown |
| **Status** | Dormant (last push 2020-10-12, 71mo) |
| **Self-hostable** | yes |

**VC use case**

The single number a board watches: how many months of cash remain, under what hiring and spend assumptions. This models the scenario, which is what a fund needs when a portfolio company's bridge question arrives two months earlier than planned.

**Why it's interesting**

Almost no open-source tooling exists for this, despite it being the most-asked portfolio question. It is a small model someone who understood the problem released.

**Good for**

- Runway monitoring
- Portfolio support
- Board reporting

**Limitations**

Small project that has not been touched since 2020, and the licence is not a standard SPDX identifier. Read it as a model to adapt rather than a maintained tool.

**Links:** [GitHub](https://github.com/tdavidson/runway-tool) &nbsp;·&nbsp; [Site](https://foresight.is/runway-cash-forecasting)

---
