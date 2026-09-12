# Discovery Record — v1.0.0

How the initial directory was assembled. Kept because a curated list is only as trustworthy as its method, and because the funnel numbers tell you how much filtering happened.

**Result: 10,111 candidates → 2,673 that survived mechanical filtering → 226 curated.**

The raw candidate pool (`research/candidates.json`, about 15 MB) is not committed: it is an intermediate build artefact, and committing it would bloat the repository permanently for no reader benefit. It is reproducible with the scripts below.

---

## Stage 1 — Broad search

`python scripts/discover.py`

| | |
|---|---|
| Search queries | 113 |
| Candidates collected | 10,111 unique repositories |
| Sort orders used | `stars` (adopted projects) and `updated` (emerging ones) |
| Forks | excluded at collection |
| Run at | 2026-09-12 |

The query set covered the venture workflow and the adjacent infrastructure that venture work actually depends on. Deliberately, most queries had nothing to do with venture capital:

| Group | Candidates surfaced |
|---|---:|
| vc-native | 1,369 |
| agents | 1,100 |
| sourcing | 1,100 |
| web-intel | 1,000 |
| finance | 1,000 |
| documents | 900 |
| knowledge | 800 |
| market-research | 800 |
| automation | 700 |
| datasets | 700 |
| relationships | 700 |
| legal | 550 |
| standards | 220 |

**Why so broad.** Searching only for venture-capital vocabulary returns a thin set dominated by abandoned projects and false positives. The `vc-native` group above, for instance, included voice-conversion models (the acronym RVC), hardware accelerators, and cloud landing zones. Broad search found the generic infrastructure well; it found VC-native tooling badly.

**Seeds merged:** 170 candidates arrived through a targeted pass rather than search, described below.

## Stage 2 — Targeted verification

`python scripts/seed_repos.py`

Broad search cannot find what does not describe itself. The second half of discovery was a list of 168 specific repositories worth checking, each fetched directly from the GitHub API and verified before anything else happened.

| | |
|---|---|
| Repositories checked | 168 |
| Resolved | 150 |
| Failed to resolve | 2 — `seriesseed/seriesseed` and `gleif/lei` do not exist |
| Archived, and dropped | 1 — `commoncrawl/commoncrawl` |
| Renamed, canonical name adopted | 1 — `JSv4/OpenContracts` → `Open-Source-Legal/OpenContracts` |
| Archived workflow tool, dropped | 1 — `FlowiseAI/Flowise` |

This is the stage that justified itself. Every one of those five corrections would have become a wrong entry if the list had been written from memory or from a search snippet. The failed lookups are recorded in `research/seeds.txt` alongside the note that both standards live on their own websites rather than on a code forge.

## Stage 3 — Mechanical filtering

`python scripts/shortlist.py --stats`

| Filter | Rejected |
|---|---:|
| Below the star floor | 6,228 |
| No description, or recognisably a list, tutorial, or template | 516 |
| Stale (no push in over 30 months) | 375 |
| Archived upstream | 319 |
| **Remaining** | **2,673** |

The spam filter is narrow on purpose: it catches "awesome list", cheat sheets, interview-question repos, dotfiles, and course material by explicit pattern rather than by taste. Judgement about quality happened later and by hand.

A further signal from this stage: of the 2,673 that passed, 578 had no detectable licence and a further 323 declared only a non-standard one. Licence availability, not popularity, turned out to be one of the strongest predictors of whether a project was usable at all.

## Stage 4 — Curation

`curation.yaml`, written by hand.

226 repositories were selected, categorised, tiered, and given a VC use case and stated limitations. Nothing entered the directory on the strength of a search result alone.

Final shape:

| Tier | Count |
|---|---:|
| ⭐ Essential | 39 |
| 🔥 Interesting | 117 |
| 🧪 Experimental | 36 |
| 🛠 Infrastructure | 20 |
| 📚 Research | 14 |

| Kind | Count |
|---|---:|
| Software | 170 |
| Framework | 35 |
| Research | 10 |
| Dataset | 9 |
| Standard | 2 |

Also selected: 32 projects for the [starter pack](../STARTER_PACK.md) and 38 for [hidden gems](../HIDDEN_GEMS.md).

## Stage 5 — Metadata verification

`python scripts/update.py --with-releases`

All 226 curated repositories were re-fetched from the GitHub API. Stars, forks, licences, creation dates, last push dates, and archived status in `metadata/snapshot.json` are that API response, not typed values.

| | |
|---|---|
| Repositories resolved | 226 of 226 |
| With a standard SPDX licence | 178 |
| With no detectable licence | 8 |
| With a non-standard licence identifier | 40 |
| Archived upstream | 0 |
| Dormant (no push in 12+ months) | 16 |
| New releases detected since caching | 179 |

## What the numbers say

**Filtering was the work.** 10,111 candidates became 226 entries, a ratio of roughly 45 to 1. Coverage was the easy part; deciding what was worth a reader's time was the whole job.

**Star counts were not the selection criterion.** Several of the highest-starred repositories surfaced by search were excluded: apparent SEO projects, prompt collections, and tutorials wearing a framework's clothes. Several of the most useful entries have fewer than a thousand stars, and two have fewer than a hundred.

**Licences are messier than expected.** Roughly one in five curated entries either has no licence file or uses a non-standard identifier. Each is reported as published, and none are described as open source when they are not.

**Some categories are genuinely thin.** Cap tables (3 entries) and LP and fund management (7 entries) are the weakest, because those niches are commercially well served and barely served by open source at all. Each category page carries a coverage note rather than padding.

## Reproducing this

```bash
pip install -r requirements.txt

python scripts/discover.py                          # broad search, ~10 minutes
python scripts/seed_repos.py                        # targeted verification
python scripts/seed_repos.py --file research/seeds-batch3.txt
python scripts/shortlist.py --stats                 # filter funnel
python scripts/update.py --with-releases            # verified metadata for curated repos
python scripts/generate_index.py                    # rebuild every derived page
python scripts/verify.py                            # validate
```

The GitHub API rate limits the search stage to roughly 25 queries a minute, so `discover.py` takes several minutes by design rather than by accident.
