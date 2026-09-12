# The Sourcing Stack

Finding companies before they appear in a pitch deck, and doing it without a data vendor's licence.

---

## The problem

Most funds describe their sourcing the same way: it comes from the network. That is true and also incomplete. A network tells you about companies its members already know, which is a small and correlated subset of what exists. The gap is everything being built by people outside your network, in markets you do not follow, by founders who have not raised before.

Closing that gap with open-source tooling means building a monitoring operation. Not a database, not a platform, a habit with infrastructure behind it.

## The four questions sourcing actually answers

**1. What exists that I do not know about?**

Collect from the sources where companies appear before they are funded: package registries, app stores, job boards, conference speaker lists, accelerator cohorts, government registries, and the technical communities where a category is being built out in public.

- [JobSpy](../categories/founder-discovery.md) for hiring activity across the major boards
- [Scrapy](../categories/osint.md) and [Crawlee](../categories/osint.md) for anything you need to collect yourself
- The [YC API](../categories/company-discovery.md) for a cohort you can map by sector
- [ExploreYC](../categories/company-discovery.md) when you want to browse rather than query

**2. What changed this week?**

A company that just hired five people in a function it did not previously have is a different company from the one you looked at last quarter.

- [changedetection.io](../categories/deal-sourcing.md) for specific pages
- [Huginn](../categories/deal-sourcing.md) for multi-step watchers with actions
- [subsignal](../categories/deal-sourcing.md) if you want something already shaped for funds

**3. Is this company real?**

A landing page costs nothing. Evidence of building costs something.

- [subfinder](../categories/osint.md) to find the hostnames they actually run
- [httpx](../categories/osint.md) to see what is live on them
- [Web-Check](../categories/founder-discovery.md) for the stack and the mail configuration
- [shhgit](../categories/due-diligence.md) for whether they leak credentials in public repositories

**4. Is it different from the thirty companies that look identical?**

At the point where every deck describes the same category, the difference is in specifics: pricing structure, target customer, technical approach, hiring pattern.

- [Firecrawl](../categories/osint.md) to collect competitor pages as text
- [Finance Toolkit](../categories/investment-analysis.md) if public comparables exist
- [idea-reality-mcp](../categories/company-discovery.md) to check how novel the claim is before a call

## The pipeline, concretely

```text
Sources you monitor (job boards, registries, communities, competitors)
        │
   Collect  ──  Scrapy / Crawlee / API connectors
        │
   Resolve  ──  dedupe, so the same company is one row
        │
   Enrich   ──  domain, stack, headcount signal, funding, founders
        │
   Store    ──  Postgres, NocoDB, or Grist
        │
   Watch    ──  changedetection.io / Huginn on what matters
        │
   Triage   ──  a partner reviewing twenty rows, not two hundred
```

**The step everyone skips is resolution.** Companies appear as "Acme", "Acme AI", "Acme Labs Inc", and "acme.ai", and if you do not collapse those you will report a market of eighty companies that is actually sixty. [dedupe](../categories/company-discovery.md) is the tool; ignoring it is the most common reason a homemade sourcing database is quietly wrong.

## What to actually watch

A watchlist is only useful if the changes are actionable. In practice, five categories of page produce almost all the signal worth acting on:

| What | Why it matters | Tool |
|---|---|---|
| Job postings by function | Hiring is the hardest signal to fake and it leads revenue | [JobSpy](../categories/founder-discovery.md) |
| Pricing pages | A price change is a positioning decision, usually ahead of an announcement | [changedetection.io](../categories/deal-sourcing.md) |
| Terms and privacy pages | Changes here precede compliance shifts and market moves | [changedetection.io](../categories/deal-sourcing.md) |
| Product documentation | New capabilities show up in docs before marketing | [Firecrawl](../categories/osint.md) |
| Team pages | Departures and senior hires are the earliest visible sign of a pivot | [SingleFile](../categories/osint.md) |

Keep the archive. [SingleFile](../categories/osint.md) saves a page as a single self-contained file, which is how you later prove that a company's positioning changed rather than argue about it.

## Attribution: the part funds neglect

Most funds cannot say which channel produced their last ten deals, which means they cannot invest more in whichever one works. If you run a newsletter, a scout programme, an event, or a podcast, put attributable links on everything.

[Dub](../categories/deal-sourcing.md) does this and keeps the data in your own infrastructure. The output changes a conversation from "the newsletter is working well" to "eleven of our last forty qualified conversations came from it, and two became termsheets."

## What open source cannot do here

Two things, stated plainly because pretending otherwise costs a quarter:

**The compiled private-company graph.** Who invested in whom, at what valuation, with what terms. This is the incumbent databases' entire product and no open project comes close. You can build a sector-specific version of it by hand, and for a focused thesis that is often enough. You cannot build a general one.

**The network effect.** The best deal flow is a byproduct of being useful to founders, and no software changes that. What software changes is whether you notice what your network sends you, and whether you have something to send back.

## A realistic starting point

Week one: pick one sector you actually care about. Collect every company in it you can find from public sources, resolve the duplicates, put it in [NocoDB](../categories/deal-sourcing.md). That is a market map, and hand-built ones beat commercial exports for a narrow sector because you know what is in them.

Week two: choose five pages per company worth watching. Set up [changedetection.io](../categories/deal-sourcing.md). Route alerts somewhere a person reads.

Week three: connect it to the fund's pipeline so a new signal becomes a row an analyst reviews, with a name attached. This is the step that turns a project into a process.

Then do nothing for a month and see whether the alerts were worth reading. If they were, widen the sector. If they were not, the problem is the watchlist, not the tooling, and adding more sources will not fix it.
