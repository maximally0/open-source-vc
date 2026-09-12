# The Diligence Stack

From a data room to a decision, with the reasoning traceable.

---

## The problem

Diligence is the part of venture where the volume of material is largest and the time available is fixed. A data room holds a few thousand documents. Two analysts have three weeks. The failure mode is not laziness, it is coverage: nobody reads everything, so what gets read is whatever the requesting partner thought to ask for, which is a function of what they already suspected.

Open-source tooling does not change the judgement required. It changes whether coverage is a function of diligence or a function of luck.

## Before anything else: get the documents readable

This step is unglamorous and it determines whether everything after it works. Roughly half of the documents in a real data room are scans, and a scanned PDF is an image: no search, no extraction, no model can read it.

```text
Data room
    │
    ├── Is it a scan?  ──→  OCRmyPDF        (adds a text layer, keeps the original)
    │
    ├── Is it digital? ──→  Docling / Marker (layout-aware conversion)
    │
    ├── Tables only?   ──→  Camelot / pdfplumber
    │
    └── Non-Latin?     ──→  PaddleOCR
```

The choice that matters is **layout awareness**. If you only need to search text, plain extraction is fine. If you need the number in row four of the revenue table, the position of that number is part of the data, and a parser that flattens tables produces confident errors. [Docling](../categories/document-intelligence.md) and [Marker](../categories/document-intelligence.md) preserve structure; [Tesseract](../categories/document-intelligence.md) does not, and is still worth having as a fallback.

**Do this once, properly.** A re-parse three weeks in, after the model has read flattened tables, means redoing the analysis too.

## The five workstreams

### Commercial

Can this company sell, and to whom, for how much?

- Customer interviews, coded consistently: [Label Studio](../categories/due-diligence.md) or [doccano](../categories/due-diligence.md)
- Support tickets and reviews at volume, for a count rather than an impression
- Market context: [company-research-agent](../categories/company-discovery.md), [GPT Researcher](../categories/market-research.md)
- Competitor pricing and positioning: [changedetection.io](../categories/deal-sourcing.md), [SingleFile](../categories/osint.md)

### Financial

Are the numbers what they appear to be?

- Statements as data, not PDFs: [Camelot](../categories/document-intelligence.md), [pdfplumber](../categories/document-intelligence.md)
- Normalised ratios with documented formulas: [Finance Toolkit](../categories/investment-analysis.md)
- Public comparables where they exist: [edgartools](../categories/investment-analysis.md), [OpenBB](../categories/investment-analysis.md)
- Reproducible model: [Marimo](../categories/knowledge-management.md), so a corrected input updates every figure

### Technical

Is the product what the deck says it is?

- Their public footprint: [subfinder](../categories/osint.md), [httpx](../categories/osint.md), [Web-Check](../categories/founder-discovery.md)
- Repository practice: [shhgit](../categories/due-diligence.md) for leaked credentials, [OpenHands](../categories/ai-agents.md) to interrogate the codebase
- Research claims: [paper-qa](../categories/due-diligence.md) against their papers and patents
- Data quality claims: [Cleanlab](../categories/due-diligence.md)
- Production claims: [Phoenix](../categories/due-diligence.md) on their model traces
- Training-data provenance: [CorpusCustody](../categories/due-diligence.md), which is now a real question for AI companies
- AI product evaluation: [LangWatch](../categories/due-diligence.md)

### Legal

What has the company committed to?

- Contract review: [Mike](../categories/legal.md), [OpenContracts](../categories/legal.md), with a defined risk framework from [Claude Legal Skill](../categories/legal.md)
- Cross-document questions: how is this indemnity worded across the whole set, rather than in this one contract
- Regulatory exposure: [Open US Law](../categories/legal.md) for what a regulated business is actually required to do
- Redlines: [Python-Redlines](../categories/legal.md)

None of this replaces counsel. Its value is arriving at counsel with the questions already formed, which changes what an hour of their time buys you.

### Cap table and structure

What do I actually own, and what does it return?

- The cap table: [Captable](../categories/cap-tables.md), or the [worksheet](../categories/cap-tables.md)
- The standard: [Open Cap Format](../categories/standards.md), which is how you validate a founder's model instead of asking them to re-explain it
- The exit maths: [cap-table-tool](../categories/cap-tables.md) for the waterfall, which is where ownership percentage turns out not to be what it appeared
- Instrument terms: [QuantLib](../categories/investment-analysis.md), [FinancePy](../categories/investment-analysis.md)

Read the coverage note on the [cap tables page](../categories/cap-tables.md) first. This is the least-served area of open-source venture tooling.

## Handling the material safely

Data rooms contain salaries, customer names, personal data, and contract terms under NDA. Before any of that reaches a hosted model:

- [Rizzo PII](../categories/due-diligence.md) strips personal information locally
- [doc-haus](../categories/legal.md) and [DocuChat](../categories/legal.md) keep documents on your machine entirely
- [Stirling PDF](../categories/document-intelligence.md) for redaction without uploading anything to a free web tool

Check what your NDA actually says before deciding a hosted model is fine. Confidentiality obligations often prohibit third-party processing regardless of what the vendor's terms claim.

## Turning it into a memo

The memo is where diligence becomes a decision, and it is the step that resists automation most, because its value is the argument.

What tooling can do is remove the blank page and the copy-paste error:

- Structure and scaffold: [memo_generator](../categories/investment-memos.md), [TickerToThesis](../categories/investment-memos.md)
- Typesetting, so it reads as considered work: [Typst](../categories/investment-memos.md)
- Reproducible figures: [Quarto](../categories/investment-memos.md), so a corrected input updates the numbers in the text
- Cited research: [STORM](../categories/market-research.md), [paper-qa](../categories/due-diligence.md)

## The habit that matters most

Every finding in a memo should be traceable to a document, a page, and a date. That is what makes a memo defensible six months later when someone asks why the fund believed a number.

Three tools enforce that habit more than any process document:

- [SingleFile](../categories/osint.md), so a claim made on a website is a file you still have
- [WhisperX](../categories/relationship-intelligence.md), so a claim made on a call has a timestamp and a speaker
- [Marimo](../categories/knowledge-management.md), so a number in a model can be reproduced rather than believed

A diligence process that produces confident conclusions without that trail is not faster. It is just less likely to be checked.
