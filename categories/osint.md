# Web Intelligence & OSINT

_Systematic collection from public sources._

OSINT frameworks, crawling, scraping, domain intelligence, monitoring, and change detection.

**17 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-12

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

---

### SingleFile

> Save a faithful, self-contained copy of a web page.

`gildas-lormeau/SingleFile` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Web Intelligence & OSINT |
| **License** | AGPL-3.0 |
| **Stars** | 22.4k |
| **Forks** | 1.4k |
| **Language** | JavaScript |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

Evidence capture. When a company's claims, pricing, or team page matter to a decision, save the page as it stands today: one file, styling and content intact, openable years later. Analysts who have watched a pitch deck quietly change know why this matters.

**Why it's interesting**

It inlines everything into a single file rather than a folder of assets, so archives stay portable and readable. It runs as a browser extension or a CLI.

**Good for**

- Evidence capture
- Due diligence records
- Competitive monitoring

**Limitations**

Saved pages can be large, and some dynamic content still fails to capture. It is a snapshot, not a legal record of what a company said.

**Links:** [GitHub](https://github.com/gildas-lormeau/SingleFile) &nbsp;·&nbsp; [Site](https://getsinglefile.com)

---

### Firecrawl

> Turns websites into clean markdown for models.

`firecrawl/firecrawl` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Web Intelligence & OSINT |
| **License** | AGPL-3.0 |
| **Stars** | 179.5k |
| **Forks** | 9.8k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | partial (open core) |

**VC use case**

Feeds a research or diligence agent with readable page content instead of raw HTML. Concretely: crawl every company on a market map and get text the model can actually use, ready for extraction into a comparison table.

**Why it's interesting**

It solves the unglamorous part of data collection, which is stripping navigation, cookie banners, and markup so that what reaches the model is the content.

**Good for**

- Research pipelines
- Market mapping
- Data collection

**Limitations**

The open-source core pairs with a paid hosted service, and the best crawling behaviour is easier to get from the hosted version. Self-hosting needs browser infrastructure.

**Links:** [GitHub](https://github.com/firecrawl/firecrawl) &nbsp;·&nbsp; [Site](https://firecrawl.dev)

---

### Crawlee

> Crawling and browser automation with anti-blocking built in.

`apify/crawlee` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Web Intelligence & OSINT |
| **License** | Apache-2.0 |
| **Stars** | 25.8k |
| **Forks** | 1.7k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

The modern alternative when a target site renders everything in JavaScript or fights scrapers. Funds collecting pricing pages or marketplace listings use it because the browser handling is already solved.

**Why it's interesting**

It unifies HTTP and headless-browser crawling behind one interface, so the same crawler can start cheap and escalate to a real browser only where needed.

**Good for**

- Dataset collection
- Competitor pricing
- Marketplace research

**Limitations**

Fingerprint management is an arms race you can lose. Running browsers at scale needs real infrastructure.

**Links:** [GitHub](https://github.com/apify/crawlee) &nbsp;·&nbsp; [Site](https://crawlee.dev)

---

### SpiderFoot

> Automates OSINT collection and maps what it finds.

`smicallef/spiderfoot` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Web Intelligence & OSINT |
| **License** | MIT |
| **Stars** | 22.1k |
| **Forks** | 3.6k |
| **Language** | Python |
| **Status** | Active (last push 2026-04-13) |
| **Self-hostable** | yes |

**VC use case**

Point it at a company domain and it runs many collection modules, then links the results into a graph of hosts, addresses, accounts, and leaks. Used as a wide first sweep on a target with no public history.

**Why it's interesting**

The module list is long and the correlation step is the point: it connects findings across sources rather than handing you separate reports.

**Good for**

- Company reconnaissance
- Technical screening
- Risk checks

**Limitations**

Noisy without tuning, and some modules need API keys. Output needs a human to separate signal from coincidence.

**Links:** [GitHub](https://github.com/smicallef/spiderfoot) &nbsp;·&nbsp; [Site](http://www.spiderfoot.net)

---

### subfinder

> Fast passive subdomain discovery.

`projectdiscovery/subfinder` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Web Intelligence & OSINT |
| **License** | MIT |
| **Stars** | 14.4k |
| **Forks** | 1.6k |
| **Language** | Go |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

Map the hostnames a company actually runs, drawn from public certificate and DNS sources without touching the target. That reveals products and environments the marketing site never mentions: staging systems, regional deployments, internal tools.

**Why it's interesting**

It is passive, so it collects from public records rather than probing the target, and it is fast enough to run across a hundred companies in one pass.

**Good for**

- Technical screening
- Product discovery
- Market mapping

**Limitations**

Certificate transparency data is retrospective, and a missing subdomain means nothing. Some sources need API keys for better coverage.

**Links:** [GitHub](https://github.com/projectdiscovery/subfinder) &nbsp;·&nbsp; [Site](https://projectdiscovery.io)

---

### Photon

> A fast crawler built for open-source collection.

`s0md3v/Photon` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Web Intelligence & OSINT |
| **License** | GPL-3.0 |
| **Stars** | 13.2k |
| **Forks** | 1.7k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-04) |
| **Self-hostable** | yes |

**VC use case**

Pull the links, keys, endpoints, and files a site exposes, which is how you find out what a company has published without meaning to. Used in a light technical screen before a call.

**Why it's interesting**

It collects the useful artefacts rather than a page dump, and it is fast enough to run over a target set quickly.

**Good for**

- Technical screening
- Site inventory
- Data collection

**Limitations**

Crawls whatever you point it at, so rate and scope need care, and the target can see the traffic. Findings need interpretation.

**Links:** [GitHub](https://github.com/s0md3v/Photon)

---

### BBOT

> A recursive scanner that follows what it discovers.

`blacklanternsecurity/bbot` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Web Intelligence & OSINT |
| **License** | AGPL-3.0 |
| **Stars** | 10.6k |
| **Forks** | 922 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-07) |
| **Self-hostable** | yes |

**VC use case**

Maps a company's real internet footprint, including subsidiaries and forgotten subdomains. Useful before signing: a target that does not know its own attack surface is a diligence finding in itself.

**Why it's interesting**

It recurses, so a single domain can expand into a full picture without manual iteration. The output is structured rather than a wall of text.

**Good for**

- Technical due diligence
- Attack surface mapping
- Subsidiary discovery

**Limitations**

Active scanning is not passive reconnaissance: some techniques are detectable and may breach terms or law depending on the target. Get authorisation.

**Links:** [GitHub](https://github.com/blacklanternsecurity/bbot) &nbsp;·&nbsp; [Site](https://www.blacklanternsecurity.com/bbot/)

---

### httpx

> Probe many hosts at once and report what is live.

`projectdiscovery/httpx` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Web Intelligence & OSINT |
| **License** | MIT |
| **Stars** | 10.4k |
| **Forks** | 1.1k |
| **Language** | Go |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

The companion to subdomain discovery: given a list of hosts, report which respond, with what technologies, certificates, and status. It turns a raw hostname list into an inventory an analyst can read.

**Why it's interesting**

It handles large lists with sensible concurrency and emits structured output, so it feeds a database rather than producing a text dump.

**Good for**

- Infrastructure inventory
- Technical screening
- Stack detection

**Limitations**

Active probing: it sends requests, so the target sees them. Technology detection can be wrong.

**Links:** [GitHub](https://github.com/projectdiscovery/httpx) &nbsp;·&nbsp; [Site](https://docs.projectdiscovery.io/tools/httpx)

---

### OpenCTI

> A structured platform for intelligence about entities and their links.

`OpenCTI-Platform/opencti` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Web Intelligence & OSINT |
| **License** | unverified (Other) |
| **Stars** | 10k |
| **Forks** | 1.4k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

The graph model fits venture research well: companies, people, and relationships as typed objects, with sources attached. A fund tracking a sector can keep a structured picture instead of scattered documents.

**Why it's interesting**

It enforces a data model and provenance on intelligence work, which is why it is used by national CERTs. Applying that discipline to private-market research is a genuine upgrade over notes in a doc.

**Good for**

- Entity tracking
- Relationship mapping
- Structured research

**Limitations**

Heavy to deploy, with several services and a real learning curve. Built for threat intelligence, so the vocabulary takes adapting.

**Links:** [GitHub](https://github.com/OpenCTI-Platform/opencti) &nbsp;·&nbsp; [Site](https://opencti.io)

---

### reNgine

> Recon-as-a-service with a web interface.

`yogeshojha/rengine` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Web Intelligence & OSINT |
| **License** | GPL-3.0 |
| **Stars** | 8.8k |
| **Forks** | 1.3k |
| **Language** | HTML |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

A team-facing way to run and track reconnaissance across many target domains, with scan history and a database behind it. Useful for a fund or platform team that screens companies regularly rather than once.

**Why it's interesting**

It stores results over time, so you can see what changed since the last scan instead of starting over. That is what turns recon into an ongoing process.

**Good for**

- Repeated screening
- Technical due diligence
- Portfolio monitoring

**Limitations**

Operationally heavy for what most funds need, and active scanning carries the same authorisation requirements as any other recon tool.

**Links:** [GitHub](https://github.com/yogeshojha/rengine) &nbsp;·&nbsp; [Site](https://yogeshojha.github.io/rengine/)

---

### Flowsint

> Graph-based investigations you can see.

`reconurge/flowsint` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Web Intelligence & OSINT |
| **License** | Apache-2.0 |
| **Stars** | 7.8k |
| **Forks** | 977 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-06) |
| **Self-hostable** | yes |

**VC use case**

Investigate an entity by following the graph: a person to their companies, those to their addresses and domains. For competitive research or checking whether two startups share founders or investors, the visual graph finds links a spreadsheet hides.

**Why it's interesting**

It makes the investigation itself the interface, so the path from a name to a conclusion is visible and reviewable rather than buried in a script.

**Good for**

- Relationship mapping
- Competitive research
- Investigation

**Limitations**

Early project. Built for security investigations, so some entity types and connectors need adapting for company research.

**Links:** [GitHub](https://github.com/reconurge/flowsint) &nbsp;·&nbsp; [Site](https://flowsint.io)

---

### Osmedeus

> Chains security tools into repeatable reconnaissance workflows.

`j3ssie/osmedeus` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Web Intelligence & OSINT |
| **License** | MIT |
| **Stars** | 6.6k |
| **Forks** | 1k |
| **Language** | Go |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

Standardises a technical screening process so every target gets the same treatment and the output is comparable across companies. That comparability is what makes a diligence finding defensible.

**Why it's interesting**

It orchestrates existing tools through declarative workflows, so the process is documented in code rather than in someone's head.

**Good for**

- Technical due diligence
- Process standardisation
- Repeatable screening

**Limitations**

Workflow definitions need maintaining as the underlying tools change. Same authorisation caveats as any active scanning.

**Links:** [GitHub](https://github.com/j3ssie/osmedeus) &nbsp;·&nbsp; [Site](https://www.osmedeus.org/)

---

### dnstwist

> Finds lookalike domains around a brand.

`elceef/dnstwist` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Web Intelligence & OSINT |
| **License** | Apache-2.0 |
| **Stars** | 5.7k |
| **Forks** | 852 |
| **Language** | Python |
| **Status** | Dormant (last push 2025-04-15, 17mo) |
| **Self-hostable** | yes |

**VC use case**

Detect typo-squatting and phishing sites aimed at a portfolio company, and check whether a target has been quietly buying defensible domain variants. A concrete, checkable input to a security review.

**Why it's interesting**

It generates permutations and then checks which resolve and what is behind them, so results are live domains rather than speculation.

**Good for**

- Security review
- Brand protection
- Portfolio monitoring

**Limitations**

Fuzz results include legitimate lookalikes, so each hit needs a look. Some detection features depend on external services.

**Links:** [GitHub](https://github.com/elceef/dnstwist) &nbsp;·&nbsp; [Site](https://dnstwist.it)

---

### IVRE

> Run your own internet-wide scan database instead of renting one.

`ivre/ivre` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Web Intelligence & OSINT |
| **License** | GPL-3.0 |
| **Stars** | 4.1k |
| **Forks** | 700 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-10) |
| **Self-hostable** | yes |

**VC use case**

Build and query your own inventory of internet-exposed infrastructure, including historical scans. For technical diligence this answers what a target exposed and when, using data you hold rather than a commercial lookup.

**Why it's interesting**

The scan data accumulates, so history becomes queryable. Passive data from public sources can be loaded without scanning anything yourself.

**Good for**

- Infrastructure research
- Historical exposure
- Technical due diligence

**Limitations**

Operating a scanner and its database is not a small job. Active scanning requires authorisation and there are legal limits by jurisdiction.

**Links:** [GitHub](https://github.com/ivre/ivre) &nbsp;·&nbsp; [Site](https://ivre.rocks/)

---

### Playwright

> Drive Chrome, Firefox, and WebKit from code.

`microsoft/playwright` &nbsp;·&nbsp; 🛠 **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Web Intelligence & OSINT |
| **License** | Apache-2.0 |
| **Stars** | 96k |
| **Forks** | 6.4k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

The foundation for any workflow that needs a real browser: logging into a portal and pulling a report, capturing a screenshot for evidence, or checking that a portfolio company's signup flow still works. Test and scrapers share the same tool.

**Why it's interesting**

Maintained by Microsoft with cross-browser support and auto-waiting that removes most flakiness. It is the dependable choice for browser work.

**Good for**

- Browser automation
- Evidence capture
- Product testing

**Limitations**

Needs browser binaries installed and a fair amount of memory per instance. Site terms apply to whatever you automate.

**Links:** [GitHub](https://github.com/microsoft/playwright) &nbsp;·&nbsp; [Site](https://playwright.dev)

---

### Puppeteer

> Control Chrome from JavaScript.

`puppeteer/puppeteer` &nbsp;·&nbsp; 🛠 **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Web Intelligence & OSINT |
| **License** | Apache-2.0 |
| **Stars** | 95.6k |
| **Forks** | 9.6k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-09) |
| **Self-hostable** | yes |

**VC use case**

The browser automation tool most internal dashboards and scrapers get built on when the team works in JavaScript. Rendering a client-side app to capture what it shows, or driving a portal that has no API.

**Why it's interesting**

It is the reference implementation for Chrome automation, with the deepest access to DevTools features, which matters when a page resists simpler tools.

**Good for**

- Browser automation
- JS-rendered pages
- Evidence capture

**Limitations**

Chrome-only, and the maintainers position Playwright as the cross-browser option. Memory use is high at scale.

**Links:** [GitHub](https://github.com/puppeteer/puppeteer) &nbsp;·&nbsp; [Site](https://pptr.dev)

---

### Scrapy

> The long-standing Python framework for crawling sites at scale.

`scrapy/scrapy` &nbsp;·&nbsp; 🛠 **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Web Intelligence & OSINT |
| **License** | BSD-3-Clause |
| **Stars** | 64.3k |
| **Forks** | 11.9k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-10) |
| **Self-hostable** | yes |

**VC use case**

When a fund needs its own dataset, a directory of companies, a set of filings, or every job posting in a sector, this is the tool that collects it reliably. Most bespoke venture data pipelines start here.

**Why it's interesting**

Fifteen years of production use, a stable API, and an ecosystem of middleware for retries, throttling, and proxies. Boring in the way that matters when a cron job has to work every week for a year.

**Good for**

- Dataset collection
- Market research
- Technical due diligence

**Limitations**

Does not run JavaScript, so single-page apps need a separate renderer. Polite crawling requires configuration, and site terms still apply.

**Dependencies:** Python 3.9+

**Links:** [GitHub](https://github.com/scrapy/scrapy) &nbsp;·&nbsp; [Site](https://scrapy.org)

---
