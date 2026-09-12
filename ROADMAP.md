# Roadmap

Where this is going. Ordered by what would actually make the directory more useful, not by what is easiest to build.

---

## Now (v1.0)

- ✅ Curated directory across the full venture workflow
- ✅ Verified metadata pipeline — every fact traceable to the GitHub API, timestamped
- ✅ Weekly drift detection with a human review queue
- ✅ Structured data export (`repositories.json` / `.yaml`) for building on top of
- ✅ Validation in CI: schema, duplicates, licences, attribution, dead links
- ✅ Starter Pack, Hidden Gems, workflow map, comparison matrix

## Next

**Coverage: the blind spots this pass could not reach.**
The highest-value additions are the projects that public search cannot find — tooling built inside funds and never announced, non-English ecosystems, and work hosted outside GitHub. This needs people, not queries: the most reliable path is readers telling us what is missing from their own stack.

**Contributor counts where they exist.**
Currently `unknown` across most entries, because the endpoint is expensive and a guess would be worse than a gap. Worth filling in properly for Essential-tier entries at least.

**Category-level "choose between these" guides.**
`COMPARISON.md` gives you a matrix. What it does not do is make the argument: *if you are a fund of this size, doing this kind of deal, pick X over Y, and here is what you give up.* That is the thing a new analyst actually needs, and it takes real writing.

**Datasets, treated as first-class.**
Software is well covered. Datasets are currently thinner, and the licence situation for data is messier than for code — non-commercial clauses and attribution requirements that catch people out. Each one needs the same treatment as a software entry: what it contains, what it costs to use, what breaks.

**Standards and schemas, expanded.**
Cap-table formats, financial reporting schemas, legal document structures. Unglamorous and disproportionately valuable, because a standard is the decision you only get to make once.

## Later

- **A generated static site** built from `metadata/repositories.json` — search and filtering over the directory without cloning it. The data model already supports this; it is a rendering problem.
- **`llms.txt` and structured feeds** so that agentic tools can consume the directory directly rather than scraping the README.
- **Historical tracking.** The weekly snapshots already accumulate; turning them into "this project's trajectory" charts would show maturity and decay that a single star count hides.
- **Per-tier change alerts.** Notify watchers when an Essential entry goes archived or changes licence, rather than burying it in a weekly PR.
- **A "build this yourself" track** — small reference implementations showing the components from [guides/build-your-own-vc-stack.md](guides/build-your-own-vc-stack.md) wired together, so the guide is executable rather than descriptive.

## Explicitly not planned

- **Becoming a product.** No hosted service, no paid tier, no company. This is a directory.
- **A funding database.** Compiling proprietary private-company data is a different job with different legal exposure. The directory points at tools; it does not become the data.
- **Numeric quality scores.** See [METHODOLOGY.md](METHODOLOGY.md#why-no-84100). Without a defensible methodology they are fake precision.
- **Breadth for its own sake.** Several thousand entries with no judgement applied is a search engine, and GitHub already has one.

## How to influence this

Open an issue. Arguments that change priorities are the ones tied to a specific workflow problem — "I tried to do X and the directory left me stuck at Y" beats "you should add category Z."

If you maintain a project that belongs here, submit it. If you think an entry is wrong, correct it. Corrections outrank everything on this page.
