# Fund

_LP relationships, fund maths, and reporting._

[← all stages](../VC_WORKFLOW.md) &nbsp;·&nbsp; 21 projects &nbsp;·&nbsp; metadata updated 2026-09-12

---

## Subcategories

| Subcategory | Projects | Covers |
|---|---:|---|
| [LP & Fund Management](../categories/lp-management.md) | 7 | LP CRM and intelligence |
| [Standards & Schemas](../categories/standards.md) | 14 | Cap-table standards |

## The shape of it

Keep the books in something version-controlled and auditable, and model the fund maths in a form that survives the person who built it.


## Install for this stage

VC-native first, then the adaptable tools that carry the work. Everything else in the subcategories above is on the category pages.

| Project | Relevance | Tier | Stars | License | One line |
|---|---|---|---:|---|---|
| [ERPNext](https://github.com/frappe/erpnext) | VC-adaptable | Recommended | 39.1k | GPL-3.0 | For a fund that has outgrown spreadsheets and wants one system for accounting, invoicing, payments, and asset records, with the same framework behind the CRM. |
| [Grist](https://github.com/gristlabs/grist-core) | VC-adaptable | Recommended | 11.8k | Apache-2.0 | Where fund models belong when they outgrow a spreadsheet: capital call schedules, distribution waterfalls, and per-LP allocation tables, with formulas that reference records rather than cell ranges. |
| [Ledger](https://github.com/ledger/ledger) | VC-adaptable | Recommended | 6k | unverified (Other) | The tool that established the format the others follow. |
| [PyPortfolioOpt](https://github.com/PyPortfolio/PyPortfolioOpt) | VC-adaptable | Recommended | 6k | MIT | Fund-level questions about portfolio construction: concentration limits, correlation across a book, and expected risk given position sizes. |
| [Beancount](https://github.com/beancount/beancount) | VC-adaptable | Recommended | 6k | GPL-2.0 | The honest answer for a fund's books at small scale: capital calls, management fees, expenses, and per-LP capital accounts, all as text files in version control. |
| [hledger](https://github.com/hledgerorg/hledger) | VC-adaptable | Recommended | 4.7k | GPL-3.0 | The same approach as Beancount with more reporting built in: fund-level and per-LP balance sheets, cash flow, and the reports a quarterly LP update draws on, generated from text files. |
| [GnuCash](https://github.com/Gnucash/gnucash) | VC-adaptable | Recommended | 4.3k | unverified (Other) | For a fund or family office whose finance person wants proper accounting software rather than a command line: double-entry books, invoicing, and reports for a fund vehicle, with the data held locally. |
| [Open Cap Format](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF) | VC-native | Essential | 188 | unverified (Other) | Cap tables currently move between founders, lawyers, and investors as spreadsheets in whatever shape the last person used. |
| [Arelle](https://github.com/Arelle/Arelle) | VC-adaptable | Essential | 236 | unverified (Other) | XBRL is how financial statements arrive from public companies and increasingly from private reporting. |
| [python-xbrl](https://github.com/greedo/python-xbrl) | VC-adaptable | Recommended | 233 | Apache-2.0 | The quickest route to a company's reported financials as Python objects, which is the first step in any quantitative comparison of public companies. |

---

**Next stage:** [back to the workflow](../VC_WORKFLOW.md)
