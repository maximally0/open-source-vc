# repos/

This directory is intentionally not used to vendor third-party source code.

Curated projects are **linked**, not copied. The reasoning — licence entanglement, attribution loss, immediate staleness, and a repository nobody can clone — is set out in [docs/LOCAL_COPIES.md](../docs/LOCAL_COPIES.md).

If you want the projects on your own machine, they belong in `clones/`, which is git-ignored:

```bash
./scripts/clone_repos.sh --tier essential
```

The four tier folders the original brief imagined (`essential/`, `interesting/`, `experimental/`, `infrastructure/`) are expressed instead as the `tier` field on every entry in [`metadata/repositories.json`](../metadata/repositories.json), which is sortable, filterable, and cannot go stale.

No source code from any listed project is redistributed in this repository.
