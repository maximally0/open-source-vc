# Data Rooms & Document Intelligence

_Data rooms are PDFs. This is how you read 4,000 of them._

PDF parsing, layout-aware extraction, OCR, contract extraction, document search, and multimodal document understanding.

**24 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-12

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

---

### Docling

> Layout-aware conversion of PDFs and office documents.

`docling-project/docling` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 66.3k |
| **Forks** | 4.8k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

Financial statements and contracts are where layout carries meaning: which number sits in which column, which heading a clause falls under. Docling preserves that structure on the way to structured output, which is the difference between a usable table and a scrambled list of numbers.

**Why it's interesting**

It comes from IBM Research, handles tables and reading order properly, and runs locally. It plugs into most RAG stacks rather than locking you into one.

**Good for**

- Financial document parsing
- Contract analysis
- Data-room pipelines

**Limitations**

Model-based parsing is slower than text extraction and needs decent hardware. Very unusual layouts still produce errors worth checking.

**Links:** [GitHub](https://github.com/docling-project/docling) &nbsp;·&nbsp; [Site](https://docling-project.github.io/docling)

---

### Paperless-ngx

> Scan, index, and search every document you own.

`paperless-ngx/paperless-ngx` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | GPL-3.0 |
| **Stars** | 45k |
| **Forks** | 3.1k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

The document archive for a fund or a family office: every contract, statement, and filing OCR'd, tagged, and full-text searchable, with the original file retained. The difference between finding a clause in thirty seconds and asking who has a copy.

**Why it's interesting**

It handles the whole lifecycle, including automatic tagging and correspondents, so the archive stays usable as it grows rather than becoming a folder nobody opens.

**Good for**

- Document archive
- Institutional memory
- Compliance records

**Limitations**

Retro-fitting years of existing documents takes effort and storage. Licence is GPL, worth noting if you plan to build a service on it.

**Links:** [GitHub](https://github.com/paperless-ngx/paperless-ngx) &nbsp;·&nbsp; [Site](http://docs.paperless-ngx.com/)

---

### Marker

> Fast, accurate PDF to markdown and JSON.

`datalab-to/marker` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 39.7k |
| **Forks** | 2.9k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-09) |
| **Self-hostable** | yes |

**VC use case**

The workhorse for converting a data room into text an analyst or a model can read. Handles the mix of scanned and digital PDFs that real diligences contain, and keeps tables as tables.

**Why it's interesting**

It is fast enough to process hundreds of documents without a research project, and the same team publishes the underlying layout and OCR models separately, so the pieces can be swapped.

**Good for**

- Data-room conversion
- Contract analysis
- RAG preparation

**Limitations**

Commercial-use terms require checking above a revenue threshold, which is unusual and worth reading rather than assuming. GPU or a hosted option for speed.

**Links:** [GitHub](https://github.com/datalab-to/marker) &nbsp;·&nbsp; [Site](https://www.datalab.to)

---

### OCRmyPDF

> Adds a searchable text layer to scanned PDFs.

`ocrmypdf/OCRmyPDF` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MPL-2.0 |
| **Stars** | 34.7k |
| **Forks** | 2.4k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-08) |
| **Self-hostable** | yes |

**VC use case**

The unglamorous step that makes everything else possible. Most diligence documents arrive as image-only scans, which no search or model can read. This adds a text layer while keeping the original pages intact, so the file stays evidence.

**Why it's interesting**

It preserves the original scan and adds text alongside it, which matters when the document is someone's executed contract. It also handles the awkward cases like skewed pages and mixed orientations.

**Good for**

- Scanned documents
- Data-room preparation
- Searchable archives

**Limitations**

Quality depends on the underlying OCR engine, and it is CPU-heavy on large batches. Not a layout extraction tool.

**Links:** [GitHub](https://github.com/ocrmypdf/OCRmyPDF) &nbsp;·&nbsp; [Site](http://ocrmypdf.readthedocs.io/)

---

### Unstructured

> Turns documents of any format into structured elements.

`Unstructured-IO/unstructured` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 15.4k |
| **Forks** | 1.3k |
| **Language** | HTML |
| **Status** | Active (last push 2026-09-10) |
| **Self-hostable** | yes |

**VC use case**

A data room is a pile of PDFs, slide decks, spreadsheets, and scans in no particular order. This breaks each one into typed elements, titles, tables, lists, and narrative text, so diligence questions can be asked across the whole room rather than per document.

**Why it's interesting**

It is the ingestion layer most document pipelines are built on, which means it has been hardened against the formats that actually appear in practice, including the ugly ones exported from enterprise systems.

**Good for**

- Data-room ingestion
- Document pipelines
- RAG preparation

**Limitations**

Element extraction is heuristic, so layout-heavy documents still need checking. The high-throughput pipeline needs a container and real resources.

**Dependencies:** Python 3.10+, optional system libraries for some formats

**Links:** [GitHub](https://github.com/Unstructured-IO/unstructured) &nbsp;·&nbsp; [Site](https://www.unstructured.io/)

---

### MarkItDown

> Convert almost any file to markdown.

`microsoft/markitdown` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 183.1k |
| **Forks** | 13.5k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

A quick way to get office documents, presentations, spreadsheets, and PDFs into text you can paste into a model or a notebook. Good for the ten-document case, not the thousand-document one.

**Why it's interesting**

From Microsoft, minimal dependencies, and it keeps structure such as headings and tables where the format allows. It is the shortest path from file to readable text.

**Good for**

- Quick conversion
- Ad-hoc analysis
- Document preparation

**Limitations**

Deliberately simple: no OCR, limited table fidelity, and not built for batch pipelines or layout-heavy documents.

**Links:** [GitHub](https://github.com/microsoft/markitdown)

---

### Stirling PDF

> A self-hosted toolkit of PDF operations.

`Stirling-Tools/Stirling-PDF` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unverified (Other) |
| **Stars** | 91.8k |
| **Forks** | 8.3k |
| **Language** | Java |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

Merge, split, compress, redact, sign, and OCR without uploading a confidential document to a free online tool. For a fund, that last point is the whole reason to have it.

**Why it's interesting**

It bundles dozens of operations behind one local interface, which replaces the random assortment of websites people reach for. Fine-grained control without scripts.

**Good for**

- Document preparation
- Redaction
- Confidential handling

**Limitations**

Heavy operations need resources, and the licence is not a standard SPDX identifier. Interface-first, so batch work is better done in code.

**Links:** [GitHub](https://github.com/Stirling-Tools/Stirling-PDF) &nbsp;·&nbsp; [Site](https://stirling.com)

---

### PaddleOCR

> OCR across 80+ languages, including non-Latin scripts.

`PaddlePaddle/PaddleOCR` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 89.4k |
| **Forks** | 11.3k |
| **Language** | Python |
| **Status** | Active (last push 2026-07-22) |
| **Self-hostable** | yes |

**VC use case**

Relevant for diligences involving Chinese, Japanese, Korean, Arabic, or Indic documents, where Western OCR tools degrade badly. Also fine for English scans, at a fraction of a commercial API's cost.

**Why it's interesting**

The script coverage is genuinely broad and the models are small enough to run on modest hardware, so a fund can process documents without per-page fees.

**Good for**

- Multilingual diligence
- Scanned documents
- High-volume OCR

**Limitations**

Custom training and tuning are part of the framework's ethos, which is more setup than a drop-in tool. Output needs post-processing.

**Links:** [GitHub](https://github.com/PaddlePaddle/PaddleOCR) &nbsp;·&nbsp; [Site](https://www.paddleocr.com)

---

### MinerU

> PDF to markdown with heavy layout models.

`opendatalab/MinerU` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | unverified (Other) |
| **Stars** | 79.8k |
| **Forks** | 6.7k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

Benchmarked well on scientific and financial PDFs, which is the material a deep-tech or healthcare diligence process is full of. Produces markdown and JSON that keeps formulas, tables, and figures in place.

**Why it's interesting**

It is tuned for the documents where generic parsers fail: two-column academic papers, equations, and dense tables.

**Good for**

- Scientific PDFs
- Technical diligence
- Document pipelines

**Limitations**

GPU strongly recommended, and licence terms are not a standard SPDX identifier, so check them before commercial use.

**Links:** [GitHub](https://github.com/opendatalab/MinerU) &nbsp;·&nbsp; [Site](https://opendatalab.github.io/MinerU/)

---

### Tesseract

> The OCR engine nearly everything else is built on.

`tesseract-ocr/tesseract` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 76.5k |
| **Forks** | 10.8k |
| **Language** | C++ |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

The dependable baseline when you need text from a scan and nothing clever. Every serious document pipeline of the last two decades has a Tesseract fallback somewhere, and knowing it is there matters when a newer model fails.

**Why it's interesting**

Decades of maintenance, tiny footprint, and support for a long list of languages. It is the reason OCR is not a paid API in most pipelines.

**Good for**

- Baseline OCR
- Scanned documents
- Document pipelines

**Limitations**

Layout-blind: it reads characters well and structure badly, so tables and multi-column pages need a separate tool. Accuracy trails modern vision models.

**Links:** [GitHub](https://github.com/tesseract-ocr/tesseract) &nbsp;·&nbsp; [Site](https://tesseract-ocr.github.io/)

---

### Pandoc

> Convert between essentially every document format.

`jgm/pandoc` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | GPL-2.0 |
| **Stars** | 46.3k |
| **Forks** | 4k |
| **Language** | Haskell |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

The converter that makes a document pipeline possible: markdown to docx for a memo someone must edit in Word, HTML to PDF, spreadsheets to tables. Also the reason you can keep notes in plain text and still deliver what a partner expects.

**Why it's interesting**

It has been the universal document converter for nearly two decades, and its format support is not matched. Every serious documentation pipeline depends on it.

**Good for**

- Format conversion
- Memo production
- Documentation pipelines

**Limitations**

Conversion is structural, so complex layouts do not survive intact. Learning its template system takes time.

**Links:** [GitHub](https://github.com/jgm/pandoc) &nbsp;·&nbsp; [Site](https://pandoc.org)

---

### EasyOCR

> OCR in 80+ languages with almost no setup.

`JaidedAI/EasyOCR` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 30k |
| **Forks** | 3.6k |
| **Language** | Python |
| **Status** | Active (last push 2025-12-05) |
| **Self-hostable** | yes |

**VC use case**

The fastest path from a scanned document to text when you do not want to install an OCR stack. Handles the non-Latin scripts that turn up in cross-border diligence.

**Why it's interesting**

A few lines of Python and it works. For one-off extraction tasks that is the right trade against a heavier pipeline.

**Good for**

- Ad-hoc OCR
- Multilingual documents
- Prototyping

**Limitations**

Slower and less accurate than newer layout models on complex pages. GPU needed for volume.

**Links:** [GitHub](https://github.com/JaidedAI/EasyOCR) &nbsp;·&nbsp; [Site](https://www.jaided.ai)

---

### Kotaemon

> A clean interface for chatting with your documents.

`Cinnamon/kotaemon` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 25.7k |
| **Forks** | 2.2k |
| **Language** | Python |
| **Status** | Active (last push 2026-07-14) |
| **Self-hostable** | yes |

**VC use case**

A usable front end for a fund's document collection, with citations back to the source page so an analyst can check an answer rather than trust it. Useful when a partner wants document Q&A without learning a framework.

**Why it's interesting**

It keeps the citation visible in the interface, which is the feature that decides whether a partner actually uses a tool like this.

**Good for**

- Document Q&A
- Data-room triage
- Internal tools

**Limitations**

Another deployment with a vector store behind it. Retrieval quality depends on document preparation.

**Links:** [GitHub](https://github.com/Cinnamon/kotaemon) &nbsp;·&nbsp; [Site](https://cinnamon.github.io/kotaemon/)

---

### Surya

> OCR and layout detection across many languages.

`datalab-to/surya` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 21.4k |
| **Forks** | 1.5k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

Contract and filing sets often contain scanned pages and non-English documents. Surya detects layout, reading order, and text across many languages, which is what makes a cross-border diligence possible without hiring someone to retype pages.

**Why it's interesting**

It reports reading order and table structure, not just characters, which is where most OCR stops being useful.

**Good for**

- Scanned documents
- Multilingual documents
- Document pipelines

**Limitations**

Another model to run, with the same commercial-licence caveat as the team's other tools. Accuracy on poor scans varies.

**Links:** [GitHub](https://github.com/datalab-to/surya) &nbsp;·&nbsp; [Site](https://www.datalab.to)

---

### DocuSeal

> Self-hosted e-signature.

`docusealco/docuseal` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | AGPL-3.0 |
| **Stars** | 18.5k |
| **Forks** | 1.9k |
| **Language** | Ruby |
| **Status** | Active (last push 2026-09-07) |
| **Self-hostable** | partial (open core) |

**VC use case**

Signature pages for SAFEs, side letters, and portfolio company paperwork, without a per-envelope vendor and without sending founder signatures through someone else's cloud. Handles the templates and audit trail that make a signature defensible.

**Why it's interesting**

It covers the parts that matter for a deal: templates, roles, signing order, and a certificate of completion. That is what turns a PDF into an executed document.

**Good for**

- Deal closing
- SAFE signing
- LP documents

**Limitations**

AGPL-licensed with a commercial tier for some features, and self-hosting means the documents and audit trail live on your infrastructure, which you then have to secure.

**Links:** [GitHub](https://github.com/docusealco/docuseal) &nbsp;·&nbsp; [Site](https://www.docuseal.com)

---

### Documenso

> An open DocuSign alternative.

`documenso/documenso` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | AGPL-3.0 |
| **Stars** | 15k |
| **Forks** | 3.2k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | partial (open core) |

**VC use case**

The other serious open e-signature option, useful when a fund wants to host signing itself but does not want the commercial tier that DocuSeal gates features behind. Same job: templates, signing order, and a completion record.

**Why it's interesting**

A straightforward open-core product with an active team, and a licence that is clear about what is open and what is commercial.

**Good for**

- Deal closing
- Document execution
- Compliance records

**Limitations**

Some team and enterprise features are paid. Fewer integrations than the incumbents, and self-hosting is your responsibility.

**Links:** [GitHub](https://github.com/documenso/documenso) &nbsp;·&nbsp; [Site](https://documenso.com)

---

### Chandra

> OCR built for complex tables, forms, and handwriting.

`datalab-to/chandra` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 12.3k |
| **Forks** | 1.2k |
| **Language** | Python |
| **Status** | Active (last push 2026-06-26) |
| **Self-hostable** | yes |

**VC use case**

The document types that defeat ordinary OCR are exactly the ones in a diligence: a scanned cap table with merged cells, a handwritten board minute, a form filled in by hand. This is the model aimed at those.

**Why it's interesting**

It keeps layout while handling awkward content, and it is from the same team as Marker and Surya, so it slots into that pipeline.

**Good for**

- Complex tables
- Handwritten documents
- Data-room conversion

**Limitations**

Model-based, so it needs hardware and the team's usual commercial-licence check. Handwriting accuracy varies by hand.

**Links:** [GitHub](https://github.com/datalab-to/chandra) &nbsp;·&nbsp; [Site](https://www.datalab.to)

---

### pdfplumber

> Precise access to PDF text, lines, and tables.

`jsvine/pdfplumber` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 10.7k |
| **Forks** | 919 |
| **Language** | Python |
| **Status** | Active (last push 2026-08-06) |
| **Self-hostable** | yes |

**VC use case**

When you need one specific number from one specific page and everything else is overkill. Analysts use it to pull a figure out of a filing, verify a table Camelot misread, or crop a page region for evidence.

**Why it's interesting**

It exposes the underlying geometry, so you can work with where text sits on the page rather than just what it says. That is what makes verification possible.

**Good for**

- Targeted extraction
- Verification
- Data extraction

**Limitations**

Not a layout model: you write the logic per document type. Slow on large document sets.

**Links:** [GitHub](https://github.com/jsvine/pdfplumber)

---

### PyMuPDF

> A fast library for reading and rewriting PDFs.

`pymupdf/PyMuPDF` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | AGPL-3.0 |
| **Stars** | 10.7k |
| **Forks** | 798 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

The utility layer under document work: split a 400-page filing, redact before sharing, extract embedded images, or pull just the pages that matter for a meeting pack. Fast enough to run interactively.

**Why it's interesting**

It does the whole-file manipulation that parsers do not, and it is quick enough that an analyst notices the difference versus pure-Python libraries.

**Good for**

- PDF manipulation
- Evidence preparation
- Document pipelines

**Limitations**

AGPL-licensed, which has real obligations if you build a network service on it. Not a layout understanding tool.

**Links:** [GitHub](https://github.com/pymupdf/PyMuPDF) &nbsp;·&nbsp; [Site](https://pymupdf.readthedocs.io/?utm_source=github&utm_medium=referral&utm_campaign=pymupdf_github&utm_content=about&utm_term=docs)

---

### Unstract

> Prompt-driven extraction of structured data from documents.

`Zipstack/unstract` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | AGPL-3.0 |
| **Stars** | 7.2k |
| **Forks** | 715 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | partial (open core) |

**VC use case**

When you need the same handful of fields out of hundreds of similar documents, such as revenue, headcount, and renewal date from a stack of customer contracts. Define the fields once and run the set.

**Why it's interesting**

It treats extraction as a pipeline with an API rather than a chat session, which is what makes it usable on a real batch and repeatable next quarter.

**Good for**

- Contract extraction
- Batch processing
- Data-room pipelines

**Limitations**

AGPL with a commercial tier, and LLM-based extraction needs validating against a sample before you trust a whole batch.

**Links:** [GitHub](https://github.com/Zipstack/unstract) &nbsp;·&nbsp; [Site](https://unstract.com)

---

### Apache Tika

> Metadata and text from almost any file format.

`apache/tika` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 4.1k |
| **Forks** | 969 |
| **Language** | Java |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

When a data room contains two hundred files in a dozen formats, you need to know what each one is before deciding what to read. Tika extracts type, metadata, and text from nearly anything, which makes triage possible.

**Why it's interesting**

Format coverage is the widest available, and it reports embedded metadata such as author and creation date, which occasionally settles a question about who wrote a document and when.

**Good for**

- Format triage
- Metadata extraction
- Document pipelines

**Limitations**

Text extraction is format-level, not layout-aware, so structure is lost. It is a Java service, which is a deployment consideration.

**Links:** [GitHub](https://github.com/apache/tika) &nbsp;·&nbsp; [Site](https://tika.apache.org/)

---

### Camelot

> Extract tables from PDFs as dataframes.

`camelot-dev/camelot` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 3.8k |
| **Forks** | 546 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-02) |
| **Self-hostable** | yes |

**VC use case**

Financial diligence runs on tables: revenue by quarter, cohort retention, unit economics. This pulls them out of PDFs into something you can compute on, which saves retyping numbers that will later be checked anyway.

**Why it's interesting**

It gives you control over the extraction strategy and reports accuracy per table, so you can see which numbers to distrust instead of getting a silent guess.

**Good for**

- Financial tables
- Data extraction
- Diligence models

**Limitations**

Works best on tables with visible ruling lines; borderless tables need manual coordinates. Numeric accuracy must be spot-checked against the source page.

**Links:** [GitHub](https://github.com/camelot-dev/camelot) &nbsp;·&nbsp; [Site](https://camelot-py.readthedocs.io)

---

### PageIndex

> Reasoning-based document search without a vector database.

`VectifyAI/PageIndex` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 35.6k |
| **Forks** | 3.1k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

Long structured documents, which is what filings and contracts are, are poorly served by embedding search. This builds a hierarchical index and navigates it by reasoning, so "find the change-of-control clause" lands on the clause rather than five pages that mention control.

**Why it's interesting**

It questions the default assumption that everything must become vectors, and for documents with real internal structure the argument is convincing.

**Good for**

- Long documents
- Contract navigation
- Document search

**Limitations**

Newer approach with less production evidence than vector search. Reasoning over an index costs more per query than a similarity lookup.

**Links:** [GitHub](https://github.com/VectifyAI/PageIndex) &nbsp;·&nbsp; [Site](https://pageindex.ai)

---

### Zerox

> OCR using vision models rather than an OCR engine.

`getomni-ai/zerox` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Data Rooms & Document Intelligence |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 12.3k |
| **Forks** | 846 |
| **Language** | TypeScript |
| **Status** | Dormant (last push 2025-05-20, 16mo) |
| **Self-hostable** | partial (open core) |

**VC use case**

For the documents that break conventional parsers, messy scans, unusual layouts, handwriting, sending each page to a vision model often works when Tesseract does not. Useful as the escalation step for the handful of pages that resist everything else.

**Why it's interesting**

It uses general vision models as the OCR engine, which means new document types often work without new training.

**Good for**

- Difficult documents
- Layout extraction
- Escalation path

**Limitations**

Costs per page and sends document images to a model provider, which is usually a non-starter for unredacted deal material. Slower than local OCR.

**Links:** [GitHub](https://github.com/getomni-ai/zerox) &nbsp;·&nbsp; [Site](https://getomni.ai/ocr-demo)

---
