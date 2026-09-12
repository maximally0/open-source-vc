# Build Your Own VC Stack

How the pieces fit together. This is an architecture page, not a product proposal: the point is to show which layer does what, why the order matters, and where a fund gets stuck.

```text
        Public web, filings, registries
                    │
              [ Collection ]            crawl, monitor, archive
                    │
              [ Parsing ]               documents → structured data
                    │
              [ Storage ]               relational + graph + vectors
                    │
              [ Retrieval ]             search, graph, citations
                    │
              [ Reasoning ]             agents, models, humans
                    │
              [ Application ]           tools people actually open
                    │
              [ Automation ]            schedules, triggers, alerts
                    │
             (back to Collection)
```

Each layer is useful alone. Most funds start in the middle and work outward, which is usually the wrong order.

---

## Layer 1: Collection

**What it does:** gets data from the outside world into your infrastructure.

**Tools:** [Scrapy](../categories/osint.md) for volume, [Crawlee](../categories/osint.md) or [Playwright](../categories/osint.md) when the page needs JavaScript, [Firecrawl](../categories/osint.md) when the target is text for a model, [SingleFile](../categories/osint.md) for evidence capture, [changedetection.io](../categories/deal-sourcing.md) for recurring monitoring, [Airbyte](../categories/automation.md) when the source has an API, [edgartools](../categories/investment-analysis.md) for filings.

**The decision that matters:** push or pull. A single crawl is a script. Recurring collection is a scheduled job with state, deduplication, and failure handling, which is a different engineering problem and the one funds underestimate. Decide which you are building before you write either.

**Where funds get stuck:** collecting everything. Coverage is cheap; the cost is in the parsing and the maintenance when a source changes its markup. Two well-maintained sources beat twenty fragile ones, every time.

## Layer 2: Parsing

**What it does:** turns documents into data.

**Tools:** [OCRmyPDF](../categories/document-intelligence.md) for scans, [Docling](../categories/document-intelligence.md) or [Marker](../categories/document-intelligence.md) for layout, [PaddleOCR](../categories/document-intelligence.md) for non-Latin scripts, [Camelot](../categories/document-intelligence.md) and [pdfplumber](../categories/document-intelligence.md) for tables, [Unstructured](../categories/document-intelligence.md) for format breadth, [Arelle](../categories/standards.md) and [edgartools](../categories/investment-analysis.md) for filings.

**The decision that matters:** whether you need layout. If you are searching text, plain extraction is fine. If you are pulling numbers out of a financial statement, the position of a figure in a table is part of the data, and losing it produces confidently wrong analysis. This is the single most consequential choice in the stack.

**Where funds get stuck:** skipping this layer and blaming retrieval. Almost every "the AI gives bad answers about our documents" problem traces back to a parse that flattened tables into a word salad.

## Layer 3: Storage

**What it does:** holds the data in a shape that answers your questions.

**Tools:** [Postgres with pgvector](../categories/knowledge-management.md) covers relational, JSON, and vector in one system, which is the right default. [Qdrant](../categories/knowledge-management.md) or [Milvus](../categories/knowledge-management.md) when vector search outgrows it, [Neo4j](../categories/knowledge-management.md) or [NetworkX](../categories/relationship-intelligence.md) for relationship queries, [Milvus](../categories/knowledge-management.md) and friends only at real scale.

**The decision that matters:** how many systems you are willing to operate. Every additional store is another backup, another permission model, and another thing that can be out of sync. For a fund with fewer than a million documents, one Postgres is almost always the right answer, and the graph work can be done on top of it with [NetworkX](../categories/relationship-intelligence.md).

**Where funds get stuck:** a graph database they do not need yet, containing data they have not cleaned.

## Layer 4: Retrieval

**What it does:** finds the right things for a question.

**Tools:** [RAGFlow](../categories/knowledge-management.md) or [LlamaIndex](../categories/ai-agents.md) for document retrieval, [GraphRAG](../categories/knowledge-management.md) or [LightRAG](../categories/knowledge-management.md) when the question is relational, [Qdrant](../categories/knowledge-management.md) for filtered semantic search, [Outline](../categories/knowledge-management.md) or [Paperless-ngx](../categories/document-intelligence.md) for keyword search over a corpus that does not need a model.

**The decision that matters:** not everything needs embeddings. A company name is a keyword. A clause about change of control is a concept. Matching the retrieval method to the question type is what separates a usable system from a demo, and hybrid search beats pure vector search for most venture data because analysts search by identifier constantly.

**Where funds get stuck:** indexing a corpus they will query twice. [GraphRAG](../categories/knowledge-management.md) costs real money to build; it earns that back on a document set you interrogate repeatedly, not on a one-off diligence.

## Layer 5: Reasoning

**What it does:** turns retrieved material into an answer, a summary, or a decision.

**Tools:** [GPT Researcher](../categories/market-research.md) or [STORM](../categories/market-research.md) for open-ended research, [paper-qa](../categories/due-diligence.md) for citation-backed technical answers, [browser-use](../categories/ai-agents.md) for sources without APIs, [LangGraph](../categories/ai-agents.md) where steps must be explicit and a human must approve, [DSPy](../categories/ai-agents.md) when the pipeline must survive a model upgrade.

**The decision that matters:** how much of this is an agent. An agent is worth its cost when the path is unknown and the steps depend on what is found. When the steps are known, a script with a model call in the middle is cheaper, faster, and far easier to debug. Most "we need an agent" conversations are really "we need a short pipeline".

**Where funds get stuck:** no human in the loop for anything that goes into a memo. A model that cites its sources is checkable; one that produces fluent prose is not, and the difference matters when a partner asks where a number came from.

## Layer 6: Application

**What it does:** is what people actually open.

**Tools:** [Streamlit](../categories/portfolio-management.md) and [Gradio](../categories/portfolio-management.md) for analyst tools, [Metabase](../categories/portfolio-management.md) and [Superset](../categories/portfolio-management.md) for dashboards, [Appsmith](../categories/automation.md) or [ToolJet](../categories/automation.md) for internal screens, [NocoDB](../categories/deal-sourcing.md) and [Baserow](../categories/portfolio-management.md) for grids, [Datasette](../categories/portfolio-management.md) for exploring a database, [Docmost](../categories/knowledge-management.md) or [Outline](../categories/knowledge-management.md) for the writing.

**The decision that matters:** who builds it. The best internal tools are built by the person who understands the process, and the tools that enable that are worth more than the ones with the better feature list. A partner-maintained Baserow beats an engineer-maintained web app that took three months.

**Where funds get stuck:** building for the fund's processes as they are described, rather than as they happen. Shadow spreadsheets are the symptom; ask why they exist.

## Layer 7: Automation

**What it does:** runs the whole thing without anyone remembering to.

**Tools:** [n8n](../categories/automation.md) and [Activepieces](../categories/automation.md) for glue and triggers, [Airflow](../categories/automation.md), [Prefect](../categories/automation.md), [Dagster](../categories/automation.md), or [Kestra](../categories/automation.md) for scheduled pipelines, [dbt](../categories/automation.md) for tested transformations, [changedetection.io](../categories/deal-sourcing.md) for event triggers, [Meltano](../categories/automation.md) for declarative data movement.

**The decision that matters:** who gets told when it breaks. An automated pipeline that fails silently is worse than a manual process, because you will trust it. Pick the tool that makes failure loud, and make sure the person who can fix it knows they will be told.

**Where funds get stuck:** automating a process they had not yet stabilised. Automate the third time you do something, not the first.

---

## Three complete stacks

Same layers, different trade-offs. The point is not that one is right; it is which costs you are willing to carry.

### The one-analyst stack

Everything on a laptop, no servers, nothing to maintain.

```text
SingleFile + Scrapy        → collection
Docling / pdfplumber       → parsing
SQLite + Datasette         → storage and exploration
Marimo                     → analysis, reproducible
Streamlit                  → one internal tool, run locally
OpenAI/Anthropic API       → reasoning, when needed
```

**Costs:** nothing to operate, works immediately, and every other analyst has to build it themselves. **Breaks when:** a second person needs access, or a job has to run while your laptop is closed.

### The small-fund stack

Shared infrastructure for a team of three to ten, with one person who codes.

```text
Scrapy + Airbyte           → collection
Docling + OCRmyPDF         → parsing
Postgres + pgvector        → storage
RAGFlow or LlamaIndex      → retrieval
LangGraph + an LLM API     → reasoning, with approval gates
Metabase + Streamlit       → application
Airflow or Prefect + dbt   → automation
```

**Costs:** one operator, roughly a week of setup, and a real dependency on that person. **Worth it when:** the fund has more than two analysts and generates research faster than it can find it again.

### The confidential-material stack

For deal material that cannot leave your infrastructure.

```text
Playwright / SingleFile    → collection
Docling + OCRmyPDF         → parsing, local
Rizzo PII                  → strip personal data before any model sees it
Postgres + pgvector        → storage, self-hosted
Qdrant                     → retrieval, self-hosted
Self-hosted model or a     → reasoning, inside the perimeter
  private deployment
OpenHands / local agents   → analysis on your own hardware
```

**Costs:** real hardware, meaningful maintenance, and weaker models than a hosted API. **Worth it when:** an NDA or a privacy obligation actually prohibits third-party processing, which is more often than funds assume but less often than their counsel claims.

---

## What not to build

Stated plainly, because these are the traps:

- **A proprietary-data clone.** You will not out-collect a company whose only product is the dataset, and you will spend a year discovering that.
- **A CRM.** [Twenty](../categories/relationship-intelligence.md), [Monica](../categories/relationship-intelligence.md), and [EspoCRM](../categories/relationship-intelligence.md) exist. Adopt one and spend your time on the parts that are specific to your fund.
- **A fund accounting system.** Regulated, audit-facing, and liable. Use [Beancount](../categories/lp-management.md) or [GnuCash](../categories/lp-management.md) for the books if you must, and hire an administrator for the compliance.
- **A memo writer that makes the argument.** The argument is the job. Scaffolding is fine; delegation is not.

## Where to start

Do not build the stack. Build the one piece that is currently costing your team the most hours, at the lowest layer that fixes it. If analysts cannot find past research, the fix is retrieval, not a new agent. If documents take three days to parse, the fix is the parser.

Read [analyst-stack.md](analyst-stack.md) for the workflow version of this, and [METHODOLOGY.md](../METHODOLOGY.md) for how each tool here was assessed.
