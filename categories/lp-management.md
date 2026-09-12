# LP & Fund Management

_Fund maths, LP relationships, and the paperwork in between._

LP CRM and intelligence, fundraising, fund modelling, portfolio construction, reporting, capital calls, distributions, and waterfalls.

**7 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-12

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

**Coverage note.** Fund and LP administration is the other thin area, and the reason is structural: this work is regulated, audit-facing, and carries liability, which makes it a poor fit for hobbyist software. What is genuinely missing from open source is fund-specific tooling: capital account ledgers with carried interest and waterfall mechanics, ILPA-style reporting templates, and LP CRM. What does exist, listed here, is general accounting and modelling machinery that a small fund or SPV can run its books on with some assembly. Treat this category as a starting point for building something, not as a replacement for a fund administrator.

---

### ERPNext

> An open ERP covering accounting, invoicing, and assets.

`frappe/erpnext` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | LP & Fund Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | GPL-3.0 |
| **Stars** | 39.1k |
| **Forks** | 12.8k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

For a fund that has outgrown spreadsheets and wants one system for accounting, invoicing, payments, and asset records, with the same framework behind the CRM. An emerging manager can run most of the back office on it.

**Why it's interesting**

It covers the accounting and compliance-adjacent processes that genuinely are regulated, which is where a fund cannot improvise, and it is built on a framework that can be extended.

**Good for**

- Fund back office
- Accounting
- Operations

**Limitations**

A real implementation project, not an install. GPL-licensed, which affects redistribution. Assumes business workflows that need adapting for a fund.

**Links:** [GitHub](https://github.com/frappe/erpnext) &nbsp;·&nbsp; [Site](https://frappe.io/erpnext)

---

### Grist

> A spreadsheet that behaves like a database.

`gristlabs/grist-core` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | LP & Fund Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 11.8k |
| **Forks** | 641 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

Where fund models belong when they outgrow a spreadsheet: capital call schedules, distribution waterfalls, and per-LP allocation tables, with formulas that reference records rather than cell ranges. The model stays readable and auditable when someone else inherits it.

**Why it's interesting**

It keeps the spreadsheet mental model while making the data relational, which is the right trade for fund maths that will be revisited for a decade.

**Good for**

- Fund modelling
- Waterfalls
- Capital calls

**Limitations**

Formula language differs from Excel, so existing models need porting. Some enterprise features are commercial.

**Links:** [GitHub](https://github.com/gristlabs/grist-core) &nbsp;·&nbsp; [Site](https://www.getgrist.com)

---

### Ledger

> The original plain-text accounting tool.

`ledger/ledger` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | LP & Fund Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unverified (Other) |
| **Stars** | 6k |
| **Forks** | 547 |
| **Language** | C++ |
| **Status** | Active (last push 2026-09-05) |
| **Self-hostable** | yes |

**VC use case**

The tool that established the format the others follow. Relevant if a fund's finance person already uses it, or for querying a dataset of transactions directly with its query language.

**Why it's interesting**

Years of accumulated design in its reporting and query model, and an ecosystem of tools that read the same file format.

**Good for**

- Fund accounting
- Transaction analysis
- Reporting

**Limitations**

Licence is not a standard SPDX identifier. Development is slower than the newer alternatives, and the interface is unforgiving.

**Links:** [GitHub](https://github.com/ledger/ledger) &nbsp;·&nbsp; [Site](https://www.ledger-cli.org)

---

### PyPortfolioOpt

> Portfolio construction and optimisation in Python.

`PyPortfolio/PyPortfolioOpt` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | LP & Fund Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 6k |
| **Forks** | 1.2k |
| **Language** | Jupyter Notebook |
| **Status** | Active (last push 2026-07-07) |
| **Self-hostable** | yes |

**VC use case**

Fund-level questions about portfolio construction: concentration limits, correlation across a book, and expected risk given position sizes. Also usable for a fund of funds sizing allocations across managers.

**Why it's interesting**

The methods are documented with their assumptions stated, which matters when the output feeds an allocation decision and someone asks why a weight is what it is.

**Good for**

- Portfolio construction
- Fund modelling
- Risk analysis

**Limitations**

Optimisers are sensitive to inputs, and small error in expected returns produces large changes in weights. Venture returns are not normally distributed, so classical assumptions fit badly.

**Links:** [GitHub](https://github.com/PyPortfolio/PyPortfolioOpt) &nbsp;·&nbsp; [Site](https://pyportfolioopt.readthedocs.io/)

---

### Beancount

> Double-entry accounting in plain text files.

`beancount/beancount` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | LP & Fund Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | GPL-2.0 |
| **Stars** | 6k |
| **Forks** | 467 |
| **Language** | Python |
| **Status** | Active (last push 2026-08-23) |
| **Self-hostable** | yes |

**VC use case**

The honest answer for a fund's books at small scale: capital calls, management fees, expenses, and per-LP capital accounts, all as text files in version control. An SPV or a first fund can keep accurate books without an administrator for every transaction.

**Why it's interesting**

Plain-text accounting means every entry is diffable, reviewable, and permanent. For a fund vehicle, an audit trail that lives in git is a genuine improvement over a proprietary accounting file.

**Good for**

- Fund accounting
- SPV books
- Capital accounts

**Limitations**

No interface: you write entries in a text editor and run commands. It is double-entry accounting, so the user has to understand the method. Not a replacement for an administrator handling LP compliance.

**Links:** [GitHub](https://github.com/beancount/beancount) &nbsp;·&nbsp; [Site](http://beancount.github.io/)

---

### hledger

> Plain-text accounting with a serious command line.

`hledgerorg/hledger` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | LP & Fund Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | GPL-3.0 |
| **Stars** | 4.7k |
| **Forks** | 413 |
| **Language** | Haskell |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

The same approach as Beancount with more reporting built in: fund-level and per-LP balance sheets, cash flow, and the reports a quarterly LP update draws on, generated from text files.

**Why it's interesting**

Mature and fast, with reporting commands that cover what a small fund actually needs to produce. Its author has maintained it for years, which matters in accounting.

**Good for**

- Fund accounting
- LP reporting
- Cash flow

**Limitations**

Same learning curve as any double-entry system, and no graphical interface by default. Needs discipline to keep entries current.

**Links:** [GitHub](https://github.com/hledgerorg/hledger) &nbsp;·&nbsp; [Site](https://hledger.org)

---

### GnuCash

> Full double-entry accounting with a desktop interface.

`Gnucash/gnucash` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | LP & Fund Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unverified (Other) |
| **Stars** | 4.3k |
| **Forks** | 986 |
| **Language** | C |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

For a fund or family office whose finance person wants proper accounting software rather than a command line: double-entry books, invoicing, and reports for a fund vehicle, with the data held locally.

**Why it's interesting**

Decades of development and small-business-grade features without a subscription or a cloud dependency, which matters when the books describe other people's money.

**Good for**

- Fund accounting
- SPV books
- Reporting

**Limitations**

Desktop-only and dated in places. Licence is not a standard SPDX identifier. Not built for multi-user work without care.

**Links:** [GitHub](https://github.com/Gnucash/gnucash) &nbsp;·&nbsp; [Site](http://code.gnucash.org/website/)

---
