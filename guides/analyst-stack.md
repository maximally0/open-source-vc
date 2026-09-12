# The VC Analyst Stack

Five ways of working, and what to reach for in each. This is the practical companion to [STARTER_PACK.md](../STARTER_PACK.md): that page is a shortlist, this one is a workflow.

Every tool named here is in the directory with a full entry, its licence, and its limitations. Nothing on this page is a product recommendation for its own sake.

---

## If you are doing sourcing

You are trying to answer: which companies exist in this space that I have not heard of, and which of them moved this week?

**Build the list first.** [Scrapy](../categories/osint.md) or [Firecrawl](../categories/osint.md) to collect, [dedupe](../categories/company-discovery.md) to resolve the same company appearing three times under different names, and a database you control. [NocoDB](../categories/deal-sourcing.md) or [Grist](../categories/lp-management.md) if you want a grid rather than a schema. The list is the asset; everything else is maintenance.

**Then watch it.** [changedetection.io](../categories/deal-sourcing.md) for specific pages: pricing, plans, team pages, terms. [Huginn](../categories/deal-sourcing.md) when you want an action rather than a notification. [subsignal](../categories/deal-sourcing.md) if you would rather start from something built for funds. [JobSpy](../categories/founder-discovery.md) for hiring, which is the signal companies find hardest to hide.

**Attribute what comes back.** [Dub](../categories/deal-sourcing.md) on your newsletter, event links, and scout programme, so inbound can be counted per channel rather than described anecdotally.

**The honest caveat:** none of this finds the companies nobody has written about. Open-source sourcing is about collecting and monitoring public signal cheaply; the proprietary company graphs are still commercial products, and pretending otherwise wastes a quarter.

## If you are doing founder research

You have a name and a deck, and you need to know whether the two agree.

**Start with the public footprint.** [Sherlock](../categories/founder-discovery.md) and [Maigret](../categories/founder-discovery.md) for handles, [OpenAlex](../categories/datasets.md) for publication and citation records on a technical founder, [PatentsView](../categories/datasets.md) for patent filings. [Web-Check](../categories/founder-discovery.md) for the company's actual infrastructure.

**Read the technical claim.** [PaperQA](../categories/due-diligence.md) against the founders' papers if the company claims a research result. [shhgit](../categories/due-diligence.md) to see whether their public repositories leak credentials, which says something about engineering practice.

**Capture what you find.** [SingleFile](../categories/osint.md), because team pages, pricing, and claims change, and "the page said X in March" is a sentence you will want to be able to prove.

**Keep it.** A note in [Logseq](../categories/knowledge-management.md), a record in [Monica](../categories/relationship-intelligence.md). Founder research that lives in a chat thread is research you will redo.

## If you are doing diligence

You have a data room and three weeks.

**Get the documents into a usable state first.** [OCRmyPDF](../categories/document-intelligence.md) for scans, [Docling](../categories/document-intelligence.md) or [Marker](../categories/document-intelligence.md) for layout-aware conversion, [Camelot](../categories/document-intelligence.md) or [pdfplumber](../categories/document-intelligence.md) for the tables you will actually compute on. This step is unglamorous and determines whether everything downstream works.

**Ask questions across the whole room.** [RAGFlow](../categories/knowledge-management.md) or [LlamaIndex](../categories/ai-agents.md) with a document parse you trust. [Rizzo PII](../categories/due-diligence.md) first if the material contains personal data and you plan to use a hosted model.

**Verify the technical claims.** [Cleanlab](../categories/due-diligence.md) on their data quality claims, [Phoenix](../categories/due-diligence.md) on their production traces, [paper-qa](../categories/due-diligence.md) on anything research-backed. [company-research-agent](../categories/company-discovery.md) for the market context an analyst would otherwise spend two days assembling.

**Count things properly.** When a finding needs a number rather than an impression, [Label Studio](../categories/due-diligence.md) or [doccano](../categories/due-diligence.md) so two people reading the same hundred contracts produce one defensible count.

## If you are analyzing financials

You have a model to build and a comparable set to justify.

**Public comparables.** [edgartools](../categories/investment-analysis.md) for filings as structured data, [yfinance](../categories/investment-analysis.md) for prices and fundamentals, [OpenBB](../categories/investment-analysis.md) to pull it together, [Finance Toolkit](../categories/investment-analysis.md) for the ratios computed consistently.

**Private-company financials.** [Finance Toolkit](../categories/investment-analysis.md) again for normalising what a company sends you, [Marimo](../categories/knowledge-management.md) so the model is reproducible rather than a notebook with hidden state, and [Grist](../categories/lp-management.md) when the model needs to behave like a database.

**The instrument question.** [QuantLib](../categories/investment-analysis.md) or [FinancePy](../categories/investment-analysis.md) when a SAFE, a convertible, or an option pool means the headline valuation is not the real price.

**Cap tables and exits.** [Captable](../categories/cap-tables.md), [Open Cap Format](../categories/standards.md) to check a founder's model, and the [cap-table worksheet](../categories/cap-tables.md) for dilution. Read the coverage note on that page before you assume open source has solved this.

## If you are building internal VC tooling

You are the one person at the fund who writes code, and you need to ship something people use before anyone asks why the fund pays for software.

**Decide the plumbing once.** [Postgres with pgvector](../categories/knowledge-management.md) covers structured data, relationships, and embeddings in one system. Add a dedicated vector store or graph database only when you have outgrown it, not before. [Datasette](../categories/portfolio-management.md) or [Metabase](../categories/portfolio-management.md) on top, and most questions are answerable without you.

**Put a face on it fast.** [Streamlit](../categories/portfolio-management.md) for anything an analyst runs, [Appsmith](../categories/automation.md) when the person who understands the process should build the screen.

**Automate the boring parts.** [n8n](../categories/automation.md) for glue, [Airflow](../categories/automation.md) or [Prefect](../categories/automation.md) when jobs must run in order and tell someone when they fail, [dbt](../categories/automation.md) so the reporting tables are tested rather than trusted.

**For the agent-shaped work.** [LangGraph](../categories/ai-agents.md) if a workflow needs explicit steps and a human approval gate. [browser-use](../categories/ai-agents.md) for the parts with no API. [MCP servers](../categories/ai-agents.md) to expose your systems to whatever assistant the team uses.

**Then write it down.** [Outline](../categories/knowledge-management.md) or a README in the repository. Internal tooling that only its author understands becomes legacy the week that person is busy.

---

## The pattern across all five

The tools that matter are the ones that make evidence checkable: a citation, a saved page, a reproducible model, a transcript with timestamps. Everything else is speed, and speed without provenance is how a fund ends up confident and wrong.

Pair this with [VC_WORKFLOW.md](../VC_WORKFLOW.md) for the full process map, [build-your-own-vc-stack.md](build-your-own-vc-stack.md) for how the pieces connect, and [COMPARISON.md](../COMPARISON.md) when choosing between options.
