# Due Diligence

_Replace the manual checklist with something repeatable._

Financial, commercial, technical, legal, product, and AI/ML diligence, plus customer and competitive research.

**10 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-12

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

---

### PaperQA

> Answers questions from scientific documents with citations.

`Future-House/paper-qa` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Due Diligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 9.2k |
| **Forks** | 917 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-07) |
| **Self-hostable** | yes |

**VC use case**

Technical diligence on a deep-tech company: read the founders' papers and patents, then ask whether the claimed result holds up, with page-level citations. For a biotech or materials deal, this is how a generalist gets oriented before the expert call.

**Why it's interesting**

It is built for the case where the answer must be traceable to a specific passage, and it reports what the literature does and does not agree on rather than flattening disagreement.

**Good for**

- Technical due diligence
- Deep-tech research
- Literature review

**Limitations**

Needs the source documents and an LLM key, and it will still miss domain context an expert would bring. Citations need opening.

**Links:** [GitHub](https://github.com/Future-House/paper-qa) &nbsp;·&nbsp; [Site](https://futurehouse.gitbook.io/futurehouse-cookbook)

---

### Label Studio

> A flexible interface for labelling and annotating data.

`HumanSignal/label-studio` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Due Diligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 28.3k |
| **Forks** | 3.7k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | partial (open core) |

**VC use case**

Customer research and commercial diligence often mean reading a hundred support tickets, reviews, or contracts and coding them consistently. This gives a team a shared labelling interface instead of a shared spreadsheet, and the counts that come out are defensible.

**Why it's interesting**

It supports text, images, audio, and video with configurable label schemas, so the same tool covers a support-ticket study and a product-teardown exercise.

**Good for**

- Customer research
- Commercial due diligence
- Data preparation

**Limitations**

Cloud features and collaboration sit behind a commercial tier. Setting it up for a one-off study is more work than the study.

**Links:** [GitHub](https://github.com/HumanSignal/label-studio) &nbsp;·&nbsp; [Site](https://labelstud.io)

---

### Cleanlab

> Finds label errors and bad rows in a dataset.

`cleanlab/cleanlab` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Due Diligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 11.7k |
| **Forks** | 920 |
| **Language** | Python |
| **Status** | Active (last push 2026-01-13) |
| **Self-hostable** | yes |

**VC use case**

A target claims its model works because of proprietary data. This tells you how much of that data is mislabelled or duplicated, which is often the real explanation for performance. It also applies to a fund's own data before it builds anything on it.

**Why it's interesting**

It works with any model and no clean reference set, using prediction disagreement to rank likely errors. That is what makes it usable on someone else's data.

**Good for**

- AI due diligence
- Data quality
- Technical diligence

**Limitations**

It ranks suspicious rows; someone still has to judge them. Findings on a small dataset are noisy.

**Links:** [GitHub](https://github.com/cleanlab/cleanlab) &nbsp;·&nbsp; [Site](https://cleanlab.ai)

---

### Phoenix

> Observability and evaluation for models in production.

`Arize-ai/phoenix` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Due Diligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unverified (Other) |
| **Stars** | 11.4k |
| **Forks** | 1.1k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

Ask a target to show you traces of its model in production: what users asked, what the model answered, where it failed. This is the closest thing to a live technical audit of an AI product, and it is a much better conversation than a demo.

**Why it's interesting**

It works on local traces with no account required, so a diligence session can happen on the target's own infrastructure rather than through a vendor's dashboard.

**Good for**

- AI due diligence
- Production review
- Portfolio monitoring

**Limitations**

Requires the target to instrument its system, so a fund cannot use it unilaterally. The hosted platform is the commercial product.

**Links:** [GitHub](https://github.com/Arize-ai/phoenix) &nbsp;·&nbsp; [Site](https://arize.com/docs/phoenix)

---

### doccano

> Simple text annotation for classification and extraction.

`doccano/doccano` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Due Diligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 10.8k |
| **Forks** | 1.8k |
| **Language** | Python |
| **Status** | Active (last push 2026-04-14) |
| **Self-hostable** | yes |

**VC use case**

When a diligence finding needs a number rather than an impression, such as how many of a target's contracts contain an unusual termination clause, someone has to read them all consistently. This is the lightest tool for that job.

**Why it's interesting**

Quick to stand up, with roles and review built in, so two analysts can divide a reading task and produce one count.

**Good for**

- Contract review
- Customer research
- Evidence counting

**Limitations**

Text-focused, so it will not help with tables or images. Older project, with a dated interface.

**Links:** [GitHub](https://github.com/doccano/doccano)

---

### LangWatch

> Evaluation and testing for agents and LLM features.

`langwatch/langwatch` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Due Diligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 3.5k |
| **Forks** | 370 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

The diligence question for any AI-native company is whether the product actually works when inputs vary. This provides test suites and scoring, so a technical reviewer can check the claim rather than take the benchmark slide's word for it.

**Why it's interesting**

It handles agent traces as well as single calls, which is where the failures in agentic products actually happen and where simple evals miss them.

**Good for**

- AI due diligence
- Quality review
- Technical diligence

**Limitations**

Value depends on the target being willing to run it, and designing meaningful evals is skilled work.

**Links:** [GitHub](https://github.com/langwatch/langwatch) &nbsp;·&nbsp; [Site](https://langwatch.ai)

---

### Rizzo PII

> Anonymise documents before they reach a model.

`Rizzo-AI-Academy/rizzo-pii` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Due Diligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 969 |
| **Forks** | 67 |
| **Language** | Python |
| **Status** | Active (last push 2026-08-09) |
| **Self-hostable** | yes |

**VC use case**

Data rooms contain salaries, customer names, personal data, and contract terms that should not be pasted into a hosted model. This strips personal information locally first, so an analyst can use an LLM on diligence material without breaching an NDA or a privacy obligation.

**Why it's interesting**

It runs locally, which is the whole point. Most PII tooling assumes the document is going to a cloud service you have already decided to trust.

**Good for**

- Data-room handling
- Privacy compliance
- Confidential analysis

**Limitations**

Detection will miss unusual identifiers, so a pass over the output is still needed. Anonymisation is not a legal substitute for an NDA.

**Links:** [GitHub](https://github.com/Rizzo-AI-Academy/rizzo-pii) &nbsp;·&nbsp; [Site](https://rizzo-ai-academy.github.io/rizzo-pii/)

---

### shhgit

> Finds secrets committed to public repositories.

`eth0izzle/shhgit` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Due Diligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 4k |
| **Forks** | 480 |
| **Language** | JavaScript |
| **Status** | Dormant (last push 2025-02-28, 18mo) |
| **Self-hostable** | yes |

**VC use case**

Leaked keys and credentials in a company's public repositories are a diligence finding with two readings: a security problem to price, and occasionally a signal about engineering maturity. Check the target, and check whether a portfolio company is leaking.

**Why it's interesting**

It monitors commit streams rather than one-off scanning, so exposure gets caught when it happens rather than when someone remembers to look.

**Good for**

- Technical due diligence
- Security review
- Portfolio monitoring

**Limitations**

Public repositories only, and a match is a lead: many are test fixtures or rotated keys. Confirm before you write it into a memo.

**Links:** [GitHub](https://github.com/eth0izzle/shhgit)

---

### Due Diligence Agents

> Agents that flag risks across legal and finance and link them.

`zoharbabin/due-diligence-agents` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◆ **VC-native** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Due Diligence |
| **VC relevance** | VC-native — built for venture capital, private markets, fund operations, or startup investing. |
| **License** | Apache-2.0 |
| **Stars** | 103 |
| **Forks** | 23 |
| **Language** | Python |
| **Status** | Active (last push 2026-08-08) |
| **Self-hostable** | yes |

**VC use case**

Runs separate reviewers over a deal, one legal-flavoured and one financial, then connects the flags they raise. The use case is catching the risk that only becomes visible when two workstreams are read together.

**Why it's interesting**

The cross-referencing is the interesting part. Most diligence tooling produces parallel checklists that never touch, which is exactly how correlated risks get missed.

**Good for**

- M&A diligence
- Legal risk review
- Financial risk review

**Limitations**

Small project, and the agents produce flags for a human to judge rather than conclusions. Nothing here replaces counsel.

**Links:** [GitHub](https://github.com/zoharbabin/due-diligence-agents) &nbsp;·&nbsp; [Site](https://zoharbabin.com/due-diligence-agents/)

---

### CorpusCustody

> Checks whether training data was legally usable.

`rishin-sharma/CorpusCustody` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Due Diligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 51 |
| **Forks** | 6 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-04) |
| **Self-hostable** | yes |

**VC use case**

For a fund underwriting an AI company, the question of where its training data came from and under what terms is now a real diligence item. This resolves licence obligations across a dataset and reports incompatibilities.

**Why it's interesting**

It treats data provenance as a checkable gate with resolved obligations rather than a legal opinion, which is the right shape for a diligence workstream that has to be repeatable.

**Good for**

- AI due diligence
- Licence compliance
- Technical diligence

**Limitations**

Very early project. It reads what the licences say, which is a factual check, not legal advice on whether a particular use is defensible.

**Links:** [GitHub](https://github.com/rishin-sharma/CorpusCustody)

---
