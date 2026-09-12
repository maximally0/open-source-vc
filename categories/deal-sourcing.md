# Deal Sourcing & Pipeline

_Track, dedupe, and route opportunities without a $50k seat licence._

Sourcing workflow, pipeline management, deduplication, and routing.

**6 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-12

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

**Coverage note.** Deal-flow tooling splits cleanly in two, and open source only covers one half. The generic half, monitoring, change detection, databases, and notification, is well served and listed here. The specific half, the compiled private-company graphs where most sourcing actually happens, is entirely commercial. Expect to combine these tools with a paid data source rather than replacing it.

---

### NocoDB

> Airtable-style database over Postgres, MySQL, or SQLite.

`nocodb/nocodb` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Deal Sourcing & Pipeline |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unverified (Other) |
| **Stars** | 64.9k |
| **Forks** | 5k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

The deals pipeline most small funds actually need: stages, owners, next actions, and notes, as a grid anyone on the team can edit, sitting on a real database you control. It replaces a spreadsheet that has grown past what a spreadsheet can hold.

**Why it's interesting**

It puts a collaborative grid on top of your existing database instead of creating another silo, so the pipeline stays queryable by the tools you already run.

**Good for**

- Deal pipelines
- Portfolio tracking
- Internal tools

**Limitations**

Advanced features sit behind a commercial tier, and the licence is not a standard open-source one. Large bases need real database tuning.

**Links:** [GitHub](https://github.com/nocodb/nocodb) &nbsp;·&nbsp; [Site](https://nocodb.com)

---

### changedetection.io

> Tell me when a specific page changes.

`dgtlmoon/changedetection.io` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Deal Sourcing & Pipeline |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 33.8k |
| **Forks** | 2k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

The narrow version of monitoring and the one analysts actually need: a competitor drops a price, adds a plan, edits a terms page, or a portfolio company quietly reshuffles its team page. This watches the page and says so.

**Why it's interesting**

It handles the parts that make naive diffing useless, including JavaScript-rendered pages and selecting only the region you care about, so it does not alert on a rotating banner.

**Good for**

- Competitor monitoring
- Portfolio monitoring
- Regulatory tracking

**Limitations**

Some features are behind a paid hosted tier, and a busy page still needs selector tuning. Notification plumbing is yours to set up.

**Links:** [GitHub](https://github.com/dgtlmoon/changedetection.io) &nbsp;·&nbsp; [Site](https://changedetection.io)

---

### Huginn

> Agents that watch the web and act when something changes.

`huginn/huginn` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Deal Sourcing & Pipeline |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 49.9k |
| **Forks** | 4.3k |
| **Language** | Ruby |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

Set up watchers on the sites a thesis depends on: a competitor's pricing page, a job board for a specific role, a regulator's filing list. When something changes, Huginn notifies or triggers a downstream action, so sourcing runs on its own.

**Why it's interesting**

It is a general event-and-action engine with years of accumulated integrations, which means almost any public page can become a signal source with no code.

**Good for**

- Watchlist automation
- Signal monitoring
- Scheduled research

**Limitations**

Dated interface, and the self-hosted install has real operational weight. Agents break quietly when a source page changes its markup.

**Links:** [GitHub](https://github.com/huginn/huginn)

---

### Dub

> Link attribution and inbound source tracking.

`dubinc/dub` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Deal Sourcing & Pipeline |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unverified (Other) |
| **Stars** | 24.7k |
| **Forks** | 3.3k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | partial (open core) |

**VC use case**

A fund running a newsletter, a scout programme, or an event funnel wants to know which inbound deals came from where. Short links with attribution turn "we get deal flow" into a number per channel.

**Why it's interesting**

Attribution is normally the weak point in a fund's own funnel. Having it in an open tool means the pipeline can be read programmatically instead of trusted as folklore.

**Good for**

- Inbound sourcing
- Scout programmes
- Channel attribution

**Limitations**

The core is open source with a hosted commercial product on top, and some analytics features are paid. Self-hosting requires a database and infrastructure.

**Links:** [GitHub](https://github.com/dubinc/dub) &nbsp;·&nbsp; [Site](https://dub.co)

---

### ExecSum Deal Brief

> A daily deal-flow brief with a ranked top three.

`kklounge/execsum-deal-brief` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◆ **VC-native** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Deal Sourcing & Pipeline |
| **VC relevance** | VC-native — built for venture capital, private markets, fund operations, or startup investing. |
| **License** | MIT |
| **Stars** | 50 |
| **Forks** | 0 |
| **Language** | Python |
| **Status** | Active (last push 2026-08-14) |
| **Self-hostable** | yes |

**VC use case**

Assembles a morning brief that ranks the day's deals and attaches expert and banking commentary. The use case is a partner's inbox at 7am: what moved, and what deserves a look, without anyone compiling it.

**Why it's interesting**

It ranks rather than lists, which is the part most monitoring tools skip. Ranking is where the judgement goes, so it is worth reading the code to see how it decides.

**Good for**

- Daily briefings
- Deal-flow triage
- Partner communication

**Limitations**

Depends on external news and data sources that may change or require keys, and the ranking logic is simple enough to disagree with. Small project.

**Links:** [GitHub](https://github.com/kklounge/execsum-deal-brief)

---

### subsignal

> Deal-flow monitoring built for funds.

`0xnyn/subsignal` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◆ **VC-native** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Deal Sourcing & Pipeline |
| **VC relevance** | VC-native — built for venture capital, private markets, fund operations, or startup investing. |
| **License** | unknown |
| **Stars** | 29 |
| **Forks** | 6 |
| **Language** | TypeScript |
| **Status** | Active (last push 2025-10-18) |
| **Self-hostable** | yes |

**VC use case**

Watches company and competitor signals so an analyst does not have to check the same sites weekly: new products, pricing changes, launches. The intended output is a shortlist of companies whose activity changed, which is the raw material of outbound sourcing.

**Why it's interesting**

It is one of very few projects written for investors rather than adapted from a general monitoring tool, so the event model matches how a fund actually tracks a watchlist.

**Good for**

- Outbound sourcing
- Watchlist monitoring
- Competitive intelligence

**Limitations**

Early-stage with a small maintainer base, and no licence file is present, so terms for reuse are unclear. Expect to write your own connectors.

**Links:** [GitHub](https://github.com/0xnyn/subsignal) &nbsp;·&nbsp; [Site](https://subsignal.vc)

---
