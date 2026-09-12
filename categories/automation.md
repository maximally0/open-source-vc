# Workflow & Automation

_Glue. Unglamorous, and the difference between a stack and a folder of scripts._

Workflow automation, ETL, connectors, notifications, integrations, scheduled research, and chat/email automation.

**12 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-12

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

---

### n8n

> Workflow automation with a fair-code licence.

`n8n-io/n8n` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Workflow & Automation |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | unverified (Other) |
| **Stars** | 204.1k |
| **Forks** | 60.6k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | partial (open core) |

**VC use case**

The connective tissue a fund needs: a new deal lands in a form, gets enriched, appears in the pipeline, and pings the right partner. Replaces the Zapier subscription and the folder of cron scripts nobody documented.

**Why it's interesting**

It has the widest integration catalogue in open automation and a visual editor that a non-engineer can extend. Also worth studying as a licensing model rather than a licence: the source is public, redistribution is restricted, and it is not open source.

**Good for**

- Workflow automation
- Deal routing
- Notifications

**Limitations**

Not open source despite the description people give it: the fair-code licence restricts commercial redistribution and hosting. Some nodes are enterprise-only.

**Links:** [GitHub](https://github.com/n8n-io/n8n) &nbsp;·&nbsp; [Site](https://n8n.io)

---

### Apache Airflow

> The default scheduler for data pipelines.

`apache/airflow` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Workflow & Automation |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 46.8k |
| **Forks** | 17.8k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

When a fund's data work becomes real: nightly collection jobs, enrichment pipelines, and reports that have to run in order and tell someone when they fail. The standard answer, with people who know it available to hire.

**Why it's interesting**

Apache governance, enormous adoption, and a connector ecosystem that covers almost any source. Its age is the point: the failure modes are known.

**Good for**

- Data pipelines
- Scheduled research
- Reporting

**Limitations**

Heavy for small jobs and a real operational commitment. Not the tool for two scripts and a deadline.

**Links:** [GitHub](https://github.com/apache/airflow) &nbsp;·&nbsp; [Site](https://airflow.apache.org/)

---

### ToolJet

> Another drag-and-drop internal tool builder.

`ToolJet/ToolJet` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Workflow & Automation |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | AGPL-3.0 |
| **Stars** | 40.9k |
| **Forks** | 5.4k |
| **Language** | JavaScript |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | partial (open core) |

**VC use case**

The same job as Appsmith with a different data model and a wider self-hosting story. Worth evaluating alongside it rather than picking blind, since internal tool builders are hard to migrate off.

**Why it's interesting**

Broad database and API connectivity, and a stronger default for self-hosting, which matters when the tool holds portfolio data.

**Good for**

- Internal tools
- Data entry
- Admin panels

**Limitations**

AGPL-licensed with commercial editions. Same ceiling as any visual builder when logic grows.

**Links:** [GitHub](https://github.com/ToolJet/ToolJet) &nbsp;·&nbsp; [Site](https://tooljet.com)

---

### Appsmith

> Build internal tools by dragging components.

`appsmithorg/appsmith` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Workflow & Automation |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 40.9k |
| **Forks** | 4.8k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | partial (open core) |

**VC use case**

The internal screens a fund ends up needing: a deal review form, a portfolio data entry page, an admin view over the pipeline. Built by the person who understands the process rather than by an engineer.

**Why it's interesting**

It connects to a real database and lets someone assemble a usable app in an afternoon, which is usually faster than specifying it properly.

**Good for**

- Internal tools
- Data entry
- Portfolio data

**Limitations**

Complex logic gets awkward, and the resulting app is harder to test and version than code. Some features are commercial.

**Links:** [GitHub](https://github.com/appsmithorg/appsmith) &nbsp;·&nbsp; [Site](https://www.appsmith.com)

---

### Kestra

> Declarative orchestration in YAML.

`kestra-io/kestra` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Workflow & Automation |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 28.1k |
| **Forks** | 3k |
| **Language** | Java |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

For recurring data work a fund runs on a schedule: pulling filings, refreshing a portfolio database, generating a weekly digest. Workflows are declared in files, so they can be reviewed and versioned like everything else.

**Why it's interesting**

Declarative YAML orchestration with a large plugin catalogue, and because it is Apache-licensed the extension story is not gated.

**Good for**

- Scheduled research
- Data pipelines
- Reporting

**Limitations**

Another service to operate, and for a handful of jobs a cron file is honestly enough.

**Links:** [GitHub](https://github.com/kestra-io/kestra) &nbsp;·&nbsp; [Site](https://go.kestra.io/home)

---

### Activepieces

> An open Zapier alternative.

`activepieces/activepieces` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Workflow & Automation |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | unverified (Other) |
| **Stars** | 24.4k |
| **Forks** | 4.2k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | partial (open core) |

**VC use case**

The same job as n8n with a licence that keeps redistribution options open. Where a fund or a portfolio company wants automation without the restrictions of a fair-code product.

**Why it's interesting**

It is closer to genuinely open, and it includes AI steps, which is where a lot of internal automation now starts.

**Good for**

- Workflow automation
- Integrations
- Internal tools

**Limitations**

Licence is not a standard SPDX identifier and follows a similar open-core shape. Fewer integrations than n8n.

**Links:** [GitHub](https://github.com/activepieces/activepieces) &nbsp;·&nbsp; [Site](https://www.activepieces.com)

---

### Prefect

> Python-native workflow orchestration.

`PrefectHQ/prefect` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Workflow & Automation |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 23.8k |
| **Forks** | 2.5k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

The middle ground for an analyst who writes Python and needs reliable scheduled jobs without learning a platform: decorate a function, add retries and schedules, and it runs.

**Why it's interesting**

It works with plain Python rather than requiring a DSL, so the pipeline stays readable and testable by the person who wrote the analysis.

**Good for**

- Scheduled jobs
- Data pipelines
- Reporting

**Limitations**

The managed product is the commercial focus, so some operational features are easier with it. Less suited to very large dependency graphs.

**Links:** [GitHub](https://github.com/PrefectHQ/prefect) &nbsp;·&nbsp; [Site](https://prefect.io)

---

### Airbyte

> Connectors that move data from anywhere to anywhere.

`airbytehq/airbyte` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Workflow & Automation |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | unverified (Other) |
| **Stars** | 22k |
| **Forks** | 5.3k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | partial (open core) |

**VC use case**

The ingestion layer: get data out of a CRM, a billing system, an accounting package, or a portfolio company's tooling and into the fund's own database. Removes the custom connector that somebody has to maintain every time an API changes.

**Why it's interesting**

The connector catalogue is the asset, with hundreds of sources, and it is the most complete open option for this job.

**Good for**

- Data ingestion
- Portfolio data
- Internal platforms

**Limitations**

Open-core with some connectors and features commercial, and the licence is not a standard SPDX identifier. Running it is a real service.

**Links:** [GitHub](https://github.com/airbytehq/airbyte) &nbsp;·&nbsp; [Site](https://airbyte.com)

---

### Windmill

> Turn scripts into workflows and internal apps.

`windmill-labs/windmill` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Workflow & Automation |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | unverified (Other) |
| **Stars** | 17.9k |
| **Forks** | 1.1k |
| **Language** | Rust |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | partial (open core) |

**VC use case**

Where a fund's ad-hoc Python scripts become something the team can run: a sourcing script, an enrichment job, a report generator, each with a form and a schedule. Keeps the code as code while giving non-engineers a way to run it.

**Why it's interesting**

It starts from scripts rather than from a visual builder, so it does not force complex logic into boxes. The generated UI on top of a script is the useful part.

**Good for**

- Internal tooling
- Scheduled jobs
- Data pipelines

**Limitations**

Licence is not a standard SPDX identifier. Steeper start than a visual-first tool for someone who does not write code.

**Links:** [GitHub](https://github.com/windmill-labs/windmill) &nbsp;·&nbsp; [Site](https://windmill.dev)

---

### Dagster

> Orchestration built around data assets.

`dagster-io/dagster` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Workflow & Automation |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 16.1k |
| **Forks** | 2.3k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

A pipeline where you care about the state of the data rather than the order of tasks: refreshing a company record when any of its sources change, and knowing which downstream tables are now stale. Useful for a portfolio dataset with many inputs.

**Why it's interesting**

Modelling pipelines as assets rather than tasks answers questions like what depends on this table and what broke when it changed, which schedulers alone do not.

**Good for**

- Data pipelines
- Portfolio data
- Data quality

**Limitations**

More concepts to learn than a task scheduler, and the value appears only once the data model is worth the effort.

**Links:** [GitHub](https://github.com/dagster-io/dagster) &nbsp;·&nbsp; [Site](https://dagster.io)

---

### dbt

> Transform data with SQL that is tested and documented.

`dbt-labs/dbt` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Workflow & Automation |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 13.8k |
| **Forks** | 2.6k |
| **Language** | Rust |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

Turns a fund's raw company and portfolio tables into the clean models that reporting depends on, with tests that catch a broken number before it reaches a partner. The discipline that separates a spreadsheet habit from a data practice.

**Why it's interesting**

It brings software engineering practice, version control, tests, documentation, and code review, to SQL transformations, and it has become the standard way to do it.

**Good for**

- Data modelling
- Reporting
- Data quality

**Limitations**

SQL-based, so non-tabular work needs something else. Needs a warehouse and someone who understands the business logic.

**Links:** [GitHub](https://github.com/dbt-labs/dbt) &nbsp;·&nbsp; [Site](https://getdbt.com)

---

### Meltano

> ELT as code with version control.

`meltano/meltano` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Workflow & Automation |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 2.6k |
| **Forks** | 268 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

The lighter, declarative alternative to Airbyte when a fund needs a handful of sources: extract and load as configuration in a repository, so the pipeline is reviewable and reproducible.

**Why it's interesting**

Configuration-as-code means the pipeline is diffable and can be reviewed, which is what makes data work maintainable by a small team.

**Good for**

- Data ingestion
- Internal platforms
- Reporting

**Limitations**

Fewer connectors than Airbyte and more assembly required. Smaller community.

**Links:** [GitHub](https://github.com/meltano/meltano) &nbsp;·&nbsp; [Site](https://meltano.com/)

---
