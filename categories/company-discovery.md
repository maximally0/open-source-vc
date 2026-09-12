# Company Discovery & Deal Sourcing

_Turning the open web into a pipeline._

Startup and company databases, funding data, company enrichment, inbound deal flow, and pipeline construction.

**7 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-12

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

**Coverage note.** Company discovery in open source means building your own company graph from public sources, and the best starting material is the one authoritative dataset here: Y Combinator's own API. Beyond that, coverage of private companies is a function of what you collect. Nothing in this category replaces a commercial database, but several of these entries make a homemade one viable for a specific sector.

---

### YC Open API

> Y Combinator's own company and founder data, as an API.

`yc-oss/api` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; _dataset_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **License** | unknown |
| **Stars** | 231 |
| **Forks** | 22 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

Every YC company with its batch, industry, team size, status, and founders, plus a website field. Analysts use it to build a sector map of a batch cohort, spot which companies have already shut down, and check what a founder did before YC.

**Why it's interesting**

It is maintained by the accelerator itself rather than scraped, so the batch and status fields are authoritative. Being a plain API, it drops into a script instead of a spreadsheet.

**Good for**

- Cohort analysis
- Sector mapping
- Founder research

**Limitations**

Covers YC companies only, so it is a slice of the market and a biased one. No funding rounds or valuations. There is no licence file, so confirm terms before redistributing the data.

**Links:** [GitHub](https://github.com/yc-oss/api) &nbsp;·&nbsp; [Site](https://yc-oss.github.io/api/meta.json)

---

### dedupe

> Record linkage and entity resolution for messy company lists.

`dedupeio/dedupe` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **License** | MIT |
| **Stars** | 4.5k |
| **Forks** | 577 |
| **Language** | Python |
| **Status** | Dormant (last push 2025-07-29, 13mo) |
| **Self-hostable** | yes |

**VC use case**

Two funds merge sourcing lists, or a CRM export meets a scraped dataset, and someone has to decide which rows describe the same company before anything can be counted. This does that match at a scale no one does by hand.

**Why it's interesting**

You label a handful of pairs and it learns the rest, which handles the cases exact string matching misses: "Acme AI Inc" against "Acme.ai", or a legal entity against its trading name.

**Good for**

- CRM hygiene
- List merging
- Data quality

**Limitations**

Needs labelled training pairs to perform well, and gets slow on millions of rows without tuning. Python only.

**Links:** [GitHub](https://github.com/dedupeio/dedupe) &nbsp;·&nbsp; [Site](https://docs.dedupe.io)

---

### Company Research Agent

> An agent that researches a company and returns a structured brief.

`guy-hartstein/company-research-agent` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **License** | Apache-2.0 |
| **Stars** | 2.3k |
| **Forks** | 316 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-08) |
| **Self-hostable** | yes |

**VC use case**

Feed it a company name and get back a summary of what the company does, its market, competitors, and recent news, with sources. This is the first-pass brief an analyst writes before a screening call, assembled in minutes.

**Why it's interesting**

It is built on a graph of research steps rather than one long prompt, so the output shows the retrieval path. That makes the result easier to spot-check than a single model answer.

**Good for**

- Screening preparation
- Competitive research
- Market research

**Limitations**

Requires a search API key and an LLM provider, so it costs money to run. Output quality tracks the underlying search results, and citations need checking.

**Links:** [GitHub](https://github.com/guy-hartstein/company-research-agent) &nbsp;·&nbsp; [Site](https://companyresearcher.tavily.com)

---

### ExploreYC

> Browse the YC portfolio as a searchable, filterable site.

`KonstantinMB/exploreyc` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **License** | MIT |
| **Stars** | 44 |
| **Forks** | 6 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

A fast way to walk the YC universe by batch, industry, and hiring status when you want to see a sector rather than query an API. Useful for an associate building a market map for a thesis in an afternoon.

**Why it's interesting**

It layers an idea validator, a hiring board, and a crude success signal over the same dataset, which shows how far a public company graph can be stretched.

**Good for**

- Market mapping
- Thesis building
- Sourcing

**Limitations**

Small project with a narrow dataset behind it, and the predictive features are demonstration-grade rather than something to make decisions on.

**Links:** [GitHub](https://github.com/KonstantinMB/exploreyc) &nbsp;·&nbsp; [Site](https://exploreyc.com)

---

### Idea Reality

> Checks whether a product idea already exists, across five sources.

`mnemox-ai/idea-reality-mcp` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **License** | MIT |
| **Stars** | 815 |
| **Forks** | 88 |
| **Language** | Python |
| **Status** | Active (last push 2026-08-11) |
| **Self-hostable** | yes |

**VC use case**

Before a first call with a startup claiming a new category, run the premise through this to see what already exists on GitHub, Hacker News, npm, PyPI, and Product Hunt. It is a five-minute sanity check on how novel the claim really is.

**Why it's interesting**

It queries the places where working software shows up first, rather than press coverage, so it catches prior art that predates the funding announcements.

**Good for**

- Novelty checks
- Competitive research
- First-call preparation

**Limitations**

It reports existence, not quality or traction. A hit means something similar is public, which is not the same as a competitor, and a miss proves nothing.

**Links:** [GitHub](https://github.com/mnemox-ai/idea-reality-mcp) &nbsp;·&nbsp; [Site](https://mnemox.ai/check/)

---

### OpenBook

> An open investor and venture database.

`iloveitaly/openbook` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; _dataset_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **License** | MIT |
| **Stars** | 64 |
| **Forks** | 9 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-02) |
| **Self-hostable** | yes |

**VC use case**

A community attempt at the investor-and-fund graph that normally sits behind a PitchBook licence: who invests at which stage, in which sectors, and alongside whom. Useful for building a target list of funds rather than companies.

**Why it's interesting**

It is the only serious open attempt at this dataset that this research turned up, which makes it worth watching even at its current size.

**Good for**

- Fund targeting
- Syndicate research
- Fundraising research

**Limitations**

Early and thin compared with commercial alternatives, and coverage of any given sector is likely incomplete. Verify entries upstream before relying on them.

**Links:** [GitHub](https://github.com/iloveitaly/openbook)

---

### MiraclePlus Gallery

> Five years of MiraclePlus (formerly YC China) demo-day companies.

`Nimbus318/miracle-plus-gallery` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; _dataset_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **License** | MIT |
| **Stars** | 25 |
| **Forks** | 5 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-06-08) |
| **Self-hostable** | yes |

**VC use case**

A structured look at the portfolio of the accelerator that ran YC's China programme, including sector tags, school networks, and people links. For anyone investing in or researching Chinese AI, robotics, or cross-border companies this is otherwise hard to assemble.

**Why it's interesting**

The data is in Chinese and nowhere else in a structured form. It is a reminder that a large part of the world's startup activity is invisible to English-language searches.

**Good for**

- China market research
- Sector mapping
- Network analysis

**Limitations**

Interface and data are Chinese-language, coverage stops at the programme's end, and there is no licence file. Confirm terms before reuse.

**Links:** [GitHub](https://github.com/Nimbus318/miracle-plus-gallery) &nbsp;·&nbsp; [Site](https://mplus-gallery.nimbus-nimo.com)

---
