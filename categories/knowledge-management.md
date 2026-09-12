# Knowledge Management

_Institutional memory beats individual memory._

Knowledge graphs, RAG, semantic search, vector databases, research notebooks, and internal memory.

**25 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-12

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

---

### RAGFlow

> A retrieval system built around deep document understanding.

`infiniflow/ragflow` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 90.6k |
| **Forks** | 10.7k |
| **Language** | Go |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

The knowledge layer a fund builds once so that memos, filings, and data-room material are answerable with citations. It handles the document parsing that decides whether retrieval works at all, including the tables and layouts that break naive pipelines.

**Why it's interesting**

Most RAG systems treat documents as flat text and then wonder why answers are wrong. This one treats parsing as the foundation, which is the correct order.

**Good for**

- Document RAG
- Institutional memory
- Data-room search

**Limitations**

A substantial deployment with several components. Retrieval quality still depends on document preparation.

**Links:** [GitHub](https://github.com/infiniflow/ragflow) &nbsp;·&nbsp; [Site](https://ragflow.io)

---

### Mem0

> A memory layer for assistants that persists across sessions.

`mem0ai/mem0` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 65.2k |
| **Forks** | 7.6k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

Stops an internal research assistant from forgetting everything between sessions: a fund's preferences, prior conclusions, and who asked what. Relevant when building tooling people use repeatedly rather than once.

**Why it's interesting**

It separates memory from the model, so the accumulated context survives a model change or a provider switch, which matters over a fund's timeline.

**Good for**

- Agent memory
- Internal tools
- Institutional memory

**Limitations**

Memory quality depends on what gets extracted and stored, and wrong memories persist quietly. A hosted option exists alongside the open code.

**Links:** [GitHub](https://github.com/mem0ai/mem0) &nbsp;·&nbsp; [Site](https://mem0.ai)

---

### Milvus

> A vector database built for scale.

`milvus-io/milvus` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 46.1k |
| **Forks** | 4.2k |
| **Language** | Go |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

The storage layer when a fund's search problem grows past a few thousand documents: millions of chunks, filtered by company, sector, and date, with low latency. Relevant for a platform team building shared research infrastructure.

**Why it's interesting**

It is designed for vector search at scale rather than as a library, with the distributed architecture and index options that implies, and it originated as an open project rather than an open core.

**Good for**

- Vector search
- Document RAG
- Internal platforms

**Limitations**

Operationally heavy. A fund with ten thousand documents will be happier with something embedded.

**Links:** [GitHub](https://github.com/milvus-io/milvus) &nbsp;·&nbsp; [Site](https://milvus.io)

---

### Logseq

> A local-first outliner for connected notes.

`logseq/logseq` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | AGPL-3.0 |
| **Stars** | 44.9k |
| **Forks** | 2.8k |
| **Language** | Clojure |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

Where an analyst's own thinking accumulates: meeting notes linked to companies, which link to sectors, which link to a thesis. Over a few years it becomes a private map of a market that no CRM holds.

**Why it's interesting**

Files stay as plain markdown on your machine, so the notebook is portable and survives the tool. The block-level linking is what makes connections appear.

**Good for**

- Personal research
- Note taking
- Thesis building

**Limitations**

Depends on the analyst's discipline: an unmaintained graph is just files. Not a multi-user tool.

**Links:** [GitHub](https://github.com/logseq/logseq) &nbsp;·&nbsp; [Site](https://logseq.com)

---

### Outline

> A team wiki that is fast and pleasant to use.

`outline/outline` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unverified (Other) |
| **Stars** | 40.5k |
| **Forks** | 3.6k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | partial (open core) |

**VC use case**

The internal knowledge base a fund needs: sector theses, process documentation, and what everyone learned about a market, written down somewhere findable. Also where the research that does not fit a memo lives.

**Why it's interesting**

It is quick to search and pleasant to write in, which is what determines whether a team actually documents anything. Slack and Notion imports ease the move.

**Good for**

- Internal wiki
- Institutional memory
- Process documentation

**Limitations**

Licence is not a standard SPDX identifier, with a hosted commercial product. Search is text-based rather than semantic.

**Links:** [GitHub](https://github.com/outline/outline) &nbsp;·&nbsp; [Site](https://www.getoutline.com)

---

### LightRAG

> Graph-based retrieval without GraphRAG's cost.

`HKUDS/LightRAG` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 39.6k |
| **Forks** | 5.6k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

The pragmatic middle: entity and relationship retrieval over a fund's document set without the indexing bill that makes graph RAG impractical at small scale. A fund can run it over a few hundred memos and filings.

**Why it's interesting**

It keeps the graph structure while cutting the cost dramatically, and it is published with an evaluation rather than only a claim.

**Good for**

- Document RAG
- Relationship questions
- Institutional memory

**Limitations**

Less capable than a full graph build on large, complex corpora. Emerging project relative to the established frameworks.

**Links:** [GitHub](https://github.com/HKUDS/LightRAG) &nbsp;·&nbsp; [Site](https://arxiv.org/abs/2410.05779)

---

### GraphRAG

> Retrieval that builds a knowledge graph from your documents.

`microsoft/graphrag` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 36k |
| **Forks** | 3.8k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-08) |
| **Self-hostable** | yes |

**VC use case**

The questions a fund asks are relational: which companies in this sector share an investor, which founders came from the same company, where does this supply chain concentrate. Flat similarity search cannot answer those. GraphRAG builds the entity graph and the community summaries that make them answerable.

**Why it's interesting**

It targets the multi-hop questions that make plain RAG look broken, and the approach comes from Microsoft Research with the method published.

**Good for**

- Relationship questions
- Sector mapping
- Document RAG

**Limitations**

Indexing is expensive: it calls a model many times per document set. Best suited to a corpus you will query repeatedly rather than a one-off.

**Links:** [GitHub](https://github.com/microsoft/graphrag) &nbsp;·&nbsp; [Site](https://microsoft.github.io/graphrag/)

---

### Qdrant

> A vector search engine with useful filtering.

`qdrant/qdrant` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 34.5k |
| **Forks** | 2.7k |
| **Language** | Rust |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

The usual choice for a fund's document search: semantic retrieval combined with hard filters, so a query can be scoped to one company or one vintage. The filtering is what makes venture search usable rather than a toy.

**Why it's interesting**

Filtering during search rather than after is the technical detail that separates a usable system from one that returns the wrong company's numbers. Written in Rust, so it runs on modest hardware.

**Good for**

- Vector search
- Document RAG
- Portfolio search

**Limitations**

You still need to handle parsing, chunking, and embeddings yourself. Scaling beyond one machine requires the distributed setup.

**Links:** [GitHub](https://github.com/qdrant/qdrant) &nbsp;·&nbsp; [Site](https://qdrant.tech)

---

### SurrealDB

> One database for documents, graphs, and vectors.

`surrealdb/surrealdb` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | unverified (Other) |
| **Stars** | 33k |
| **Forks** | 1.4k |
| **Language** | Rust |
| **Status** | Active (last push 2026-09-07) |
| **Self-hostable** | yes |

**VC use case**

Attractive for a fund's internal data model, where the same record is a company, a node in an investment graph, and a set of embeddings. One database removes the synchronisation work between three.

**Why it's interesting**

It collapses several data models into one query surface, which is exactly the shape of venture data: relational, graph, and semantic at once.

**Good for**

- Internal platforms
- Knowledge graphs
- Vector search

**Limitations**

Younger than the databases it replaces, so operational experience is thinner. Licence is not a standard SPDX identifier.

**Links:** [GitHub](https://github.com/surrealdb/surrealdb) &nbsp;·&nbsp; [Site](https://surrealdb.com)

---

### Onyx

> Search across everything a team has, with connectors.

`onyx-dot-app/onyx` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unverified (Other) |
| **Stars** | 32k |
| **Forks** | 4.4k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | partial (open core) |

**VC use case**

The whole-company search problem: documents, wikis, chat, and code connected and searchable by anyone, including an assistant. For a fund, that means deal material stops being findable only by whoever filed it.

**Why it's interesting**

The connector catalogue is the substance here. Internal search fails on coverage rather than on ranking, and this connects to the systems where the knowledge actually sits.

**Good for**

- Internal search
- Institutional memory
- Knowledge management

**Limitations**

Real infrastructure to run, and the licence is not a standard SPDX identifier. Value depends on connecting it to systems that have good permissions.

**Links:** [GitHub](https://github.com/onyx-dot-app/onyx) &nbsp;·&nbsp; [Site](https://onyx.app)

---

### Graphiti

> A temporal knowledge graph for agents.

`getzep/graphiti` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 30.8k |
| **Forks** | 3.1k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

Tracks how facts change over time, which is what a fund actually needs: this company's headcount, valuation, and leadership as of each date, not a single current snapshot. Matters for anything that reasons about a portfolio's history.

**Why it's interesting**

Most memory systems overwrite the past. Keeping validity windows on facts is the correct model for investment research, where what you believed in March matters.

**Good for**

- Agent memory
- Portfolio history
- Knowledge graphs

**Limitations**

Needs a graph database and an LLM. Extracting facts reliably from messy documents remains the hard part.

**Links:** [GitHub](https://github.com/getzep/graphiti) &nbsp;·&nbsp; [Site](https://help.getzep.com/graphiti)

---

### Cognee

> Persistent memory built from your documents.

`topoteretes/cognee` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 30.7k |
| **Forks** | 3k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

Gives an internal agent a memory of a fund's documents and prior research, so questions get answered against accumulated context rather than starting fresh each session. The infrastructure behind a research assistant that improves with use.

**Why it's interesting**

It builds the graph and vector representations together and exposes them as memory, which is closer to how a person accumulates context on a sector.

**Good for**

- Agent memory
- Institutional memory
- Document RAG

**Limitations**

Early project with a lot of surface area. Needs a database and model keys, and quality depends on document preparation.

**Links:** [GitHub](https://github.com/topoteretes/cognee) &nbsp;·&nbsp; [Site](https://www.cognee.ai)

---

### Chroma

> An embedded vector store for small projects.

`chroma-core/chroma` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 29.3k |
| **Forks** | 2.5k |
| **Language** | Rust |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

The right choice for a prototype or a single-analyst tool: a persistent vector store that runs inside your Python process with no server. Gets a research assistant working in an afternoon.

**Why it's interesting**

It treats embedding storage as a local library rather than a service, which is what most early experiments actually need.

**Good for**

- Prototyping
- Vector search
- Document RAG

**Limitations**

Not for scale or multi-user production. The hosted product is the commercial path.

**Links:** [GitHub](https://github.com/chroma-core/chroma) &nbsp;·&nbsp; [Site](https://www.trychroma.com/)

---

### Wiki.js

> A modern wiki on Node.

`requarks/wiki` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | AGPL-3.0 |
| **Stars** | 28.9k |
| **Forks** | 3.3k |
| **Language** | Vue |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

The documentation layer for a fund's internal processes and investment theses, structured and permissioned, with a markdown-first workflow that technical team members will actually maintain.

**Why it's interesting**

It supports markdown and git-backed storage, so documentation can be versioned and reviewed like code rather than drifting in a page nobody owns.

**Good for**

- Internal wiki
- Process documentation
- Knowledge management

**Limitations**

AGPL-licensed, which matters if you host it for others. Fewer real-time collaboration features than the modern alternatives.

**Links:** [GitHub](https://github.com/requarks/wiki) &nbsp;·&nbsp; [Site](https://js.wiki)

---

### Haystack

> A framework for retrieval pipelines with evaluation.

`deepset-ai/haystack` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 26.5k |
| **Forks** | 3.1k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

For a platform team building shared research infrastructure, it provides the pieces and the evaluation tooling that tells you whether a pipeline actually works before an analyst depends on it.

**Why it's interesting**

It treats evaluation as part of the framework, which matters when the output feeds an investment decision and someone will ask how the system performs.

**Good for**

- Internal platforms
- Document RAG
- Pipeline evaluation

**Limitations**

Another framework to learn, and its abstractions change between major versions. Overkill for a single document set.

**Links:** [GitHub](https://github.com/deepset-ai/haystack) &nbsp;·&nbsp; [Site](https://haystack.deepset.ai)

---

### pgvector

> Vector search inside Postgres.

`pgvector/pgvector` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | unverified (Other) |
| **Stars** | 23k |
| **Forks** | 1.3k |
| **Language** | C |
| **Status** | Active (last push 2026-09-10) |
| **Self-hostable** | yes |

**VC use case**

If a fund's data already lives in Postgres, this adds embeddings to the same database rather than adding a system to operate. Attractive to small teams because there is one backup, one permission model, and one place to look.

**Why it's interesting**

It removes an entire piece of infrastructure from the stack. For most fund-sized corpora, that trade beats a dedicated vector database.

**Good for**

- Vector search
- Postgres stacks
- Internal tools

**Limitations**

Not built for billions of vectors, and index build times grow. Tuning matters more than it does with a purpose-built engine.

**Links:** [GitHub](https://github.com/pgvector/pgvector)

---

### Marimo

> A reactive Python notebook that is reproducible by design.

`marimo-team/marimo` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 22.7k |
| **Forks** | 1.3k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

Solves the notebook problem that bites every fund analyst: hidden state means results depend on the order cells were run, so a number in a memo cannot be reproduced. Marimo notebooks run as a dependency graph and always produce the same output.

**Why it's interesting**

Reactivity removes an entire class of embarrassing error in research code, and the notebooks are stored as plain Python rather than JSON, so they diff and review cleanly.

**Good for**

- Reproducible analysis
- Research notebooks
- Diligence models

**Limitations**

Different enough from Jupyter that existing notebooks need reworking. Younger ecosystem of extensions.

**Links:** [GitHub](https://github.com/marimo-team/marimo) &nbsp;·&nbsp; [Site](https://marimo.io)

---

### Dgraph

> A graph database built for scale.

`dgraph-io/dgraph` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 21.8k |
| **Forks** | 1.6k |
| **Language** | Go |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

For a fund whose relationship graph spans tens of thousands of companies, people, and rounds, and needs to answer path and pattern queries quickly. Deeper than a file-based graph library will take you.

**Why it's interesting**

It handles distributed graph storage and traversal at a scale where in-memory tools stop working, with a query language designed for graph patterns.

**Good for**

- Relationship graphs
- Co-investment analysis
- Large datasets

**Limitations**

Operationally involved, and the project's direction has changed hands, so check the current state before committing.

**Links:** [GitHub](https://github.com/dgraph-io/dgraph) &nbsp;·&nbsp; [Site](https://dgraph.io)

---

### Docmost

> A collaborative wiki with real-time editing.

`docmost/docmost` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | AGPL-3.0 |
| **Stars** | 21.7k |
| **Forks** | 1.6k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

Closer to a shared workspace than a wiki: multiple people editing a sector map or a diligence checklist at once, in a space per deal. Useful for a fund whose research is collaborative rather than individual.

**Why it's interesting**

Real-time collaboration is missing from most open knowledge tools, and this is one of the few that provides it with permissions and spaces.

**Good for**

- Collaborative research
- Internal wiki
- Deal workspaces

**Limitations**

AGPL-licensed with a commercial cloud, and younger than the established options. Search is basic.

**Links:** [GitHub](https://github.com/docmost/docmost) &nbsp;·&nbsp; [Site](https://docmost.com)

---

### Neo4j

> The standard graph database.

`neo4j/neo4j` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | GPL-3.0 |
| **Stars** | 17.2k |
| **Forks** | 2.7k |
| **Language** | Java |
| **Status** | Active (last push 2026-09-10) |
| **Self-hostable** | partial (open core) |

**VC use case**

Where a fund's relationship graph lives when it outgrows NetworkX: people, companies, funds, and the investments and board seats connecting them, queryable by path. The warm-introduction and co-investment questions get much easier.

**Why it's interesting**

Its query language is the one people learn for graphs, and the tooling for exploring a graph visually is mature. Co-investment and interlock analysis map onto it directly.

**Good for**

- Relationship graphs
- Co-investment analysis
- Warm introduction paths

**Limitations**

Community edition is GPL with the clustering and enterprise features commercial. A graph is only as good as the data loaded into it.

**Links:** [GitHub](https://github.com/neo4j/neo4j) &nbsp;·&nbsp; [Site](http://neo4j.com)

---

### Weaviate

> A vector database with hybrid search built in.

`weaviate/weaviate` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | unverified (Other) |
| **Stars** | 16.8k |
| **Forks** | 1.4k |
| **Language** | Go |
| **Status** | Active (last push 2026-09-12) |
| **Self-hostable** | yes |

**VC use case**

Combines keyword and semantic search, which matters because venture search often involves exact identifiers: a company name, a fund name, a person. Pure vector search handles those badly.

**Why it's interesting**

Hybrid retrieval out of the box, with a schema that supports the typed objects a fund works with, rather than only opaque vectors.

**Good for**

- Vector search
- Document RAG
- Internal platforms

**Limitations**

Operationally heavier than an embedded option, and the licence is not a standard SPDX identifier, with a commercial cloud product alongside.

**Links:** [GitHub](https://github.com/weaviate/weaviate) &nbsp;·&nbsp; [Site](https://weaviate.io/developers/weaviate/)

---

### Zotero

> A reference manager for research material.

`zotero/zotero` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | unverified (Other) |
| **Stars** | 15.2k |
| **Forks** | 1.1k |
| **Language** | JavaScript |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

Anyone doing research across papers, reports, and filings needs citations that hold up. This stores sources with metadata and generates citations, which is the difference between a claim and a sourced claim in a memo.

**Why it's interesting**

It has been the standard open reference manager for years, with browser capture and a large plugin ecosystem, so the workflow is established rather than improvised.

**Good for**

- Research sources
- Citation management
- Technical diligence

**Limitations**

Storage and sync for large libraries need care, and the group features are weaker than the personal ones. Not built for team-scale collaboration.

**Links:** [GitHub](https://github.com/zotero/zotero) &nbsp;·&nbsp; [Site](https://www.zotero.org)

---

### txtai

> Embeddings, search, and workflows in one library.

`neuml/txtai` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | Apache-2.0 |
| **Stars** | 12.9k |
| **Forks** | 891 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

A single dependency that covers semantic search, a vector index, and a small workflow layer, which is enough for a fund to ship an internal search tool without assembling four components.

**Why it's interesting**

It bundles what other stacks spread across several projects, and it runs without a server, so an analyst can build something usable on a laptop.

**Good for**

- Internal search
- Document RAG
- Prototyping

**Limitations**

Smaller community, and the bundled approach means less flexibility than composing dedicated tools.

**Links:** [GitHub](https://github.com/neuml/txtai) &nbsp;·&nbsp; [Site](https://neuml.github.io/txtai)

---

### Jupyter Book

> Publish notebooks as a documented site.

`jupyter-book/jupyter-book` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | BSD-3-Clause |
| **Stars** | 4.3k |
| **Forks** | 730 |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-09) |
| **Self-hostable** | yes |

**VC use case**

Turns a fund's analyses into something a team can read: a research site where the code, the charts, and the writing stay together, so a sector study is reproducible rather than a deck.

**Why it's interesting**

It closes the gap between the notebook where an analysis happened and the artifact other people can read, which is where most internal research dies.

**Good for**

- Publishing research
- Reproducible analysis
- Internal documentation

**Limitations**

Needs the toolchain maintained, and non-technical readers will find the format unfamiliar. Not a knowledge base for general notes.

**Links:** [GitHub](https://github.com/jupyter-book/jupyter-book) &nbsp;·&nbsp; [Site](https://jupyterbook.org)

---

### RAG Techniques

> Worked examples of retrieval techniques, with the reasoning.

`NirDiamant/RAG_Techniques` &nbsp;·&nbsp; 📚 **Research** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _research_

| | |
|---|---|
| **Category** | Knowledge Management |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | unverified (Other) |
| **Stars** | 29.4k |
| **Forks** | 3.6k |
| **Language** | Jupyter Notebook |
| **Status** | Active (last push 2026-09-04) |
| **Self-hostable** | yes |

**VC use case**

When a document Q&A system gives bad answers, the fix is usually a retrieval technique rather than a better model. This is the catalogue of those techniques with runnable notebooks, so a platform team can diagnose rather than guess.

**Why it's interesting**

It explains when each technique helps and what it costs, which is more useful than the list of methods alone.

**Good for**

- Learning retrieval
- Diagnosing pipelines
- Internal tooling

**Limitations**

Teaching material, not a library: the code is illustrative and needs adapting. Licence is not a standard SPDX identifier.

**Links:** [GitHub](https://github.com/NirDiamant/RAG_Techniques) &nbsp;·&nbsp; [Site](https://diamant-ai.com)

---
