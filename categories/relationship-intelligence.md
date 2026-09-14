# Relationship Intelligence

_The actual moat in venture is the network._

CRMs, personal CRMs, relationship graphs, email and calendar intelligence, warm-introduction paths, and network analysis.

**13 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-14

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

---

### Twenty

> A modern open CRM with a customisable data model.

`twentyhq/twenty` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Relationship Intelligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unverified (Other) |
| **Stars** | 56.7k |
| **Forks** | 9.1k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | partial (open core) |

**VC use case**

The team version: contacts, companies, and opportunities that match how a fund works, in a shared system rather than four analysts' personal notes. Useful for a fund that wants CRM ownership without a per-seat contract.

**Why it's interesting**

The data model is editable, so a fund can model its own stages and relationship types instead of bending to a vendor's schema. It reads as a modern product rather than an ageing open-source CRM.

**Good for**

- Team CRM
- Deal tracking
- Relationship records

**Limitations**

Younger than the established open CRMs, so the integration catalogue is smaller. Some features sit behind a hosted commercial tier, and the licence is not a standard SPDX identifier.

**Links:** [GitHub](https://github.com/twentyhq/twenty) &nbsp;·&nbsp; [Site](https://twenty.com)

---

### Cal.com

> Scheduling that you host yourself.

`calcom/cal.diy` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Relationship Intelligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 48.4k |
| **Forks** | 15.1k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | yes |

**VC use case**

Founder calls, LP check-ins, and office hours all live or die on scheduling. This gives a fund one booking surface with routing, buffers, and per-person availability, without another SaaS subscription holding the calendar data.

**Why it's interesting**

It is a direct Calendly replacement with self-hosting, which matters when the calendar entries include unannounced deals. It also has a real API, so bookings can feed the CRM.

**Good for**

- Meeting scheduling
- Founder calls
- LP relations

**Limitations**

Self-hosted updates are your responsibility, and the most advanced team features are commercial. Some calendar providers have quirks that need working around.

**Links:** [GitHub](https://github.com/calcom/cal.diy) &nbsp;·&nbsp; [Site](https://cal.diy)

---

### Monica

> A personal CRM for the relationships a fund actually runs on.

`monicahq/monica` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Relationship Intelligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | AGPL-3.0 |
| **Stars** | 25.3k |
| **Forks** | 2.6k |
| **Language** | PHP |
| **Status** | Active (last push 2026-04-24) |
| **Self-hostable** | yes |

**VC use case**

Every investor keeps the same private list: who introduced whom, what they care about, when you last spoke, what you promised. Monica holds that per person, including conversations, reminders, and how you know them. For a scout or an angel with hundreds of loose ties, this is the difference between a network and a contact list.

**Why it's interesting**

It is built around the relationship rather than the deal, with reminders to stay in touch and free-form notes on family, interests, and history. That is exactly the context that gets lost when a deal pipeline becomes the system of record.

**Good for**

- Personal network management
- Warm introductions
- Founder relationships

**Limitations**

Single-user personal CRM, not a team pipeline: no shared ownership, no deal stages. Self-hosting means you own the backups.

**Links:** [GitHub](https://github.com/monicahq/monica) &nbsp;·&nbsp; [Site](https://beta.monicahq.com)

---

### Whisper

> Speech to text that holds up on real calls.

`openai/whisper` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Relationship Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 109.1k |
| **Forks** | 13.2k |
| **Language** | Python |
| **Status** | Active (last push 2026-08-31) |
| **Self-hostable** | yes |

**VC use case**

Turn founder calls into a transcript you can search, quote in a memo, and keep as part of the record. A fund takes hundreds of calls a year and remembers almost none of the detail.

**Why it's interesting**

It handles accents, background noise, and switching between languages in a way that makes transcription usable for something important, and it runs locally so confidential calls do not need to leave your machine.

**Good for**

- Call transcripts
- Institutional memory
- Memo evidence

**Limitations**

Needs a GPU for practical speed on long recordings, and no speaker separation: you get a wall of text unless you pair it with a diarisation tool.

**Links:** [GitHub](https://github.com/openai/whisper)

---

### Odoo

> An open business suite covering CRM, accounting, invoicing, and projects.

`odoo/odoo` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Relationship Intelligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unverified (Other) |
| **Stars** | 54.3k |
| **Forks** | 33.7k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | partial (open core) |

**VC use case**

For a small fund or an SPV, the unglamorous back office in one system: contacts, invoices, expenses, and basic accounting. Funds that outgrow spreadsheets often land here because the accounting and CRM share a database.

**Why it's interesting**

It covers the parts of running a fund vehicle that no CRM does, and every module writes to the same data model, which removes a class of reconciliation work.

**Good for**

- Fund back office
- SPV administration
- CRM

**Limitations**

Community edition is open source, but the most useful modules are enterprise-only. Deploying and maintaining it is a genuine operations job.

**Links:** [GitHub](https://github.com/odoo/odoo) &nbsp;·&nbsp; [Site](https://www.odoo.com)

---

### Meetily

> A self-hosted AI meeting assistant.

`Zackriya-Solutions/meetily` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Relationship Intelligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 30.7k |
| **Forks** | 3.3k |
| **Language** | Rust |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | yes |

**VC use case**

The meeting-intelligence layer a fund actually needs: transcribe founder calls and partner meetings locally, produce notes, and keep the record without sending audio to a cloud service. Investment discussions involve unannounced deals and other people's confidential information.

**Why it's interesting**

It runs locally with fast local models, which is the requirement that rules out the commercial meeting assistants for most funds. Speaker separation and summaries without a per-seat subscription.

**Good for**

- Meeting records
- Call transcripts
- IC preparation

**Limitations**

Local transcription needs decent hardware, and accuracy trails a hosted service. Recording calls still requires consent and disclosure in many jurisdictions.

**Links:** [GitHub](https://github.com/Zackriya-Solutions/meetily) &nbsp;·&nbsp; [Site](https://meetily.ai)

---

### faster-whisper

> Whisper transcription at several times the speed.

`SYSTRAN/faster-whisper` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Relationship Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 25.4k |
| **Forks** | 2.1k |
| **Language** | Python |
| **Status** | Active (last push 2025-11-19) |
| **Self-hostable** | yes |

**VC use case**

What makes transcribing every call practical rather than aspirational. If a fund wants all founder calls searchable, the limiting factor is throughput, and this is the fix.

**Why it's interesting**

A reimplementation on a faster inference engine with lower memory use, so a queue of call recordings can be processed on modest hardware.

**Good for**

- Batch transcription
- Call archives
- Institutional memory

**Limitations**

Same accuracy profile as Whisper, including the lack of speaker separation. Needs the underlying inference runtime installed.

**Links:** [GitHub](https://github.com/SYSTRAN/faster-whisper)

---

### WhisperX

> Transcription with word timings and speaker labels.

`m-bain/whisperX` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Relationship Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | BSD-2-Clause |
| **Stars** | 24k |
| **Forks** | 2.4k |
| **Language** | Python |
| **Status** | Active (last push 2026-08-30) |
| **Self-hostable** | yes |

**VC use case**

The version you want for investment committee: a transcript that shows who said what and when. When a founder's claim gets discussed three months later, knowing which person made it matters.

**Why it's interesting**

It adds speaker diarisation and accurate word-level timestamps on top of Whisper, which turns a transcript into something closer to a minute-by-minute record.

**Good for**

- Meeting records
- IC preparation
- Evidence trails

**Limitations**

More setup than plain Whisper, and diarisation degrades when several people speak at once or the audio is poor.

**Links:** [GitHub](https://github.com/m-bain/whisperX)

---

### Krayin CRM

> A lightweight CRM on Laravel.

`krayin/laravel-crm` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Relationship Intelligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 23.9k |
| **Forks** | 1.6k |
| **Language** | PHP |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | yes |

**VC use case**

A fund or platform team already working in PHP can have a working CRM with leads, quotes, and activities on day one, and modify it without fighting a framework.

**Why it's interesting**

MIT licensed with no open-core split, which is unusual in this category and makes it straightforward to extend and redistribute.

**Good for**

- Team CRM
- Custom CRM builds

**Limitations**

Smaller community than the established CRMs, and fewer integrations out of the box.

**Links:** [GitHub](https://github.com/krayin/laravel-crm) &nbsp;·&nbsp; [Site](https://krayincrm.com)

---

### NetworkX

> Graph analysis in plain Python.

`networkx/networkx` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Relationship Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | unverified (Other) |
| **Stars** | 17.3k |
| **Forks** | 3.6k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

The warm-introduction question that every fund asks and almost none can answer systematically: which of our contacts is closest to this founder, and through whom. Model people and companies as a graph and NetworkX computes the shortest paths instead of you asking around.

**Why it's interesting**

Co-investment graphs, board interlocks, and founder networks are all the same problem, and this is the standard tool for it. It needs no database and no infrastructure.

**Good for**

- Warm introduction paths
- Network analysis
- Co-investment mapping

**Limitations**

In-memory, so very large graphs need more than networkx. You have to build and maintain the graph yourself; the quality of the answer depends entirely on the data you feed it.

**Dependencies:** Python 3.10+

**Links:** [GitHub](https://github.com/networkx/networkx) &nbsp;·&nbsp; [Site](https://networkx.org)

---

### Frappe CRM

> A CRM built on the Frappe framework.

`frappe/crm` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Relationship Intelligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | AGPL-3.0 |
| **Stars** | 3.5k |
| **Forks** | 1.4k |
| **Language** | Vue |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | yes |

**VC use case**

A maintainable team CRM for a small fund, with the option to extend into the wider Frappe and ERPNext stack later for invoicing, support, or portfolio administration. That path matters for emerging managers who will need more than a CRM in two years.

**Why it's interesting**

Sitting on Frappe means the data model and permissions are configurable from a framework rather than a plugin system, and the same stack covers other back-office needs.

**Good for**

- Team CRM
- Fund back office
- Relationship records

**Limitations**

Frappe's conventions take learning if your team is not already on that stack. Smaller feature set than dedicated CRMs.

**Links:** [GitHub](https://github.com/frappe/crm) &nbsp;·&nbsp; [Site](https://frappe.io/crm)

---

### EspoCRM

> A long-lived open CRM with a mature extension model.

`espocrm/espocrm` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Relationship Intelligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | AGPL-3.0 |
| **Stars** | 3.3k |
| **Forks** | 970 |
| **Language** | PHP |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | yes |

**VC use case**

The conservative choice for a fund that wants a CRM to still be maintained in five years: contacts, accounts, and opportunities with workflow and reporting, plus a large catalogue of community extensions for the gaps.

**Why it's interesting**

Years of releases and a stable extension API. Boring, in the sense that matters for a system that will hold a decade of relationship history.

**Good for**

- Team CRM
- Relationship records
- Reporting

**Limitations**

Interface and design show their age, and the most capable extensions are paid.

**Links:** [GitHub](https://github.com/espocrm/espocrm) &nbsp;·&nbsp; [Site](https://www.espocrm.com)

---

### CiviCRM

> A constituent relationship system built for mission-driven organisations.

`civicrm/civicrm-core` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Relationship Intelligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | AGPL-3.0 |
| **Stars** | 772 |
| **Forks** | 898 |
| **Language** | PHP |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | yes |

**VC use case**

Purpose-built for relationship-heavy organisations that track people over decades: relevant to impact funds, foundations, and family offices where the relationship is the asset and money is not the only axis being tracked.

**Why it's interesting**

It models contributions, memberships, and relationships natively, which commercial sales CRMs handle badly. Two decades of development behind it.

**Good for**

- Impact funds
- Foundation relationships
- Grant tracking

**Limitations**

Dated interface, and the data model assumes nonprofit workflows, so a conventional fund would be forcing it. Deployment is substantial.

**Links:** [GitHub](https://github.com/civicrm/civicrm-core)

---
