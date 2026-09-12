# Founder & Talent Discovery

_Finding the people before the round exists._

Founder discovery, technical-talent search, GitHub intelligence, developer discovery, identity resolution, and talent graphs.

**8 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-12

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

**Coverage note.** The tools here are general-purpose people and web research rather than venture-specific talent software. There is no open equivalent of a technical talent graph or a founder database, because those are built on proprietary professional-network data. What an analyst gets from this category is the ability to verify and enrich a person's public footprint independently, which is often enough.

---

### Sherlock

> Find an account on 400+ sites from a username alone.

`sherlock-project/sherlock` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Founder & Talent Discovery |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 91.4k |
| **Forks** | 10.8k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

When a founder's name is common or their LinkedIn is thin, an analyst runs the handle they use elsewhere through Sherlock to see where else that handle exists. That confirms the person matches the deck and often turns up public work that never made it onto a resume.

**Why it's interesting**

It needs no API keys and no accounts. Results are links you can open and read yourself, which matters when the output is going into an investment memo rather than a hobby project.

**Good for**

- Founder background checks
- Identity resolution
- Reference hunting

**Limitations**

A hit is a username match, not proof of identity. Coverage shifts as sites change their responses, and some sites rate-limit or block outright.

**Dependencies:** Python 3.9+, no API keys required

**Links:** [GitHub](https://github.com/sherlock-project/sherlock) &nbsp;·&nbsp; [Site](https://sherlockproject.xyz)

---

### Web-Check

> A full external read of any website from a single URL.

`lissy93/web-check` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Founder & Talent Discovery |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 34.8k |
| **Forks** | 2.8k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-10) |
| **Self-hostable** | yes |

**VC use case**

Point it at a target company's domain and get its hosting, DNS and mail records, TLS configuration, exposed headers, and third-party services. That is the ten-minute technical screen an associate runs before a first call, and it usually surfaces something the deck did not mention.

**Why it's interesting**

It reads what the site publicly publishes rather than guessing, runs as a single page, and needs no setup. Findings are the raw records, so they are checkable.

**Good for**

- Technical screening
- Competitor stack research
- Pre-meeting preparation

**Limitations**

Only shows what is externally visible. A clean report is not a clean bill of health, and a missing finding is not evidence of absence.

**Links:** [GitHub](https://github.com/lissy93/web-check) &nbsp;·&nbsp; [Site](https://web-check.xyz)

---

### Maigret

> Build a dossier on a person from one username.

`soxoj/maigret` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Founder & Talent Discovery |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 37.5k |
| **Forks** | 2.9k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

Produces a report across 3,000+ sites from a single handle, including account metadata and extracted profile fields where the site exposes them. Useful when checking whether a claimed technical founder or advisor has any public footprint at all, which is often the fastest way to spot an inflated bio.

**Why it's interesting**

It scores confidence per hit and can emit a PDF or HTML report, so findings can be filed as evidence instead of pasted as loose links.

**Good for**

- Founder vetting
- Advisor credential checks
- Due diligence support

**Limitations**

Reports are only as good as what is public, and common usernames produce false positives. Treat every result as a lead to confirm.

**Links:** [GitHub](https://github.com/soxoj/maigret) &nbsp;·&nbsp; [Site](https://maigret.app/gh)

---

### theHarvester

> Emails, subdomains, and names tied to a domain.

`laramies/theHarvester` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Founder & Talent Discovery |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unknown |
| **Stars** | 17.4k |
| **Forks** | 2.6k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-10) |
| **Self-hostable** | yes |

**VC use case**

A first pass on a company you have no relationship with: it collects public emails, hostnames, and employee names from search engines and certificate logs. Useful for working out how large a team really is and who to approach.

**Why it's interesting**

Certificate transparency and search-engine sources are queried together, so a company's real infrastructure footprint shows up even when the marketing site hides it.

**Good for**

- Company reconnaissance
- Contact discovery
- Team sizing

**Limitations**

No licence file is present in the repository, so redistribution and some commercial uses are unclear. Check with counsel before shipping anything built on it, and note that a missing licence is reported here rather than assumed away.

**Links:** [GitHub](https://github.com/laramies/theHarvester) &nbsp;·&nbsp; [Site](http://www.edge-security.com/)

---

### OSINT Framework

> A map of where to look, organised by what you already have.

`lockfale/OSINT-Framework` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Founder & Talent Discovery |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 12.1k |
| **Forks** | 2k |
| **Language** | JavaScript |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

When a background check feels incomplete, this is the checklist that tells you what other public sources exist for the thing you hold: a username, an email, a domain, a phone number. Analysts new to research use it to learn the terrain once.

**Why it's interesting**

It is a working web interface over a maintained index, and it groups tools by category rather than pretending every link is equally worth opening.

**Good for**

- Research training
- Background checks
- Source discovery

**Limitations**

Many listed links are stale or lead to commercial products. Nothing here checks the links for you.

**Links:** [GitHub](https://github.com/lockfale/OSINT-Framework) &nbsp;·&nbsp; [Site](https://osintframework.com)

---

### JobSpy

> Job postings from five boards into one dataframe.

`speedyapply/JobSpy` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Founder & Talent Discovery |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 4.3k |
| **Forks** | 843 |
| **Language** | Python |
| **Status** | Active (last push 2026-02-18) |
| **Self-hostable** | yes |

**VC use case**

A fund watching a sector can track which startups are hiring, for which functions, and how fast, without buying a labour-market dataset. Headcount movement by team is one of the few signals a private company cannot easily dress up.

**Why it's interesting**

It covers LinkedIn, Indeed, Glassdoor, Google, and ZipRecruiter behind one interface and returns a typed frame, so a hiring signal can be built in an afternoon rather than a data-engineering project.

**Good for**

- Sourcing signals
- Market research
- Portfolio monitoring

**Limitations**

Upstream layout changes break scrapers without warning, and collecting from these boards may breach their terms of service. Check that before running it at scale.

**Links:** [GitHub](https://github.com/speedyapply/JobSpy)

---

### Instaloader

> Download public Instagram posts and their metadata.

`instaloader/instaloader` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Founder & Talent Discovery |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 13.4k |
| **Forks** | 1.6k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-06) |
| **Self-hostable** | yes |

**VC use case**

For consumer and creator-facing companies, a founder's or brand's Instagram is part of the evidence trail: posting cadence, engagement, and how long they have been at it. This gathers that into files an analyst can review.

**Why it's interesting**

It captures metadata alongside media and can resume interrupted runs, which makes it practical for watching an account over time rather than taking one snapshot.

**Good for**

- Founder research
- Consumer brand research

**Limitations**

Instagram actively blocks bulk collection, so expect throttling and account losses. Public content only, and the platform's terms still apply to how you use it.

**Links:** [GitHub](https://github.com/instaloader/instaloader) &nbsp;·&nbsp; [Site](https://instaloader.github.io/)

---

### linkedin_scraper

> Pull LinkedIn profiles and company pages into structured data.

`joeyism/linkedin_scraper` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Founder & Talent Discovery |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | GPL-3.0 |
| **Stars** | 4.5k |
| **Forks** | 987 |
| **Language** | Python |
| **Status** | Active (last push 2026-04-10) |
| **Self-hostable** | yes |

**VC use case**

Build a sourcing database from profile and company pages, including positions and tenure. Funds use it to answer questions like how long a founding team has worked together and who reported to whom.

**Why it's interesting**

Runs in a real browser session and returns typed fields rather than screenshots, which is what makes the output usable in a database instead of a folder of saves.

**Good for**

- Sourcing databases
- Team research

**Limitations**

LinkedIn's terms prohibit automated collection and accounts get restricted for it. Use only where you accept that risk; prefer licensed data for anything systematic.

**Links:** [GitHub](https://github.com/joeyism/linkedin_scraper)

---
