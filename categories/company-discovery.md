# Company Discovery & Deal Sourcing

_Turning the open web into a pipeline._

Startup and company databases, funding data, company enrichment, inbound deal flow, and pipeline construction.

**11 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-14

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

**Coverage note.** Company discovery in open source means building your own company graph from public sources, and the best starting material is the one authoritative dataset here: Y Combinator's own API. Beyond that, coverage of private companies is a function of what you collect. Nothing in this category replaces a commercial database, but several of these entries make a homemade one viable for a specific sector.

---

### YC Open API

> Y Combinator's own company and founder data, as an API.

`yc-oss/api` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ◆ **VC-native** &nbsp;·&nbsp; _dataset_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **VC relevance** | VC-native — built for venture capital, private markets, fund operations, or startup investing. |
| **License** | unknown |
| **Stars** | 231 |
| **Forks** | 22 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-14) |
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

### Star History

> Plot repository star growth over time.

`star-history/star-history` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 9.5k |
| **Forks** | 370 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

The fast sanity check on a developer-tool claim. A repo with a vertical star curve followed by a plateau tells a different story from one climbing steadily, and a sudden spike often means a launch or a Hacker News moment rather than adoption.

**Why it's interesting**

It is a small tool that answers a question people routinely get wrong, and the curve is usually more informative than the total.

**Good for**

- Technical due diligence
- GitHub signals
- Competitor tracking

**Limitations**

Stars measure attention, not usage or revenue, and spikes are frequently launch-driven. Read it as one input.

**Links:** [GitHub](https://github.com/star-history/star-history) &nbsp;·&nbsp; [Site](https://www.star-history.com)

---

### dedupe

> Record linkage and entity resolution for messy company lists.

`dedupeio/dedupe` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 4.5k |
| **Forks** | 577 |
| **Language** | Python |
| **Status** | Dormant (last push 2025-07-29, 14mo) |
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

### OSS Insight

> Analytics over the public GitHub event stream.

`pingcap/ossinsight` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 2.5k |
| **Forks** | 446 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-08) |
| **Self-hostable** | yes |

**VC use case**

Technical traction without asking the company: how fast is a repository growing, who contributes, where are the contributors located, is momentum rising or flattening. For a developer-tools or open-source business this is the most objective signal available before revenue.

**Why it's interesting**

It analyses the full public GitHub event history rather than current star counts, so you can see trajectory and contributor geography. That is the difference between a vanity metric and a diligence input.

**Good for**

- Technical due diligence
- GitHub signals
- Developer market research

**Limitations**

GitHub only, so it says nothing about closed-source businesses, and popularity is not revenue. The hosted instance is the primary product.

**Links:** [GitHub](https://github.com/pingcap/ossinsight) &nbsp;·&nbsp; [Site](https://ossinsight.io/)

---

### Company Research Agent

> An agent that researches a company and returns a structured brief.

`guy-hartstein/company-research-agent` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
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

`KonstantinMB/exploreyc` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◆ **VC-native** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **VC relevance** | VC-native — built for venture capital, private markets, fund operations, or startup investing. |
| **License** | MIT |
| **Stars** | 44 |
| **Forks** | 6 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-14) |
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

### Fire Enrich

> Turn an email or domain into company data.

`firecrawl/fire-enrich` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 1.3k |
| **Forks** | 315 |
| **Language** | TypeScript |
| **Status** | Active (last push 2025-10-08) |
| **Self-hostable** | yes |

**VC use case**

The enrichment step in a sourcing pipeline: given a list of addresses from a community, an event, or a newsletter, resolve them to companies with industry and size. That is how a list of names becomes a target list.

**Why it's interesting**

Enrichment is normally a paid API and this does the job with a crawler and a model, so a fund can run it over its own lists without per-record pricing.

**Good for**

- Company enrichment
- Inbound triage
- Sourcing pipelines

**Limitations**

Enrichment quality depends on what is publicly crawlable, so results need checking before they enter a CRM. Early project.

**Links:** [GitHub](https://github.com/firecrawl/fire-enrich)

---

### Idea Reality

> Checks whether a product idea already exists, across five sources.

`mnemox-ai/idea-reality-mcp` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 815 |
| **Forks** | 87 |
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

`iloveitaly/openbook` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◆ **VC-native** &nbsp;·&nbsp; _dataset_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **VC relevance** | VC-native — built for venture capital, private markets, fund operations, or startup investing. |
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

`Nimbus318/miracle-plus-gallery` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◆ **VC-native** &nbsp;·&nbsp; _dataset_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **VC relevance** | VC-native — built for venture capital, private markets, fund operations, or startup investing. |
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

### OpenRegistry

> Company registry data direct from official sources.

`sophymarine/openregistry` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Company Discovery & Deal Sourcing |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 18 |
| **Forks** | 2 |
| **Language** | JavaScript |
| **Status** | Active (last push 2026-09-07) |
| **Self-hostable** | yes |

**VC use case**

Incorporation and corporate-structure checking: is the entity real, where is it registered, what is its status. A surprising number of pitches get the legal entity wrong, and the registry is the authoritative answer.

**Why it's interesting**

One of very few open attempts at official registry data, and it exposes it to agents rather than only as a website. Corporate registries are fragmented and paid, which is why this category is so thin.

**Good for**

- Entity verification
- Legal due diligence
- KYC checking

**Limitations**

Coverage of jurisdictions is limited and uneven, and registry data quality varies by country. Early project with a small maintainer base.

**Links:** [GitHub](https://github.com/sophymarine/openregistry) &nbsp;·&nbsp; [Site](https://openregistry.sophymarine.com)

---
