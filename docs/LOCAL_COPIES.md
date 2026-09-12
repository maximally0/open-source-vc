# Local Copies

Why this repository links to projects instead of vendoring them, and how to get them onto your own machine when you want them.

---

## The decision

The brief that started this project suggested cloning the strongest repositories into the directory itself, "where legally permitted." That is permitted for most of what is listed here — MIT and Apache-2.0 both allow redistribution with attribution. This repository still does not do it, deliberately.

**What vendoring a few hundred projects actually produces:**

- **A fork that goes stale immediately.** Every vendored copy is a snapshot frozen at the moment of copying. Six months later a reader cannot tell whether they are looking at current upstream code or a year-old copy. A directory's job is to point at the live thing.
- **Licence entanglement.** Nesting hundreds of differently licensed trees under one repository means the whole bundle's licence status becomes a question nobody can answer quickly. `LICENSE` files collide, notices get dropped, and a permissive directory quietly becomes a copyleft one because one dependency is AGPL.
- **Attribution loss.** Redistributed code is where attribution breaks. The upstream `README`, the copyright headers, the `NOTICE` files — every one is an opportunity to lose the thread back to the maintainer who did the work. Preserving them perfectly across 200 repositories is not a one-off cost; it is a permanent maintenance burden.
- **A repository nobody can clone.** Tens of gigabytes. Slow, unsearchable, and the actual curation — the part with value — gets lost in it.
- **Zero benefit to the reader.** The code is already public, already versioned, already installable. A stale copy in a directory repo adds nothing over a link.

The brief anticipated this: it lists metadata-only linking as a valid option and warns against the repository becoming "an unmanageable 50GB dumping ground." That is the option taken.

**So: no source code from any listed project is redistributed here.** What this repository contains is prose, structured metadata, and scripts — all first-party, all CC0.

## What that means for you

Every entry has a verified upstream link. To work with a project, you clone it from its own home, where you get current code, real issues, and the maintainers' own documentation.

If you want the local copies the brief described, get them on your machine rather than in this repository:

```bash
# clone every project in the directory into ./clones/<category>/<name>
./scripts/clone_repos.sh

# just the ⭐ Essential tier
./scripts/clone_repos.sh --tier essential

# one category
./scripts/clone_repos.sh --category document-intelligence

# shallow, faster (no history)
./scripts/clone_repos.sh --shallow --tier essential
```

`clones/` is git-ignored. Nothing you clone can accidentally end up committed.

## Licensing, if you redistribute anything

Once you have clones locally, the licences are yours to respect. The directory reports each project's licence in its entry and in `metadata/repositories.json`, so you can check before you copy code into anything you ship.

- **Permissive** (`MIT`, `Apache-2.0`, `BSD-*`, `ISC`, `0BSD`, `Unlicense`, `CC0-1.0`) — redistribution fine; keep the copyright notice and licence text.
- **Weak copyleft** (`MPL-2.0`, `LGPL-*`) — file-level obligations; keep modified files under the same licence.
- **Strong copyleft** (`GPL-*`) — distributing a derivative means the derivative is GPL.
- **AGPL** — as GPL, plus network use can trigger source-disclosure. This is the one that surprises people building internal tools.
- **`unverified`** — no licence file detected upstream. Treat redistribution as prohibited until you have confirmed otherwise.
- **`CC-BY-NC-*`** — non-commercial. Common with datasets, and easy to violate without noticing.

`scripts/clone_repos.sh` prints the licence of each project as it clones, so the information is in front of you at the moment it matters.

This is a summary of what the projects say about themselves, not legal advice. If a licence decision is material to your fund, read the upstream `LICENSE` and speak to counsel.
