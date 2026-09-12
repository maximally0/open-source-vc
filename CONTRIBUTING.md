# Contributing

Two ways to help, in order of value.

1. **Corrections.** A wrong licence, a dead link, a "maintained" project that has not seen a commit in three years. These get priority over everything else, because accuracy is the entire product.
2. **Submissions.** A project that belongs here and is not here yet.

Read [METHODOLOGY.md](METHODOLOGY.md) first. It is the spec; this page is the practical version.

---

## The bar

Before you submit, the project must pass all of these. Be honest with yourself — a rejected submission costs you five minutes here, but a bad entry costs every reader who trusts it.

- [ ] **Genuinely open source**, with a licence visibly present in the repository.
- [ ] **Contains working code or real data.** Not a landing page, not a thin API wrapper, not a prompt collection.
- [ ] **Not abandoned.** Recent commits, or a clear reason it is complete and finished.
- [ ] **A specific VC use case exists**, and you can name the task it replaces or accelerates.
- [ ] **Not a duplicate** of something already listed. Search the README and `metadata/repositories.json` first.
- [ ] **Documented well enough** that a competent stranger could install and use it.

## The single most common reason for rejection

Not quality. **A vague use case.**

> ✗ "Useful for investors and analysts."

That sentence is compatible with approximately nine thousand repositories and tells the reader nothing. It will be rewritten or the submission closed.

> ✓ "An associate doing technical DD on a Series A devtools company can pull the target's GitHub org, measure contributor concentration, and see whether commit cadence dropped after the last raise. Replaces about an hour of manual clicking per company."

Name the person, the task, and ideally the thing it replaces. If you cannot do that, the project probably does not have a clear VC use case — which is fine, and worth knowing early.

## What will be rejected

- Closed-source products, and paid products whose OSS component is marketing.
- Model wrappers with no engineering substance.
- Prompt collections, link lists, and abandoned tutorials.
- Repositories that exist to rank in search rather than to work.
- Unclear provenance, or no discernible licence.
- A second implementation of something already listed, where the difference is cosmetic.
- Anything whose primary purpose is unethical or illegal. Security and OSINT tooling is welcome where the legitimate research, diligence, or defensive use case is explicit; stalking, doxxing, credential theft, and unauthorised access are not.

## How to submit

Open a [repository submission issue](../../issues/new?template=repository-submission.yml). The form asks for everything needed. Alternatively, edit `curation.yaml` directly and open a pull request.

### Editing `curation.yaml` directly

```yaml
repos:
  - name: owner/repo                    # required, exact, owner/repo
    category: due-diligence             # required, must match a page in categories/
    tier: interesting                   # essential | interesting | experimental | infrastructure | research
    kind: software                      # software | dataset | framework | standard | research
    tagline: >                          # optional; falls back to the upstream description
      One line, accurate.
    vc_use_case: >                      # required, specific
      Who does what, and what it replaces.
    why_interesting: >                  # required
      What it does that the obvious alternative does not.
    good_for:                           # at least one
      - Technical DD
      - Portfolio monitoring
    limitations: >                      # strongly encouraged — every tool has them
      Rate limits, licence terms, maintenance risk, cost, missing features.
    vc_native: false                    # built explicitly for venture / private markets?
    ai: true                            # is the core function model-dependent?
    self_hostable: true                 # true | false | partial
    hidden_gem: false                   # small, brilliant, or underrepresented?
    starter: false                      # belongs in the Starter Pack?
    docs: https://example.com/docs
    demo: https://demo.example.com
    dependencies: "Python 3.11+, Postgres 14+"
    installation: "pip install example"
    notes: >
      Anything else a reader needs.
```

Then, locally:

```bash
pip install -r requirements.txt
python scripts/update.py --repos-only owner/repo   # verify the repo and fetch real metadata
python scripts/generate_index.py                   # regenerate every derived page
python scripts/verify.py --offline                 # catch mistakes before CI does
```

Commit `curation.yaml`, `metadata/snapshot.json`, and the regenerated pages together. CI rejects a pull request where the generated files are stale.

If you are not comfortable with Python, just open the issue — maintainers will do the mechanics.

## Metadata rules

1. **Never invent a number.** Stars, forks, and dates come from the API. If you are hand-editing `metadata/`, do not guess.
2. **Never guess a licence.** Read the `LICENSE` file. No licence means `unverified`, and the entry says so.
3. **Use `unknown`.** If you cannot verify a field, write `unknown`. An honest gap is worth more than a confident error.
4. **Preserve attribution.** Original repository, author, and URL, always. Nothing original is ever stripped.
5. **Flag open core.** If there is a commercial tier, say what is open and what is not.

## How review works

1. CI validates structure, schema, duplicates, licences, attribution, and link liveness.
2. A maintainer reads the entry and may rewrite the use case for tone and specificity. This is normal.
3. The tier is assigned by the maintainer, not the submitter. It is editorial, and disagreement is welcome in the thread.
4. Merged entries appear on the next regeneration and in [CHANGELOG.md](CHANGELOG.md).

Reviews are not fast and there is no SLA. This is maintained alongside other work.

## Reporting a correction

Use the [correction template](../../issues/new?template=correction.yml). Include **evidence and a link** — the `LICENSE` file, the API response, the commit, the release. Corrections without a source cannot be merged, no matter how right they are.

## Licence of contributions

By contributing you agree that your prose and metadata contributions are released under [CC0-1.0](LICENSE), matching the rest of the directory. You keep the rights to your own work; you are simply placing these contributions in the public domain alongside it.

## Code of conduct

Be direct, be specific, be kind about it. Argue with the tier, not with the person who assigned it. Corrections are welcome at any time, including to this page.
