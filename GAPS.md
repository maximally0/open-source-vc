# Gaps: What Open Source Does Not Cover

The other half of knowing what you can build. Every sub-task below was checked against a candidate pool of 10,111 repositories, and the honest answer for most of them is that **no usable open-source tool exists**.

That is a finding, not an oversight. Nine of the fourteen sub-tasks most VCs would name as core to the job have essentially nothing behind them, and knowing which ones saves you from starting a build that has no library at the end of it.

Method for each line: search the pool, check the top results by hand, record what actually exists. Where a real tool does exist, it is listed and it is in the directory.

---

## Where the gaps are, in one picture

| Stage | Coverage | Honest read |
|---|---|---|
| 01 Source | **Good** | Collection and monitoring are general problems with real communities behind them |
| 02 Research | **Good** | Web intelligence is well served; this is where open source is strongest |
| 03 Diligence | **Mixed** | Documents and legal are decent; financial and entity work are thin |
| 04 Underwrite | **Poor** | Public-market maths exists; private-market valuation does not |
| 05 IC & Memo | **Poor** | Scaffolding exists; scoring and decision frameworks do not |
| 06 Close | **Mixed** | Contract tooling is real; transaction infrastructure is not |
| 07 Portfolio | **Poor** | Dashboards exist; KPI standards and runway tooling barely do |
| 08 Relationships | **Mixed** | General CRM is mature; venture-specific network intelligence is not |
| 09 Fund | **Poor** | General accounting exists; fund accounting, waterfalls, and LP reporting do not |

The pattern: **open source is strong where the problem is general and weak where the problem is regulated, commercial, or private-data-dependent.** Collection, parsing, retrieval, and search are general. Valuation, compliance, fund administration, and proprietary datasets are not.

---

## Verified gaps — nothing usable exists

### Incorporation and entity analysis

**Searched:** `incorporat`, `entity formation`, `company registry`, `corporate registry`, `beneficial owner`, `companies house api client`, `entity resolution company matching`.

**Found:** registry API clients at 8 to 40 stars for individual jurisdictions (a .NET Companies House wrapper, a PHP one), and [OpenRegistry](categories/company-discovery.md) at 18 stars covering a limited set of registries. Everything else matching those terms was noise: robotics SDKs, marketing-terms-of-service dumps, API documentation tools.

**Why:** corporate registries are fragmented by jurisdiction, often paid, frequently hostile to bulk access, and the good aggregated version (OpenCorporates) is a commercial product. **Sixteen stars is the state of the art for open entity data.**

**What to do instead:** [OpenRegistry](categories/company-discovery.md) where it covers your jurisdiction, direct registry APIs (Companies House is free and has a documented API), and accept manual lookups for the rest.

### Funding round data

**Searched:** `funding data`, `funding round`, `crunchbase`, `dealroom`.

**Found:** hobby projects reading Crunchbase's API, a few regional scrapes at single-digit stars, and notebooks analysing Kaggle dumps. Nothing maintained, nothing with coverage.

**Why:** this is the incumbent databases' entire product. Crunchbase, Dealroom, PitchBook, and Tracxn exist precisely because compiling this is expensive and the data is not freely licensable. No open project comes close, and none is likely to.

**What to do instead:** [yc-oss/api](categories/company-discovery.md) covers YC companies authoritatively and for free. Beyond that, build sector-specific company graphs by hand from public sources, which for a narrow thesis beats a commercial export because you know what is in it.

### Investor and fund databases

**Searched:** `investor database`, `vc database`, `fund database`, `GP database`.

**Found:** [OpenBook](categories/company-discovery.md) at 64 stars, and nothing else above single digits. A handful of dead React front ends and SEO pages.

**Why:** same as funding data. The LP and GP graph is a licence fee, and the people who have it do not give it away.

### Cohort analysis

**Searched:** `cohort analysis`, `cohort retention`, `retention curve`.

**Found:** one repository, at one star. It is an MCP server for product analytics at early-stage startups.

**Why:** cohort analysis is a spreadsheet. It is a pivot table with a date dimension, and it becomes a real tool only inside a product-analytics company where the data lives. For a fund looking at a target's cohorts, the target's own analytics platform is the tool, and a fund does not get access to it.

**What to do instead:** [Marimo](categories/knowledge-management.md) or [Jupyter Book](categories/knowledge-management.md), so the analysis is at least reproducible when someone asks how you got the number.

### Unit economics (LTV, CAC, payback)

**Searched:** `unit economic`, `ltv`, `cac`.

**Found:** nothing. The query returned Redis, Kubernetes tooling, and unrelated projects that happen to contain those three letters.

**Why:** unit economics are a model, not an application, and every company computes them differently. There is no standardised input, so there is nothing to build a tool around. This is a job for a spreadsheet and a founder who understands their own numbers.

### Investment scoring frameworks

**Searched:** `deal scoring`, `startup scoring`, `investment scoring`, `scorecard`, `rating framework`, `diligence rubric`.

**Found:** credit-scorecard tooling for lenders, SEO audit scorers, and one 11-star vendor-comparison tool. Nothing for venture.

**Why:** the interesting one, because it is not a technical gap. Scoring a startup is contested: every fund weights different things, and a published rubric invites gaming. The absence of a tool here reflects genuine disagreement about the method, not a missing library.

**What to do instead:** build it, but build the rubric first and make it yours. [Y Combinator's own guidance](https://www.ycombinator.com/library) is a starting point for what to weight. Any generic score you download will be wrong for your fund and you will not be able to explain why a deal scored what it did.

### Deal comparison and private comparables

**Searched:** `deal comparison`, `comparables`, `comp set`, `peer group`.

**Found:** student projects doing DCF on named listed companies. Nothing for comparing private deals against each other, and nothing for building a private comparable set.

**Why:** comparing private deals requires a proprietary dataset of private deals, which is the same gap as funding data wearing different clothes. Public-market comparables are well served — [OpenBB](categories/investment-analysis.md), [yfinance](categories/investment-analysis.md), [edgartools](categories/investment-analysis.md) — so use those and be explicit that the private side is your own analysis.

### Portfolio benchmarking

**Searched:** `benchmark portfolio`, `fund benchmark`, `vc benchmark`.

**Found:** nothing. Four results, all coursework.

**Why:** benchmarking a venture portfolio requires industry-wide return data by vintage, which is published in aggregate (by Cambridge Associates and similar) and never as data you can compute on. You can read a benchmark table. You cannot run against one.

### Fund accounting, waterfalls, and carried interest

**Searched:** the whole `lp-management` category, plus `fund waterfall`, `carried interest`, `ILPA`.

**Found:** [Beancount](categories/lp-management.md), [hledger](categories/lp-management.md), [Ledger](categories/lp-management.md), [GnuCash](categories/lp-management.md), and [ERPNext](categories/lp-management.md) — all general double-entry accounting, none fund-specific. Nothing implements carried interest, distribution waterfalls, or capital-account mechanics.

**Why:** regulated, audit-facing, liable, and idiosyncratic to each fund's LPA. The fund-administration industry exists because the work carries risk that is worth paying someone to hold.

**What to do instead:** keep the books in a plain-text ledger so at least the record is yours and diffable, and pay an administrator for the compliance and the LP reporting. Do not build this.

### Cap table tooling

**Found:** three entries. One self-hosted platform, one worksheet, one waterfall model. Two are dormant.

**Why:** cap-table management is one of the most commercially successful niches in venture software, which is exactly why so little of it is open. See the coverage note on [the cap tables page](categories/cap-tables.md).

**The exception worth noting:** [Open Cap Format](categories/standards.md) is the standard, and it is more mature than any of the tools implementing it. Standardise on the format even if you do not adopt a tool.

### Product launch tracking

**Searched:** `product hunt`, `launch feed`, `new product launch`.

**Found:** nothing usable. A few single-digit-star scrapers.

**Why:** Product Hunt's data is behind its own API and terms, and launch tracking is only valuable with broad coverage.

**What to do instead:** [changedetection.io](categories/deal-sourcing.md) on the launch pages you care about, and [TrendRadar](categories/market-research.md) for social signal.

### Warm-introduction paths

**Found:** [NetworkX](categories/relationship-intelligence.md) — a graph library, not a network tool. You supply the graph and write the query.

**Why:** the graph that matters is your own contacts, which no open project can have. The tool cannot exist without the data, and the data is a fund's private asset.

**What to do instead:** this is a two-hour [NetworkX](categories/relationship-intelligence.md) script over a CSV of your contacts and their companies. The library is the answer; there is no product because there is no shared dataset.

---

## Gaps closed in v1.1

These were missing from the first release and are now in the directory. Listed because the method matters: each was found by testing the directory against the sub-tasks rather than against its own categories.

| Sub-task | What was missing | Now covered by |
|---|---|---|
| Litigation and court records | Nothing at all | [CourtListener](categories/legal.md) (1k★, the only serious open index) and [Juriscraper](categories/legal.md) |
| Patent analysis | Only PatentView, which is a client | [Google Patents Public Data](categories/datasets.md) and the [Harvard USPTO dataset](categories/datasets.md) |
| GitHub signals and technical traction | Nothing | [OSS Insight](categories/company-discovery.md) and [Star History](categories/company-discovery.md) |
| Meeting intelligence | Only raw transcription models | [Meetily](categories/relationship-intelligence.md) — self-hosted, which is what a fund needs |
| Runway and burn monitoring | Nothing | [Runway Tool](categories/portfolio-management.md), small and stale but real |
| Company enrichment | Nothing | [Fire Enrich](categories/company-discovery.md) |
| Entity and registry checking | Nothing | [OpenRegistry](categories/company-discovery.md), thin coverage disclosed |

---

## How to use this page

**If you are choosing what to build:** start with a gap that is *general enough to have tools* but *specific enough to matter to your fund*. The failures on this page are mostly the second kind — too specific and too private to have a library. The workable projects live in the middle: the stack guides show what a working combination looks like.

**If you are buying:** the gaps are where your budget goes and where it is justified. Paying for a funding database or a fund administrator is not laziness; there is genuinely no open alternative, and this page is the evidence.

**If you disagree:** [open a correction](issues/new?template=correction.yml) with the repository. The most common way this page is wrong is not that a tool does not exist, but that it exists under vocabulary I did not search. Non-English projects and work hosted outside GitHub are the likeliest blind spots, and both are named in [METHODOLOGY.md](METHODOLOGY.md#known-limits-of-this-directory).
