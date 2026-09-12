# Cap Tables & Equity

_Ownership, dilution, and the mechanics of the round._

Cap table modelling, dilution, SAFEs, priced rounds, ownership, liquidation preferences, and equity standards.

**3 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-12

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

**Coverage note.** This is the thinnest category in the directory, and that is a finding rather than an oversight. Cap-table software is one of the most commercially successful niches in venture tooling, and almost none of it is open source: what exists here is a handful of self-hosted platforms and spreadsheet models, several of which are not actively maintained. The relevant standard, [Open Cap Format](../categories/standards.md), is more mature than the tools that implement it. If you are choosing a cap-table system today, the honest advice is that this is one place where paying for software is probably the right call, and the open options are worth knowing about for SPVs, rolling funds, and small vehicles where per-company pricing does not make sense.

---

### Captable

> An open-source cap table management platform.

`captableinc/captable` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ◆ **VC-native** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Cap Tables & Equity |
| **VC relevance** | VC-native — built for venture capital, private markets, fund operations, or startup investing. |
| **License** | AGPL-3.0 |
| **Stars** | 822 |
| **Forks** | 179 |
| **Language** | TypeScript |
| **Status** | Dormant (last push 2025-06-04, 15mo) |
| **Self-hostable** | yes |

**VC use case**

The cap table, dilution modelling, and stakeholder records that every fund currently pays a vendor for. A fund or a founder can run it themselves, which matters most for SPVs, rolling funds, and emerging managers where the per-company pricing is hard to justify.

**Why it's interesting**

This is one of the very few genuinely VC-native open-source products in existence. Cap tables are the one piece of venture infrastructure everybody needs and almost nobody has open source.

**Good for**

- Cap table management
- Dilution modelling
- Fund administration

**Limitations**

AGPL-licensed, which has real obligations if you offer it as a service. Last commit is older than most entries here, so check that it still fits your needs before relying on it.

**Links:** [GitHub](https://github.com/captableinc/captable) &nbsp;·&nbsp; [Site](https://captableinc.com)

---

### Cap Table Worksheet

> A spreadsheet-native cap table that computes the maths properly.

`1984vc/cap-table` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◆ **VC-native** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Cap Tables & Equity |
| **VC relevance** | VC-native — built for venture capital, private markets, fund operations, or startup investing. |
| **License** | MIT |
| **Stars** | 139 |
| **Forks** | 17 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-08-19) |
| **Self-hostable** | yes |

**VC use case**

Most cap tables in venture are spreadsheets, and most of those are subtly wrong. This implements the mechanics from the standards, so a round's dilution, option pool shuffle, and conversion outcomes are computed rather than typed in.

**Why it's interesting**

Someone who understood the arithmetic released the working model. That is a small corner of the market that commercial tools charge a lot to occupy.

**Good for**

- Dilution modelling
- Round modelling
- Founder education

**Limitations**

Small project with limited maintenance history. Verify against a known-good model before relying on it for a real round.

**Links:** [GitHub](https://github.com/1984vc/cap-table) &nbsp;·&nbsp; [Site](https://startup-finance.1984.vc)

---

### Cap Table and Exit Waterfall

> Cap table plus exit waterfall modelling.

`tdavidson/cap-table-tool` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◆ **VC-native** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Cap Tables & Equity |
| **VC relevance** | VC-native — built for venture capital, private markets, fund operations, or startup investing. |
| **License** | unverified (Other) |
| **Stars** | 47 |
| **Forks** | 10 |
| **Language** | unknown |
| **Status** | Dormant (last push 2025-03-10, 18mo) |
| **Self-hostable** | yes |

**VC use case**

The question that decides whether a deal is worth doing at a given price is what the exit proceeds actually return to each class, after preferences and participation. This models that, which is harder than modelling the round.

**Why it's interesting**

Exit waterfalls are where funds discover that their ownership percentage is not what they thought. Having an open model means the assumptions are visible.

**Good for**

- Exit modelling
- Liquidation preferences
- Dilution modelling

**Limitations**

No licence file, so reuse terms are unclear. Research-grade, not maintained as a product.

**Links:** [GitHub](https://github.com/tdavidson/cap-table-tool)

---
