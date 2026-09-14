# Market & Industry Research

_Build the map before you take the meeting._

Market mapping, competitive research, industry intelligence, company comparison, and trend detection.

**16 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-14

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

---

### Khoj

> Search your own documents and the web from one place.

`khoj-ai/khoj` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Market & Industry Research |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | AGPL-3.0 |
| **Stars** | 37.3k |
| **Forks** | 2.5k |
| **Language** | Python |
| **Status** | Active (last push 2026-08-02) |
| **Self-hostable** | yes |

**VC use case**

A fund's institutional memory problem: a hundred memos, data-room exports, and meeting notes that nobody can search. Khoj indexes them and answers questions against both those files and the open web, so "what did we say about this company in 2024" stops being a Slack thread.

**Why it's interesting**

It can be self-hosted entirely, which matters when the corpus is deal material. It also runs against local models, so nothing has to leave your infrastructure.

**Good for**

- Institutional memory
- Document search
- Research

**Limitations**

Indexing quality depends on the source documents being reasonably clean. The self-hosted path needs ongoing maintenance, and large corpora need real hardware.

**Links:** [GitHub](https://github.com/khoj-ai/khoj) &nbsp;·&nbsp; [Site](https://khoj.dev)

---

### STORM

> Writes a cited article from scratch on any topic.

`stanford-oval/storm` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Market & Industry Research |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 31.3k |
| **Forks** | 2.9k |
| **Language** | Python |
| **Status** | Active (last push 2025-09-30) |
| **Self-hostable** | yes |

**VC use case**

Ask it to produce a briefing on a sector and it researches, outlines, and drafts with references. Analysts use it for the market section of an investment memo, then edit down rather than start at a blank page.

**Why it's interesting**

It came out of Stanford's Oval lab and mimics how a reporter works: generate the questions a knowledgeable reader would ask, research each, then write. The question-generation step is what lifts it above summarize-the-top-ten-results.

**Good for**

- Market research
- Memo drafting
- Sector briefings

**Limitations**

Still needs an editor. It will produce fluent text about a market it has misunderstood, and the reference list occasionally includes sources it read thinly.

**Links:** [GitHub](https://github.com/stanford-oval/storm) &nbsp;·&nbsp; [Site](http://storm.genie.stanford.edu)

---

### GPT Researcher

> An agent that researches a question across many sources and cites them.

`assafelovic/gpt-researcher` &nbsp;·&nbsp; ⭐ **Essential** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Market & Industry Research |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 29.4k |
| **Forks** | 4k |
| **Language** | Python |
| **Status** | Active (last push 2026-08-27) |
| **Self-hostable** | yes |

**VC use case**

Hand it a market question, such as how many companies are selling continuous compliance tooling into European banks and who funded them, and it returns a written answer with the sources it used. This covers the desk research that otherwise eats an analyst's first two days on a new thesis.

**Why it's interesting**

It plans sub-questions and searches in parallel rather than issuing one query, and it keeps a source list attached to every claim. The citation trail is what makes it usable in a memo where someone will ask where a number came from.

**Good for**

- Market research
- Thesis building
- Competitive research

**Limitations**

Needs an LLM key and a search API, so cost scales with use. It can restate a weak source confidently, and every citation still needs opening.

**Dependencies:** Python 3.11+, OpenAI or another LLM provider, search API key

**Links:** [GitHub](https://github.com/assafelovic/gpt-researcher) &nbsp;·&nbsp; [Site](https://gptr.dev)

---

### TrendRadar

> Aggregated trend and sentiment monitoring across platforms.

`sansan0/TrendRadar` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Market & Industry Research |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | GPL-3.0 |
| **Stars** | 62.2k |
| **Forks** | 24.9k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-13) |
| **Self-hostable** | yes |

**VC use case**

Tracks what is rising across social platforms, news, and RSS and sends alerts on chosen keywords. For a consumer-facing fund this is how a trend gets on the radar before it shows up in a pitch deck.

**Why it's interesting**

It aggregates across many platforms behind one feed and supports keyword rules rather than a single dashboard, so alerts can be tuned to a thesis.

**Good for**

- Consumer trend research
- Signal monitoring
- Brand monitoring

**Limitations**

Volume is the enemy: without tight keyword rules the alerts become noise. It reflects online attention, which is not the same as market demand.

**Links:** [GitHub](https://github.com/sansan0/TrendRadar) &nbsp;·&nbsp; [Site](https://trendradar.sandev.cc)

---

### Tongyi DeepResearch

> An open deep-research agent with published weights.

`Alibaba-NLP/DeepResearch` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _research_

| | |
|---|---|
| **Category** | Market & Industry Research |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 19.9k |
| **Forks** | 1.5k |
| **Language** | Python |
| **Status** | Active (last push 2026-02-27) |
| **Self-hostable** | yes |

**VC use case**

For funds that cannot send research questions to a hosted API, this runs research loops against a self-hosted model. Relevant when the question involves a target's confidential material or a sector you would rather not query through a vendor.

**Why it's interesting**

The model weights are open, which is rare for research agents, so the whole loop can run inside your own infrastructure. Its benchmark results are published with the code, so claims are checkable.

**Good for**

- Confidential research
- Self-hosted research
- Model evaluation

**Limitations**

Needs serious GPU capacity to run well. Setup is a research-engineering job, not an afternoon install.

**Links:** [GitHub](https://github.com/Alibaba-NLP/DeepResearch) &nbsp;·&nbsp; [Site](https://tongyi-agent.github.io/blog/introducing-tongyi-deep-research/)

---

### deep-research

> A small, readable iterative research loop.

`dzhng/deep-research` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Market & Industry Research |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 19.7k |
| **Forks** | 2k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-04-11) |
| **Self-hostable** | yes |

**VC use case**

The version to read if you want to build your own research agent: it searches, reads, generates follow-up questions, and recurses to a depth you set. Funds building internal tooling use it as the reference implementation.

**Why it's interesting**

The whole thing is a few files. For understanding how deep research actually works, that beats reading a framework's documentation.

**Good for**

- Internal tooling
- Learning agent design
- Prototyping

**Limitations**

Minimal by design: no UI, thin error handling, and no provenance beyond the source list. Treat it as a starting point rather than a product.

**Links:** [GitHub](https://github.com/dzhng/deep-research)

---

### DocsGPT

> Chat over your own document collections.

`arc53/DocsGPT` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Market & Industry Research |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 18.3k |
| **Forks** | 2.1k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | yes |

**VC use case**

Point it at a data room, a set of competitor filings, or a folder of sector reports and ask questions. Useful for the first pass over a hundred PDFs before deciding which twenty deserve a careful read.

**Why it's interesting**

It includes an agent builder and supports many file formats, so a fund can stand up a private research assistant without building retrieval plumbing.

**Good for**

- Data-room triage
- Document Q&A
- Research

**Limitations**

Retrieval quality is only as good as the chunking, and answers need verification against the page. Self-hosting is a real deployment.

**Links:** [GitHub](https://github.com/arc53/DocsGPT) &nbsp;·&nbsp; [Site](https://app.docsgpt.cloud/)

---

### SurfSense

> NotebookLM-style research over live web and platform data.

`MODSetter/SurfSense` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Market & Industry Research |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unverified (Other) |
| **Stars** | 16.1k |
| **Forks** | 1.5k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

Research a market using current Reddit, YouTube, and social data rather than whatever a search index has cached. For consumer theses, what users say in communities is often better evidence than the press release.

**Why it's interesting**

It pairs a personal knowledge base with connectors to platforms that do not expose search well, which is where the useful consumer signal actually sits.

**Good for**

- Consumer research
- Community research
- Knowledge management

**Limitations**

Platform connectors break as those platforms change access, and coverage is uneven. Licence is not a standard SPDX identifier, so check terms.

**Links:** [GitHub](https://github.com/MODSetter/SurfSense) &nbsp;·&nbsp; [Site](https://www.surfsense.com)

---

### MiroThinker

> A research agent tuned for prediction and forecasting tasks.

`MiroMindAI/MiroThinker` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _research_

| | |
|---|---|
| **Category** | Market & Industry Research |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 8.4k |
| **Forks** | 646 |
| **Language** | Python |
| **Status** | Active (last push 2026-07-06) |
| **Self-hostable** | yes |

**VC use case**

Built for questions with a checkable answer, such as whether a market will grow at a given rate. Funds use this class of model to pressure-test a forecast rather than to write prose about a sector.

**Why it's interesting**

It is optimised for prediction rather than summarisation, and the benchmarks it reports are the forecasting ones rather than generic QA.

**Good for**

- Forecast testing
- Quantitative research
- Model evaluation

**Limitations**

Forecasting accuracy on venture-scale questions is unproven, and the published benchmarks are not drawn from private markets. Treat outputs as one input.

**Links:** [GitHub](https://github.com/MiroMindAI/MiroThinker) &nbsp;·&nbsp; [Site](https://miromind.ai/)

---

### Deep Searcher

> Private-data research with citations.

`zilliztech/deep-searcher` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Market & Industry Research |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 8.3k |
| **Forks** | 803 |
| **Language** | Python |
| **Status** | Active (last push 2025-11-19) |
| **Self-hostable** | yes |

**VC use case**

Runs the deep-research loop over documents you supply rather than the open web, which is what you want for a data room or a portfolio's internal reporting. The question can then be answered against material you are allowed to hold.

**Why it's interesting**

It is built by the team behind Milvus, so the retrieval layer is the part they know best, and it supports several model providers rather than one.

**Good for**

- Data-room research
- Portfolio data
- Private research

**Limitations**

Needs a vector store and an LLM key, and answer quality depends heavily on how the documents were prepared.

**Links:** [GitHub](https://github.com/zilliztech/deep-searcher) &nbsp;·&nbsp; [Site](https://zilliztech.github.io/deep-searcher/)

---

### Situation Monitor

> A dashboard for news, markets, and geopolitical events.

`hipcityreg/situation-monitor` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Market & Industry Research |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unknown |
| **Stars** | 4.2k |
| **Forks** | 919 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-01-13) |
| **Self-hostable** | yes |

**VC use case**

A single screen for the macro backdrop when a fund's thesis depends on rates, conflict, or policy. Analysts keep it open rather than tabbing between five sites.

**Why it's interesting**

It assembles disparate live feeds into one view, which is the useful part; the feeds themselves are public.

**Good for**

- Macro monitoring
- Situational awareness

**Limitations**

No licence file is present, so reuse terms are unclear. Feed availability changes without notice.

**Links:** [GitHub](https://github.com/hipcityreg/situation-monitor) &nbsp;·&nbsp; [Site](https://situation-monitor-rose.vercel.app)

---

### DeepResearchAgent

> A hierarchical multi-agent research system.

`SkyworkAI/DeepResearchAgent` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Market & Industry Research |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 3.5k |
| **Forks** | 456 |
| **Language** | Python |
| **Status** | Active (last push 2026-05-04) |
| **Self-hostable** | yes |

**VC use case**

Shows how to split a research job across planning, browsing, and writing agents with different models for each. Useful if your internal tooling needs to keep cheap models on the busywork and expensive ones on the judgement.

**Why it's interesting**

The hierarchy is explicit and configurable, so cost and quality can be traded off per stage instead of sending every step to the largest model.

**Good for**

- Agent architecture
- Internal tooling
- Cost control

**Limitations**

More moving parts than a single-loop agent, and the coordination overhead is real. Early-stage.

**Links:** [GitHub](https://github.com/SkyworkAI/DeepResearchAgent) &nbsp;·&nbsp; [Site](https://skyworkai.github.io/DeepResearchAgent/)

---

### Hyperresearch

> A research knowledge base that agents keep adding to.

`jordan-gibbs/hyperresearch` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Market & Industry Research |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 3.3k |
| **Forks** | 319 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

Instead of losing research when a deal dies, the findings stay in a queryable store that later agents can search. This is the accumulation problem: a fund does research once and forgets it forever.

**Why it's interesting**

It treats research as a persistent asset rather than a chat log, which is the right shape for an institution that needs memory across analysts and years.

**Good for**

- Institutional memory
- Research archiving
- Agent memory

**Limitations**

Early project, and the value depends on discipline in adding to it. Search quality over a large accumulated corpus is untested.

**Links:** [GitHub](https://github.com/jordan-gibbs/hyperresearch) &nbsp;·&nbsp; [Site](https://hyperresearch.ai)

---

### World Intel MCP

> A large MCP toolset for global intelligence feeds.

`marc-shade/world-intel-mcp` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Market & Industry Research |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 638 |
| **Forks** | 115 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-02) |
| **Self-hostable** | yes |

**VC use case**

Gives an agent access to markets, filings, conflict, and macro feeds through one MCP server, so a research agent can pull current data instead of only reading web pages. Useful for funds whose theses depend on macro or geopolitical conditions.

**Why it's interesting**

It packages a wide set of public data sources behind a standard agent interface, which is the difference between an agent that can look things up and one that just writes from memory.

**Good for**

- Macro research
- Agent tooling
- Geopolitical monitoring

**Limitations**

Young project with a large surface area, so individual tools vary in reliability. Some upstream sources require keys or rate-limit heavily.

**Links:** [GitHub](https://github.com/marc-shade/world-intel-mcp)

---

### WebThinker

> A NeurIPS paper on giving reasoning models the ability to browse.

`RUC-NLPIR/WebThinker` &nbsp;·&nbsp; 📚 **Research** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _research_

| | |
|---|---|
| **Category** | Market & Industry Research |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 1.5k |
| **Forks** | 139 |
| **Language** | Python |
| **Status** | Active (last push 2025-12-08) |
| **Self-hostable** | yes |

**VC use case**

Read it to understand why research agents fail: where browsing breaks the reasoning chain, and what a working loop looks like. Relevant to anyone specifying internal research tooling.

**Why it's interesting**

It is peer-reviewed work with the method and evaluation in the open, which is more than most agent repositories offer.

**Good for**

- Understanding research agents
- Specifying internal tools

**Limitations**

A research implementation, not a product. Expect to read code and papers to use it.

**Links:** [GitHub](https://github.com/RUC-NLPIR/WebThinker) &nbsp;·&nbsp; [Site](https://foremost-beechnut-8ed.notion.site/WebThinker-Empowering-Large-Reasoning-Models-with-Deep-Research-Capability-d13158a27d924a4b9df7f9ab94066b64)

---

### DeepResearch Bench

> A benchmark for judging whether a research agent is any good.

`Ayanami0730/deep_research_bench` &nbsp;·&nbsp; 📚 **Research** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _research_

| | |
|---|---|
| **Category** | Market & Industry Research |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | Apache-2.0 |
| **Stars** | 829 |
| **Forks** | 85 |
| **Language** | Python |
| **Status** | Active (last push 2026-05-11) |
| **Self-hostable** | yes |

**VC use case**

If a fund is choosing between research agents, or building one, this is how to compare them on something other than vibes. It scores both the report and the retrieval behind it.

**Why it's interesting**

It evaluates the retrieval as well as the writing, which is where research agents usually fail. The task set is public, so results are comparable.

**Good for**

- Tool selection
- Agent evaluation
- Internal tooling

**Limitations**

Benchmark tasks are general-purpose rather than venture-specific, so a high score does not mean it can research a market well.

**Links:** [GitHub](https://github.com/Ayanami0730/deep_research_bench) &nbsp;·&nbsp; [Site](https://arxiv.org/pdf/2506.11763)

---
