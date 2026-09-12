# The Investment Workflow, Stage by Stage

Tools are organised here the way the work actually happens, because that is how people look for them. Nobody wakes up wanting a vector database; they wake up needing to find a company, or to check whether a founder is telling the truth.

```text
  01 SOURCE  →  02 RESEARCH  →  03 DILIGENCE  →  04 UNDERWRITE  →  05 IC & MEMO
                                                                      │
  09 FUND    ←  08 RELATIONSHIPS  ←  07 PORTFOLIO  ←  06 CLOSE  ←──────┘
```

Three categories cut across every stage rather than sitting in one: [AI Agents for VC](categories/ai-agents.md), [Workflow & Automation](categories/automation.md), [Datasets & Open Data](categories/datasets.md).

| Stage | What happens | Subcategories | Projects |
|---|---|---|---:|
| [Source](stages/01-source.md) | Find the company before it is on anyone's list. | [Founder & Talent Discovery](categories/founder-discovery.md), [Company Discovery & Deal Sourcing](categories/company-discovery.md), [Deal Sourcing & Pipeline](categories/deal-sourcing.md) | 25 |
| [Research](stages/02-research.md) | Understand the company, the founder, and the market. | [Market & Industry Research](categories/market-research.md), [Web Intelligence & OSINT](categories/osint.md) | 33 |
| [Diligence](stages/03-diligence.md) | Verify what the company says is true. | [Due Diligence](categories/due-diligence.md), [Data Rooms & Document Intelligence](categories/document-intelligence.md), [Cap Tables & Equity](categories/cap-tables.md) | 37 |
| [Underwrite](stages/04-underwrite.md) | Model the business, the round, and the outcome. | [Investment Analysis](categories/investment-analysis.md) | 14 |
| [IC & Memo](stages/05-ic.md) | Turn evidence into a decision the partnership can defend. | [Investment Memo & IC](categories/investment-memos.md), [Knowledge Management](categories/knowledge-management.md) | 31 |
| [Close](stages/06-close.md) | Documents, signatures, and the money moving. | [Legal & Transaction Infrastructure](categories/legal.md) | 17 |
| [Portfolio](stages/07-portfolio.md) | The decade after the wire hits. | [Portfolio Management](categories/portfolio-management.md) | 10 |
| [Relationships](stages/08-relationships.md) | The network is the asset. | [Relationship Intelligence](categories/relationship-intelligence.md) | 13 |
| [Fund](stages/09-fund.md) | LP relationships, fund maths, and reporting. | [LP & Fund Management](categories/lp-management.md), [Standards & Schemas](categories/standards.md) | 21 |

---

## Where the open-source gaps are

Two stages are far better served than the rest. **Sourcing** and **research** have genuine options, because collecting and reading public information is a general problem with a large open-source community behind it.

**Underwriting, IC, and fund administration are the opposite.** Valuation, scoring frameworks, cohort analysis, unit economics, and fund accounting have almost no open-source tooling at all, because they are either spreadsheets or regulated. [GAPS.md](GAPS.md) documents every sub-task where the honest answer is that nothing exists.
