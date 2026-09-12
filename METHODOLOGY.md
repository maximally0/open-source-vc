# Methodology

Why the directory contains what it contains, and how every field got there. This page exists so you can decide how much to trust a given entry, and so disagreements are about substance rather than vibes.

---

## The one rule that shapes everything

**Nothing is stated that was not verified against the project itself.**

This sounds obvious. In practice almost every curated list breaks it: stars get copied from a screenshot, licences get guessed from the README badge, "actively maintained" gets decided by a glance at the landing page. That is how a directory becomes useless within a year — worse than useless, because people make decisions on it.

So the split is explicit:

| Data | Source | Trust level |
|---|---|---|
| Stars, forks, language, last push, archived status, licence, creation date | GitHub API, read by `scripts/update.py` | Machine-verified, timestamped |
| Category, tier, VC use case, why it is interesting, limitations | Human curation in `curation.yaml` | Editorial judgement — argue with it |
| Contributor counts, funding, adoption, internal usage | Frequently **unavailable** | Reported as `unknown` |

When a field cannot be verified, it says `unknown` or `unverified`. It is never estimated, and never left out so the entry looks cleaner than it is. A missing licence is reported as a missing licence, because that is exactly the fact you need to know before putting a dependency in your fund's stack.

## Tiers

Quality, and nothing else. Four labels, no numeric scores.

| | Tier | Applied when |
|---|---|---|
| ⭐ | **Essential** | An analyst installs this in week one and it unblocks real work. If it disappeared, a core task would get materially harder. |
| 🔥 | **Recommended** | Strong fit, narrower in scope, or better once you already have a stack. Also where excellent infrastructure lands, because "excellent" and "install this first" are different claims. |
| 🧪 | **Experimental** | Early stage, incomplete, possibly important. Listed with the caveats stated. |
| 📚 | **Research** | You are not going to deploy it. It is here because the approach, dataset, or result will change how you think about the problem. |

## VC relevance

A separate axis, and the separation is the point. It answers a different question from the tier:

| | Relevance | Meaning |
|---|---|---|
| ◆ | **VC-native** | Built for venture capital, private markets, fund operations, or startup investing. |
| ◇ | **VC-adaptable** | A general tool a fund adopts directly for a specific venture task. |
| ▫ | **Infrastructure** | A building block you construct venture tooling with, not something an analyst uses standalone. |

**Only 14 of the projects here are VC-native.** The rest are either general tools with a clear venture application or components you assemble. That ratio is a finding about the ecosystem, not about the curation: venture-specific software is a commercial category and very little of it is open source.

**Why the two axes are separate.** An earlier version of this directory used one scale that mixed quality with kind, including an `infrastructure` tier. The result was predictable: the top tier filled with whatever had the most stars, and a reader scanning the category index concluded there were far more venture-native tools than there are. A PDF parser can be the best tool here for a data room and still have no idea what a data room is. Both facts need to be visible, which requires two fields.

`vc_native` (a boolean, kept for anyone already filtering on it) is derived from `vc_relevance` rather than set by hand, so the two cannot disagree. CI errors if the same value appears in both axes.

For each inclusion, the entry states the specific VC use case. Where a tool is not venture-native, it says so and explains the adaptation.

### Why no `84/100`

Because the methodology behind such a number does not exist, and inventing one produces fake precision that readers will optimise against. Stars measure attention, not usefulness — the most-cited example being that a 40,000-star UI framework is worth less to a VC analyst than a 900-star cap-table model. Popularity is recorded as a fact (`Stars`) and used for sorting within a tier, never as a quality claim.

A multi-dimension rubric was proposed during review of v1.1: score every project on VC relevance, utility, maturity, maintenance, setup cost, data access, extensibility, and differentiation. Every one of those is a fair question. The reason it is not implemented as 236 × 8 published numbers is that the judgements underneath them would not survive the precision. "Setup: 4/5" invites a reader to compare two tools by a score nobody can reproduce or audit, and to trust it more than the one thing the entry does say clearly, which is what the tool is for and what it costs you.

Where those dimensions change a decision, they appear as prose in the entry — the limitations field exists precisely to carry "this needs a GPU", "this is AGPL", "this has not been touched since 2020" — and as the two labelled axes. If a defensible quantitative method is ever published, with weights and failure modes stated here first, the scores can follow.

## What qualifies

A project belongs here if all of the following hold:

1. **It is genuine open source.** A licence is present and its terms permit the use you would make of it. Source-available, fair-code, and "open core with a commercial enterprise tier" projects are labelled as such and are never described as simply "open source".
2. **It contains real code or real data.** A working artefact someone can inspect. Not a landing page, not a wrapper around one API call, not a prompt list.
3. **The VC use case is specific and stated.** The entry must name the task it accelerates and who performs that task. "Useful for investors" is not a use case and gets an entry rejected.
4. **It is discoverable and documented.** Someone with relevant skills can work out how to install and use it without asking the author.
5. **It is not abandoned.** Unless the entry is explicitly `Research`, or labelled so you can see the risk. Archived projects do not appear as active.

## What is excluded

- Closed-source products, and paid products whose open-source component is a marketing artefact.
- Model wrappers with no engineering substance.
- Prompt collections, lists of links, and tutorials that were abandoned mid-sentence.
- SEO bait: repositories that exist to rank rather than to work.
- Repositories with unclear provenance, or no discernible licence.
- Duplicate implementations of something already listed, unless the difference is material — in which case the entry says what the difference is.
- Tools whose primary purpose is unethical or illegal activity.

### On OSINT and security tooling

Some of the most useful tools for diligence are dual-use: they can research a target or they can harass a person. The inclusion test here is whether a clear legitimate use exists — due diligence, fraud and misrepresentation detection, sanctions and KYC screening, security assessment, academic research — and whether the tool's own documentation frames it that way. Tools built for stalking, doxxing, credential theft, or unauthorised access are excluded regardless of quality.

Inclusion is not an endorsement of every use of a tool. Use of personal data is governed by law in your jurisdiction (GDPR, CCPA, and their equivalents), and "it was public" is not a legal defence. That is on you, and it is worth saying plainly.

## Licensing

Licences are read from the repository and reported as published. The taxonomy used:

| Reported as | Meaning |
|---|---|
| `MIT` `Apache-2.0` `BSD-*` `ISC` `0BSD` `Unlicense` `CC0-1.0` | Permissive. Redistribution permitted with attribution. |
| `MPL-2.0` `LGPL-*` `EUPL-1.2` | Weak copyleft. File-level or library-level obligations. |
| `GPL-*` `AGPL-*` | Strong copyleft. **AGPL in particular**: network use can trigger source-disclosure obligations. If you are embedding it in anything you host, read it properly. |
| `CC-BY-*` | Attribution required; not designed for software. |
| `CC-BY-NC-*` | Non-commercial. Check before any commercial use — this catches people out on datasets more than code. |
| `unverified` | No licence file detected. Treat redistribution as prohibited until proven otherwise. |
| `source-available` | Readable source, restrictions beyond OSS. Not open source, and not described as such. |

Open-core projects are annotated explicitly, e.g. *"Core is AGPL; enterprise features are commercial."* The point is that you find out before you build on it, not after.

**None of this is legal advice.** It is a report of what each repository says about itself. If a licence decision is material to your fund, read the upstream `LICENSE` and speak to counsel.

## How an entry gets verified

1. **Discovery.** Broad automated search across GitHub topics and search, plus prior lists, communities, papers, and company engineering blogs as leads. See [SOURCES.md](SOURCES.md). The candidate pool is deliberately much larger than the final list — usually by a factor of five or more.
2. **Inspection.** The repository is opened: README, `LICENSE`, structure, commit history, releases, open issues, install instructions.
3. **Fact extraction.** Metadata is read from the GitHub API by `scripts/update.py` and committed to `metadata/snapshot.json` with a timestamp.
4. **Judgement.** Category, tier, use case, and limitations are written by hand in `curation.yaml`.
5. **Validation.** `scripts/verify.py` checks schema, duplicates, licence presence, archived status, attribution, category coverage, and link liveness. CI fails on errors.
6. **Weekly drift check.** The scheduled workflow re-reads every entry and opens a review queue. Archived, dormant, licence-changed, and unreachable entries surface automatically.

What verification does **not** include: running every project. Entries are not benchmarked, and no claim is made about performance, accuracy, or fitness for a specific purpose. Where the maintainers themselves state a limitation, it is repeated in the entry.

## Known limits of this directory

Stated here rather than buried, because knowing where a map is blank is part of reading it.

- **Coverage is biased toward what is findable.** Projects written in English, documented publicly, and hosted on GitHub are over-represented. Excellent work in other languages, on other forges, or in private use inside funds is missing — the last category is the hardest to find and the most valuable when found.
- **Star counts are a lagging and noisy signal.** Verified as numbers, never treated as quality.
- **Contributor counts are usually `unknown`.** The API endpoint that would give them is expensive and rate-limited, so they are only filled in where individually confirmed rather than estimated across the board.
- **The tier is one person's judgement.** Bias included. The remedy is a well-argued correction, and those get priority over new submissions.
- **Breadth is not neutrality.** A project being listed says nothing about whether you should use it, and nothing about the maintainers beyond what is written in their own repository.
