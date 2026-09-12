# Sources

Where candidates came from. Everything listed in this file was a **lead**, not a citation — every entry in the directory was then verified against the project itself, which is the standard described in [METHODOLOGY.md](METHODOLOGY.md).

---

## Primary discovery surfaces

**GitHub search and topics.** The backbone of the discovery pass. Queries were deliberately not limited to VC vocabulary: searching only for `venture capital` and `vc` returns a thin, mostly abandoned set. The productive queries were the adjacent ones — `pdf parsing`, `entity resolution`, `change detection website`, `cap table`, `contract analysis nlp`, `topic:mcp` — because most of the infrastructure a VC analyst actually uses has never heard of venture capital.

Two sort orders were used on purpose:

- `sort=stars` to find adopted, mature projects
- `sort=updated` to find emerging projects that a star ranking would bury under a decade of accumulated attention

The candidate pool is intentionally several times the size of the final list. Coverage is the easy part; the tedium is the filtering.

## Secondary leads

| Source | Used for |
|---|---|
| Prior curated lists and awesome-lists | Identifying gaps and long-standing recommendations worth re-checking |
| Hacker News | Projects with engineering credibility before they have stars |
| Product Hunt | Commercial tools, mostly to find the open-source alternative and to name the gap |
| Reddit and developer communities | Practitioner commentary — what people actually run, and what broke |
| Papers With Code, arXiv, academic work | Document intelligence, entity resolution, and graph approaches not yet productised |
| Hugging Face | Datasets, embeddings, and document-understanding models |
| Company engineering blogs | Internal tooling that was open-sourced late, or never announced |
| SEC EDGAR and public filings | Standards, schemas, and financial data formats |
| Project documentation and repos themselves | Licence, maintenance status, and actual capability |

## Things worth knowing about the sources

**Awesome-lists age badly.** They were treated as leads to re-verify, never as authorities. A significant share of entries in older VC and fintech lists are archived, unlicensed, or link to a landing page. Re-checking them was some of the most useful work in this project, and also some of the least visible.

**Star counts are a lagging indicator.** Several of the strongest entries have modest star counts because their audience is small and professional. Several very popular entries were excluded because they are a tutorial wearing a framework's clothes.

**Commercial product pages are useful in reverse.** The most reliable way to find the open-source option in a category is to read what the paid products in that category say they replace.

**Private and internal tooling is the blind spot.** Repositories used inside funds and never published cannot be found by any search, and are almost certainly the most valuable category missing here. If you know of one, [open an issue](../../issues/new).

## What sources were deliberately not used as evidence

Search-result snippets, AI-generated summaries, aggregator sites that mirror GitHub metadata without dates, and any "top 50 tools" listicle without a stated methodology. These are how wrong licence and maintenance claims propagate through the ecosystem, and they are the specific failure this directory is built to avoid.

## Verifying a claim yourself

Every entry carries the GitHub API state recorded at the timestamp in `metadata/snapshot.json`, and the mechanism is public:

```bash
python scripts/update.py --repos-only owner/repo   # re-read live state for one project
python scripts/verify.py                           # re-check every link and licence
```

If you believe an entry is wrong, the [correction template](../../issues/new?template=correction.yml) asks for the source. That is not bureaucracy — a correction without evidence cannot be distinguished from a guess, and guesses are how a directory like this dies.
