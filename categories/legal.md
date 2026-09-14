# Legal & Transaction Infrastructure

_Documents that decide the deal._

SAFEs, term sheets, legal NLP, contract analysis, clause extraction, and transaction infrastructure.

**17 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-14

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

---

### Mike

> An open legal AI platform for document review.

`open-legal-products/mike` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Legal & Transaction Infrastructure |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | AGPL-3.0 |
| **Stars** | 4.2k |
| **Forks** | 1.3k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

Contract review is the most expensive line item in a deal that nobody talks about. Mike reads agreements and returns structured analysis, so a fund can triage a commercial contract set before paying outside counsel for the ones that matter.

**Why it's interesting**

It is the most serious attempt at an open answer to the commercial legal AI products, and it handles the document types that actually appear in a deal rather than a demo contract.

**Good for**

- Contract review
- Legal due diligence
- Document analysis

**Limitations**

AGPL-licensed. It produces analysis for a lawyer to check, not legal advice, and it should not be the last word on anything that carries liability.

**Links:** [GitHub](https://github.com/open-legal-products/mike) &nbsp;·&nbsp; [Site](https://mikeoss.com)

---

### CourtListener

> A searchable archive of US court data.

`freelawproject/courtlistener` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Legal & Transaction Infrastructure |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unverified (Other) |
| **Stars** | 1k |
| **Forks** | 271 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | yes |

**VC use case**

Litigation is a diligence question almost nobody checks properly: is the target or its founders party to a lawsuit, has a competitor sued them, is there an IP dispute waiting. Court records are public but scattered across thousands of county and federal systems. This puts them in one searchable place.

**Why it's interesting**

Maintained by the Free Law Project, which has been doing this for over a decade with bulk data and an API rather than a website you have to scrape. It is the single biggest open legal dataset available.

**Good for**

- Legal due diligence
- Litigation checks
- Founder background

**Limitations**

US courts only, and coverage varies by jurisdiction and court level, with some records incomplete. The licence is not a standard SPDX identifier, so check terms before building a service on the data.

**Links:** [GitHub](https://github.com/freelawproject/courtlistener) &nbsp;·&nbsp; [Site](https://www.courtlistener.com)

---

### OpenContracts

> An open document intelligence platform for contract analysis.

`Open-Source-Legal/OpenContracts` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Legal & Transaction Infrastructure |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 1.5k |
| **Forks** | 186 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | yes |

**VC use case**

A fund that signs many similar agreements accumulates a corpus nobody can query. This structures contracts, extracts the clauses that matter, and lets you ask how a particular indemnity is worded across the whole set.

**Why it's interesting**

It is built by people in the legal field for the work legal teams do, and it is MIT licensed, which makes it straightforward to build on.

**Good for**

- Contract analysis
- Clause extraction
- Legal due diligence

**Limitations**

Smaller than the commercial alternatives, and setup means hosting a real application. Extraction quality depends on document consistency.

**Links:** [GitHub](https://github.com/Open-Source-Legal/OpenContracts) &nbsp;·&nbsp; [Site](https://open-source-legal.github.io/OpenContracts/)

---

### Claude Legal Skill

> A contract review workflow with defined risk categories.

`evolsb/claude-legal-skill` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Legal & Transaction Infrastructure |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 441 |
| **Forks** | 57 |
| **Language** | unknown |
| **Status** | Active (last push 2026-07-23) |
| **Self-hostable** | yes |

**VC use case**

Reviews a contract against a stated risk framework and produces output a lawyer can work from. Useful as a first pass that tells an analyst which clauses deserve attention, rather than as a substitute for review.

**Why it's interesting**

It uses a published contract risk dataset for its categories, so the risk list is grounded in research rather than invented. That is the difference between a useful checklist and a random prompt.

**Good for**

- Contract review
- Legal due diligence
- Risk triage

**Limitations**

Tied to a specific agent tool, and it is only as good as the risk framework behind it. Not legal advice, and it should not be the only reader of anything material.

**Links:** [GitHub](https://github.com/evolsb/claude-legal-skill) &nbsp;·&nbsp; [Site](https://ctsheehan.com)

---

### Python-Redlines

> Generate Word tracked changes from Python.

`JSv4/Python-Redlines` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Legal & Transaction Infrastructure |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 128 |
| **Forks** | 21 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-06) |
| **Self-hostable** | yes |

**VC use case**

The concrete deliverable in any negotiation is a redline. This produces native Word tracked changes programmatically, so a fund or its tooling can generate a marked-up draft a counterparty can open, comment on, and accept.

**Why it's interesting**

Producing genuine tracked changes rather than a PDF comparison is fiddly, and this solves it. There is almost nothing else open source that does it.

**Good for**

- Contract negotiation
- Redlining
- Legal documentation

**Limitations**

Narrow tool: it produces the redline, it does not decide what should change. Word compatibility details matter.

**Links:** [GitHub](https://github.com/JSv4/Python-Redlines) &nbsp;·&nbsp; [Site](https://jsv4.github.io/Python-Redlines/)

---

### OpenNyAI

> An NLP pipeline for Indian legal documents.

`OpenNyAI/Opennyai` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Legal & Transaction Infrastructure |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 101 |
| **Forks** | 18 |
| **Language** | Python |
| **Status** | Active (last push 2026-04-01) |
| **Self-hostable** | yes |

**VC use case**

For anyone working in or investing into India, court judgments and legal documents in that jurisdiction were largely unprocessable by Western legal NLP. This extracts structure, judgment outcomes, and citations from them.

**Why it's interesting**

It addresses a jurisdiction with enormous case volume and almost no tooling, which is exactly the kind of gap that gets missed by English-language-first projects.

**Good for**

- India market research
- Legal research
- Document pipelines

**Limitations**

Indian legal documents only, and quality varies by court and document age. Model accuracy on unusual document types needs checking.

**Links:** [GitHub](https://github.com/OpenNyAI/Opennyai)

---

### Open US Law

> A structured corpus of US primary law.

`Vaquill-AI/open-us-law` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _dataset_

| | |
|---|---|
| **Category** | Legal & Transaction Infrastructure |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 61 |
| **Forks** | 15 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-06) |
| **Self-hostable** | yes |

**VC use case**

Millions of sections of state codes, the US Code, and regulations in a structured form. For a fund underwriting a regulated business, this is the source material for checking what the company is actually required to do.

**Why it's interesting**

Primary law in a queryable structure rather than a website is what makes regulatory research automatable, and almost nobody has assembled it openly.

**Good for**

- Regulatory research
- Legal due diligence
- Dataset building

**Limitations**

A corpus, not an answer: coverage, currency, and updates are the maintainer's challenge, and it is not a substitute for counsel.

**Links:** [GitHub](https://github.com/Vaquill-AI/open-us-law) &nbsp;·&nbsp; [Site](https://huggingface.co/datasets/vaquill/open-us-law)

---

### Juriscraper

> Scrapers for US court websites.

`freelawproject/juriscraper` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Legal & Transaction Infrastructure |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | BSD-2-Clause |
| **Stars** | 636 |
| **Forks** | 172 |
| **Language** | HTML |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

The collection layer behind CourtListener, usable directly when a diligence needs filings from a specific court that is not well covered. Relevant for jurisdiction- specific litigation research.

**Why it's interesting**

Court websites are hostile to automation and this maintains scrapers for hundreds of them, including the parsing of what comes back. That maintenance is the expensive part.

**Good for**

- Litigation research
- Legal data collection

**Limitations**

Per-court scrapers break as courts change their sites, so expect gaps and breakage. US only.

**Links:** [GitHub](https://github.com/freelawproject/juriscraper) &nbsp;·&nbsp; [Site](https://free.law/projects/juriscraper)

---

### doc-haus

> A self-hosted legal AI agent that keeps documents local.

`sure-scale/doc-haus` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Legal & Transaction Infrastructure |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unverified (Other) |
| **Stars** | 71 |
| **Forks** | 19 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-06-13) |
| **Self-hostable** | yes |

**VC use case**

Redlines contracts without the document leaving the machine, which is the requirement when the material is unannounced deal paperwork. Aimed at the confidentiality constraint that stops funds using commercial legal AI.

**Why it's interesting**

It treats local processing as the product rather than a limitation, and it delivers the redline in Word, which is the format the other side requires.

**Good for**

- Confidential review
- Redlining
- Contract analysis

**Limitations**

A fork of an earlier project with a single maintainer, and the licence is not a standard SPDX identifier. Early.

**Links:** [GitHub](https://github.com/sure-scale/doc-haus) &nbsp;·&nbsp; [Site](https://doc.haus)

---

### DocuChat

> Self-hosted document chat for lawyers.

`janderswag/docuchat.app` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Legal & Transaction Infrastructure |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 33 |
| **Forks** | 0 |
| **Language** | Python |
| **Status** | Active (last push 2026-07-22) |
| **Self-hostable** | yes |

**VC use case**

Ask questions of a legal PDF set using a local model, with nothing leaving the machine. A reasonable pattern for a fund that wants document Q&A on privileged material without a cloud dependency.

**Why it's interesting**

It is built around the constraint that matters in legal work, which is that the document set may not be shareable. Runs with local models.

**Good for**

- Privileged documents
- Document Q&A
- Confidential analysis

**Limitations**

Local models are weaker than hosted ones, so answers need more checking. Single maintainer, early.

**Links:** [GitHub](https://github.com/janderswag/docuchat.app) &nbsp;·&nbsp; [Site](https://docuchat.app/)

---

### OpenSpecter

> A self-hostable workspace for legal teams.

`akashshrx/OpenSpecter` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Legal & Transaction Infrastructure |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | AGPL-3.0 |
| **Stars** | 31 |
| **Forks** | 4 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

A broader legal workspace rather than one function: document handling, review, and drafting for an in-house team, deployed on your own infrastructure. Relevant to funds and portfolio companies that want legal tooling without a hosted vendor.

**Why it's interesting**

It aims at the whole workflow rather than a single task, which is closer to how a legal team actually operates.

**Good for**

- Legal workspace
- Contract review
- In-house legal

**Limitations**

AGPL-licensed and very early, so expect to be part of its development rather than a satisfied user of it.

**Links:** [GitHub](https://github.com/akashshrx/OpenSpecter) &nbsp;·&nbsp; [Site](https://www.openspecter.com/)

---

### LexNLP

> Extract legal structure from contracts and statutes.

`LexPredict/lexpredict-lexnlp` &nbsp;·&nbsp; 📚 **Research** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Legal & Transaction Infrastructure |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | AGPL-3.0 |
| **Stars** | 795 |
| **Forks** | 199 |
| **Language** | Jupyter Notebook |
| **Status** | Dormant (last push 2024-05-27, 28mo) |
| **Self-hostable** | yes |

**VC use case**

Pull the dates, money amounts, durations, conditions, and defined terms out of contracts at scale. This is the groundwork for any question a fund wants to ask across a portfolio's contracts rather than one at a time.

**Why it's interesting**

It encodes knowledge of legal document conventions, which is what makes extraction work where generic NLP fails. The library is a reference for how to model legal text.

**Good for**

- Clause extraction
- Contract analysis
- Legal research

**Limitations**

Last meaningful development was some years ago, so treat it as a foundation to build on rather than a maintained product. AGPL-licensed.

**Links:** [GitHub](https://github.com/LexPredict/lexpredict-lexnlp)

---

### Blackstone

> A spaCy pipeline trained on legal text.

`ICLRandD/Blackstone` &nbsp;·&nbsp; 📚 **Research** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Legal & Transaction Infrastructure |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 697 |
| **Forks** | 110 |
| **Language** | Python |
| **Status** | Dormant (last push 2024-07-16, 26mo) |
| **Self-hostable** | yes |

**VC use case**

Named entity recognition for contracts: parties, dates, monetary amounts, and obligations. Useful when building a contract pipeline and needing the preprocessing that legal text specifically requires.

**Why it's interesting**

General NLP models perform badly on legal language, and this is one of the few purpose-trained alternatives with the model in the open.

**Good for**

- Contract analysis
- Entity extraction
- Legal research

**Limitations**

Development stopped a while ago and the underlying spaCy version is dated, so expect to port it. English contracts only.

**Links:** [GitHub](https://github.com/ICLRandD/Blackstone) &nbsp;·&nbsp; [Site](https://research.iclr.co.uk)

---

### Awesome Legal NLP

> An index of legal NLP resources, datasets, and tools.

`maastrichtlawtech/awesome-legal-nlp` &nbsp;·&nbsp; 📚 **Research** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _research_

| | |
|---|---|
| **Category** | Legal & Transaction Infrastructure |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 338 |
| **Forks** | 48 |
| **Language** | unknown |
| **Status** | Active (last push 2025-10-14) |
| **Self-hostable** | yes |

**VC use case**

The starting point for anyone building legal document tooling: what datasets exist, what has been tried, and which papers the field is built on. Saves a week of literature searching.

**Why it's interesting**

Maintained by a university legal-tech group rather than a hobbyist, so the entries are relevant to research rather than only to products.

**Good for**

- Legal research
- Tool selection
- Literature review

**Limitations**

A curated list, so it inherits the format's weaknesses: some links go stale and maintenance is intermittent.

**Links:** [GitHub](https://github.com/maastrichtlawtech/awesome-legal-nlp)

---

### LexGLUE

> A benchmark for legal language understanding.

`coastalcph/lex-glue` &nbsp;·&nbsp; 📚 **Research** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _research_

| | |
|---|---|
| **Category** | Legal & Transaction Infrastructure |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unknown |
| **Stars** | 271 |
| **Forks** | 44 |
| **Language** | Python |
| **Status** | Dormant (last push 2025-07-23, 14mo) |
| **Self-hostable** | yes |

**VC use case**

When a vendor or an internal project claims to understand contracts, this is how that claim gets tested on a comparable set of legal tasks. Useful as the standard a diligence review can point at.

**Why it's interesting**

It is a published benchmark with a defined task set, which means results across different models are actually comparable. That is rarer than it should be.

**Good for**

- Model evaluation
- Legal tech diligence
- Research

**Limitations**

Benchmark tasks are not venture diligence tasks. No licence file is present, so check terms before redistributing the data.

**Links:** [GitHub](https://github.com/coastalcph/lex-glue)

---

### Open Australian Legal Corpus

> The pipeline behind a multi-jurisdiction legal corpus.

`isaacus-dev/open-australian-legal-corpus-creator` &nbsp;·&nbsp; 📚 **Research** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _dataset_

| | |
|---|---|
| **Category** | Legal & Transaction Infrastructure |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 124 |
| **Forks** | 20 |
| **Language** | Python |
| **Status** | Dormant (last push 2025-05-26, 16mo) |
| **Self-hostable** | yes |

**VC use case**

A worked example of assembling a legal corpus properly: which sources, what normalisation, how updates are handled. Useful if a fund or a portfolio company needs a jurisdiction-specific legal dataset.

**Why it's interesting**

The tooling is published alongside the result, so the method can be copied for another jurisdiction rather than only the data being consumed.

**Good for**

- Dataset building
- Legal research
- Regulatory research

**Limitations**

Australian sources, so the specifics need redoing elsewhere. Corpus maintenance over time is the hard part and is largely manual.

**Links:** [GitHub](https://github.com/isaacus-dev/open-australian-legal-corpus-creator) &nbsp;·&nbsp; [Site](https://huggingface.co/datasets/umarbutler/open-australian-legal-corpus)

---

### LeSICiN

> A graph-based approach to identifying contract clauses.

`Law-AI/LeSICiN` &nbsp;·&nbsp; 📚 **Research** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _research_

| | |
|---|---|
| **Category** | Legal & Transaction Infrastructure |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unknown |
| **Stars** | 25 |
| **Forks** | 11 |
| **Language** | Python |
| **Status** | Dormant (last push 2024-04-20, 29mo) |
| **Self-hostable** | yes |

**VC use case**

Read it to understand why clause extraction is hard: obligations in a contract refer to each other, so a sentence-level model misses conditions defined three pages away. Relevant when specifying a contract pipeline.

**Why it's interesting**

It models the document as a graph rather than a sequence of sentences, which is the right representation for contracts and explains a lot of extraction failures.

**Good for**

- Understanding clause extraction
- Contract analysis
- Research

**Limitations**

Academic implementation with a dataset, not a product, and no licence file is present.

**Links:** [GitHub](https://github.com/Law-AI/LeSICiN)

---
