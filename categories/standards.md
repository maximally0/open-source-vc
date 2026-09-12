# Standards & Schemas

_Formats worth adopting before you have to migrate off them._

Cap-table standards, financial data standards, legal schemas, interoperability formats, and open investment data.

**14 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-12

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

**Coverage note.** Two important open standards are deliberately absent because they are not hosted on a code forge: the Series Seed document set and the GLEIF Legal Entity Identifier registry. Both are genuine standards worth knowing, both live on their own websites rather than as repositories, and this directory links repositories, so they are noted here rather than listed. What is included is the financial-reporting toolchain around XBRL, which is the format through which most structured financial data reaches a fund.

---

### Arelle

> The reference open XBRL processor.

`Arelle/Arelle` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Standards & Schemas |
| **License** | unverified (Other) |
| **Stars** | 236 |
| **Forks** | 360 |
| **Language** | HTML |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

XBRL is how financial statements arrive from public companies and increasingly from private reporting. Arelle reads it, validates it, and exposes the facts, which is what makes automated financial analysis possible rather than rekeying.

**Why it's interesting**

It is the reference implementation used by regulators and filers, so it handles the parts of the specification that simpler parsers get wrong.

**Good for**

- Financial data
- Filings analysis
- Data pipelines

**Limitations**

The licence is not a standard SPDX identifier. Interface is technical, and XBRL itself takes learning.

**Links:** [GitHub](https://github.com/Arelle/Arelle) &nbsp;·&nbsp; [Site](https://arelle.org)

---

### Open Cap Format

> An open data standard for cap tables.

`Open-Cap-Table-Coalition/Open-Cap-Format-OCF` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; _standard_

| | |
|---|---|
| **Category** | Standards & Schemas |
| **License** | unverified (Other) |
| **Stars** | 188 |
| **Forks** | 45 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-08-11) |
| **Self-hostable** | yes |

**VC use case**

Cap tables currently move between founders, lawyers, and investors as spreadsheets in whatever shape the last person used. OCF is a defined schema for the whole cap table: stakeholders, stock classes, issues, and conversions. A fund that standardises on it can compare companies and validate a founder's model.

**Why it's interesting**

This is the interoperability standard the venture industry has needed for years, and it is the one genuinely VC-native standard that exists. Being on it early is cheap; being on it late is a migration.

**Good for**

- Cap table validation
- Data standards
- Fund operations

**Limitations**

Designed for US-style company structures, so other jurisdictions need extension. Adoption is still limited, and the licence identifier is not standardised, so read the terms.

**Links:** [GitHub](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF) &nbsp;·&nbsp; [Site](https://opencaptablecoalition.com)

---

### python-xbrl

> A Python parser for XBRL filings.

`greedo/python-xbrl` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Standards & Schemas |
| **License** | Apache-2.0 |
| **Stars** | 233 |
| **Forks** | 76 |
| **Language** | Python |
| **Status** | Active (last push 2026-04-21) |
| **Self-hostable** | yes |

**VC use case**

The quickest route to a company's reported financials as Python objects, which is the first step in any quantitative comparison of public companies.

**Why it's interesting**

Minimal and readable, with a straightforward mapping from filing structure to data, which makes it easy to modify when a company reports unusually.

**Good for**

- Financial data
- Comparable companies
- Filings analysis

**Limitations**

Simpler than Arelle, so it handles edge cases less well. Activity has been intermittent.

**Links:** [GitHub](https://github.com/greedo/python-xbrl) &nbsp;·&nbsp; [Site](https://pypi.python.org/pypi/python-xbrl)

---

### py-xbrl

> A parser for XBRL and inline XBRL.

`manusimidt/py-xbrl` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Standards & Schemas |
| **License** | GPL-3.0 |
| **Stars** | 154 |
| **Forks** | 52 |
| **Language** | Python |
| **Status** | Active (last push 2026-08-29) |
| **Self-hostable** | yes |

**VC use case**

Inline XBRL is what modern filings actually use, and it embeds financial data in HTML rather than a separate document. This handles both forms, which matters when pulling a filing directly from a regulator's site.

**Why it's interesting**

The iXBRL support is the differentiator: many libraries handle only classic XBRL and silently fail on recent filings.

**Good for**

- Filings analysis
- Financial data
- Data pipelines

**Limitations**

GPL-licensed. Smaller maintenance community than the reference implementation.

**Links:** [GitHub](https://github.com/manusimidt/py-xbrl) &nbsp;·&nbsp; [Site](https://py-xbrl.readthedocs.io/en/latest/)

---

### iXBRL Viewer

> Browse inline XBRL reports interactively.

`Arelle/ixbrl-viewer` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Standards & Schemas |
| **License** | unverified (Other) |
| **Stars** | 129 |
| **Forks** | 77 |
| **Language** | JavaScript |
| **Status** | Active (last push 2026-09-10) |
| **Self-hostable** | yes |

**VC use case**

When a filing's numbers need checking against the original document, this shows the tagged data in place, so an analyst can see exactly which figure was tagged and how. Useful for verification rather than bulk analysis.

**Why it's interesting**

Tagging errors are common in filings and invisible in a parsed output. Seeing the tagged source is how you catch them.

**Good for**

- Verification
- Filings analysis
- Financial data

**Limitations**

A viewing tool rather than a data pipeline. Licence is not a standard SPDX identifier.

**Links:** [GitHub](https://github.com/Arelle/ixbrl-viewer)

---

### ixbrl-parse

> Get usable data out of inline XBRL files.

`kanedata/ixbrl-parse` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Standards & Schemas |
| **License** | MIT |
| **Stars** | 71 |
| **Forks** | 23 |
| **Language** | HTML |
| **Status** | Active (last push 2026-05-08) |
| **Self-hostable** | yes |

**VC use case**

Practical extraction from UK-style iXBRL accounts, which is the format most non-US filings use. Relevant for comparing private or small companies that file publicly in those jurisdictions.

**Why it's interesting**

Inline XBRL mixed into HTML breaks naive parsers, and this handles the transformation properly rather than treating the file as text.

**Good for**

- Filings analysis
- Financial data
- UK company research

**Limitations**

Oriented to UK filings, so other jurisdictions need work. Small project.

**Links:** [GitHub](https://github.com/kanedata/ixbrl-parse) &nbsp;·&nbsp; [Site](https://ixbrl-parse.readthedocs.io/)

---

### Xule

> A rules language for validating XBRL data.

`xbrlus/xule` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Standards & Schemas |
| **License** | Apache-2.0 |
| **Stars** | 38 |
| **Forks** | 17 |
| **Language** | HTML |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

When a fund or a portfolio company receives financial data, someone has to check it is internally consistent. This expresses validation rules against reported figures, so broken numbers are caught before they reach a model.

**Why it's interesting**

It is maintained by the standards body's own foundation, so it tracks the specification rather than trailing it.

**Good for**

- Data validation
- Financial data
- Reporting

**Limitations**

Requires understanding both XBRL and the rules language. Narrow audience.

**Links:** [GitHub](https://github.com/xbrlus/xule)

---

### edinet-tools

> Japanese corporate disclosure data, parsed.

`matthelmer/edinet-tools` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Standards & Schemas |
| **License** | MIT |
| **Stars** | 53 |
| **Forks** | 9 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-10) |
| **Self-hostable** | yes |

**VC use case**

Japanese filings are available publicly but in a form almost nothing can read. This turns dozens of document types into typed objects, which makes research on Japanese companies possible without a local data vendor.

**Why it's interesting**

It documents and parses a disclosure system that is effectively closed to anyone outside the country, which is exactly the sort of access gap that matters to a fund looking at that market.

**Good for**

- Japan market research
- Filings analysis
- Financial data

**Limitations**

Japanese-language domain, and coverage depends on the filing types the maintainer has implemented. Small project.

**Links:** [GitHub](https://github.com/matthelmer/edinet-tools) &nbsp;·&nbsp; [Site](https://pypi.org/project/edinet-tools/)

---

### Brel

> Read XBRL reports in Python.

`BrelLibrary/brel` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Standards & Schemas |
| **License** | unverified (Other) |
| **Stars** | 45 |
| **Forks** | 10 |
| **Language** | Python |
| **Status** | Active (last push 2026-03-24) |
| **Self-hostable** | yes |

**VC use case**

A lighter path to parsing XBRL when you only need the reported facts and do not want to take on a full processor. Suitable for building a small comparable-set dataset.

**Why it's interesting**

A clean, focused API for the common case, maintained by someone working on financial data interoperability.

**Good for**

- Financial data
- Comparable companies
- Data pipelines

**Limitations**

Limited specification coverage compared with Arelle, so unusual filings may not parse. Early.

**Links:** [GitHub](https://github.com/BrelLibrary/brel)

---

### OpenCLI

> A specification for describing command-line tools.

`bcdxn/opencli` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; _standard_

| | |
|---|---|
| **Category** | Standards & Schemas |
| **License** | MIT |
| **Stars** | 44 |
| **Forks** | 4 |
| **Language** | Go |
| **Status** | Active (last push 2026-08-30) |
| **Self-hostable** | yes |

**VC use case**

A small but relevant idea: if an agent is going to run CLI tools, it needs a machine- readable description of them. Worth knowing about when specifying how internal tools will be exposed to agents.

**Why it's interesting**

It extends the OpenAPI approach to the interface agents actually use most, which is the shell.

**Good for**

- Agent tooling
- Internal tools
- Standards

**Limitations**

Very early and narrow. Only relevant if you are building agent tooling.

**Links:** [GitHub](https://github.com/bcdxn/opencli) &nbsp;·&nbsp; [Site](https://opencli.dev)

---

### XBRL Parser

> A Go library for XBRL facts, contexts, and units.

`massive-com/xbrl-parser` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Standards & Schemas |
| **License** | MIT |
| **Stars** | 39 |
| **Forks** | 9 |
| **Language** | Go |
| **Status** | Active (last push 2025-11-06) |
| **Self-hostable** | yes |

**VC use case**

Relevant when a fund's pipeline is in Go and needs to ingest filings without a Python sidecar. Same job as the Python parsers, in a language that suits high-throughput ingestion.

**Why it's interesting**

Go is the right language for a service that parses filings continuously, and there are few options in it.

**Good for**

- Data pipelines
- Filings analysis
- Financial data

**Limitations**

Lower-level than the Python alternatives, so more work to use. Small project.

**Links:** [GitHub](https://github.com/massive-com/xbrl-parser)

---

### Digital Template to XBRL Converter

> Convert sustainability reporting templates to XBRL.

`EFRAG-EU/Digital-Template-to-XBRL-Converter` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Standards & Schemas |
| **License** | MIT |
| **Stars** | 38 |
| **Forks** | 20 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-08) |
| **Self-hostable** | yes |

**VC use case**

European sustainability reporting rules require tagged disclosures, and portfolio companies will have to produce them. A fund tracking ESG data across a portfolio benefits from understanding the format now rather than when the filings arrive.

**Why it's interesting**

It is maintained by the body setting the European standard, so it is the reference for that format rather than an interpretation of it.

**Good for**

- ESG reporting
- Regulatory compliance
- Portfolio monitoring

**Limitations**

Narrow to the European sustainability framework, and early. Not applicable outside it.

**Links:** [GitHub](https://github.com/EFRAG-EU/Digital-Template-to-XBRL-Converter)

---

### iXBRL Reporter

> Generate iXBRL financial reports from templates.

`cybermaggedon/ixbrl-reporter` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Standards & Schemas |
| **License** | GPL-3.0 |
| **Stars** | 35 |
| **Forks** | 12 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-08) |
| **Self-hostable** | yes |

**VC use case**

The production side of the format: taking account data and emitting a compliant tagged report. Relevant to portfolio companies that must file in that format, and to understanding what the data looks like when it leaves the company.

**Why it's interesting**

Most tooling reads XBRL; very little writes it. That makes this useful for anyone generating regulated financial reports.

**Good for**

- Regulatory reporting
- Financial data
- Portfolio support

**Limitations**

GPL-licensed, and the template system is configuration-heavy. Jurisdiction-specific rules need care.

**Links:** [GitHub](https://github.com/cybermaggedon/ixbrl-reporter)

---

### pystock-crawler

> Crawl and parse SEC EDGAR filings and prices.

`eliangcs/pystock-crawler` &nbsp;·&nbsp; 📚 **Research** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Standards & Schemas |
| **License** | MIT |
| **Stars** | 317 |
| **Forks** | 97 |
| **Language** | Python |
| **Status** | Dormant (last push 2024-05-14, 28mo) |
| **Self-hostable** | yes |

**VC use case**

An older worked example of building a filings dataset from EDGAR, including the XBRL handling. Useful as a reference for the shape of a filings pipeline.

**Why it's interesting**

It shows the full path from raw filings to a usable dataset, which is the part most examples skip.

**Good for**

- Filings collection
- Learning pipelines
- Dataset building

**Limitations**

Explicitly unmaintained by its author and years old, so its EDGAR interactions will need updating. Read it, do not depend on it.

**Links:** [GitHub](https://github.com/eliangcs/pystock-crawler)

---
