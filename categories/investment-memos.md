# Investment Memo & IC

_From evidence to a decision the partnership can defend._

Memo generation, IC workflow, scorecards, decision systems, and citation-backed evidence.

**6 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-12

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

**Coverage note.** Memo tooling is the least mature area here, and the reason is straightforward: a memo is the part of the process that most resists automation, because its value is the judgement in it. What these entries offer is scaffolding, typesetting, and reproducibility, which removes the blank-page problem and the copy-paste errors without pretending to make the argument for you.

---

### Typst

> Typesetting that makes documents look considered.

`typst/typst` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Investment Memo & IC |
| **License** | Apache-2.0 |
| **Stars** | 56k |
| **Forks** | 1.7k |
| **Language** | Rust |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

The output quality question that nobody prices: a memo typeset properly reads as considered work, and a Word document with inconsistent spacing does not. Typst produces publication-quality PDFs from markup, so a fund can template its memo format once.

**Why it's interesting**

It gives LaTeX-quality output with a syntax people can learn in an afternoon and compiles fast enough to preview while writing.

**Good for**

- Memo production
- LP reporting
- Document templates

**Limitations**

Not a word processor: collaborators who need to edit in Word are out of the loop unless you convert. Younger ecosystem than LaTeX.

**Links:** [GitHub](https://github.com/typst/typst) &nbsp;·&nbsp; [Site](https://typst.app)

---

### Quarto

> Reproducible reports where the analysis and the document are one file.

`quarto-dev/quarto-cli` &nbsp;·&nbsp; 🔥 **Interesting** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Investment Memo & IC |
| **License** | unverified (Other) |
| **Stars** | 6k |
| **Forks** | 455 |
| **Language** | JavaScript |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

A diligence report where the numbers come from the data rather than being pasted in, so a corrected input updates every figure downstream. That removes the class of error where a number changes and a summary does not.

**Why it's interesting**

It covers notebooks, code, prose, and output formats in one tool, which means a fund's analysis and its deliverables can share a source.

**Good for**

- Diligence reports
- Reproducible analysis
- LP reporting

**Limitations**

Licence is not a standard SPDX identifier. Requires the underlying language runtimes, so the toolchain needs upkeep.

**Links:** [GitHub](https://github.com/quarto-dev/quarto-cli) &nbsp;·&nbsp; [Site](https://quarto.org)

---

### Memo Generator

> Generates a startup investment memorandum.

`dforwardfeed/memo_generator` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Investment Memo & IC |
| **License** | MIT |
| **Stars** | 95 |
| **Forks** | 36 |
| **Language** | JavaScript |
| **Status** | Dormant (last push 2025-01-14, 20mo) |
| **Self-hostable** | yes |

**VC use case**

Assembles a first-draft investment memo from inputs about a company. The honest use is as a scaffold: it prompts the analyst for the sections a memo needs, which is usually where junior writing stalls.

**Why it's interesting**

It targets the actual deliverable of venture work, the memo, rather than the research that precedes it. That framing is rare.

**Good for**

- Memo drafting
- Analyst onboarding
- IC preparation

**Limitations**

Last meaningful activity some time ago, so treat it as a reference implementation to read rather than a tool to adopt. Output needs an investor's judgement throughout.

**Links:** [GitHub](https://github.com/dforwardfeed/memo_generator)

---

### Buffett Investment Research

> A research workflow that starts from primary sources.

`MichaelRochonnn/buffett-investment-research` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Investment Memo & IC |
| **License** | MIT |
| **Stars** | 63 |
| **Forks** | 14 |
| **Language** | Python |
| **Status** | Active (last push 2026-04-08) |
| **Self-hostable** | yes |

**VC use case**

A worked example of the discipline that separates real research from summarisation: go to the primary document, extract what matters, and structure a conclusion with the source attached. Readable as a method even if you never run it.

**Why it's interesting**

It encodes a research standard rather than a prompt, and the primary-source insistence is exactly what diligence reviews are meant to enforce.

**Good for**

- Analyst training
- Research method
- Memo drafting

**Limitations**

Single-author project around one investor's approach, so treat the method as one valid style rather than a standard.

**Links:** [GitHub](https://github.com/MichaelRochonnn/buffett-investment-research)

---

### VC Reporting

> An AI-native platform for fund reporting and analysis.

`tdavidson/reporting` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Investment Memo & IC |
| **License** | Apache-2.0 |
| **Stars** | 52 |
| **Forks** | 15 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

Covers the recurring paperwork a fund owes its LPs and itself: portfolio updates, performance reporting, and the analysis that goes with them. Built by an investor, which shows in what it chooses to automate.

**Why it's interesting**

Most fund software is built by engineers guessing at investor workflows. This one started from the reporting obligation, which is the part with a deadline attached.

**Good for**

- LP reporting
- Portfolio reporting
- Fund operations

**Limitations**

Small project by an individual investor, so continuity is a real question. Early.

**Links:** [GitHub](https://github.com/tdavidson/reporting) &nbsp;·&nbsp; [Site](https://portfolio.hemrock.com)

---

### TickerToThesis

> A research pipeline that produces an investment memo.

`jasonfdg/TickerToThesis` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Investment Memo & IC |
| **License** | unknown |
| **Stars** | 26 |
| **Forks** | 8 |
| **Language** | Python |
| **Status** | Active (last push 2026-02-04) |
| **Self-hostable** | yes |

**VC use case**

Takes a ticker, gathers public research, and drafts a memo in the shape a buyside analyst would expect. Worth reading for the section structure alone, which translates to private deals.

**Why it's interesting**

The pipeline is the point: it shows the sequence from raw filings to a written thesis, which is the process a fund is really trying to automate.

**Good for**

- Memo drafting
- Research pipelines
- Analyst training

**Limitations**

No licence file, so terms are unclear. Public-company inputs, and the writing still needs a human with a view.

**Links:** [GitHub](https://github.com/jasonfdg/TickerToThesis)

---
