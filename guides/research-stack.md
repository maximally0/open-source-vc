# The Research Stack

Building a defensible view of a market, with sources you can point at.

---

## The problem

Research in a fund usually means one analyst, a deadline, and a folder of browser tabs. The output is a document that reads well and cannot be audited: claims without sources, numbers without windows, and a conclusion that depends on whoever did the searching.

The open-source toolkit for this is now good enough to change the shape of the work. Not by writing the conclusion, which remains the analyst's job, but by making every claim traceable and every search reproducible.

## The three kinds of research question

They need different tools, and mixing them up is why research agents often disappoint.

| Question type | Example | What works |
|---|---|---|
| **Landscape** | Who is building in this space, and who funded them? | Collection plus structured storage |
| **Evidence** | Is this technical claim true? | Retrieval with citations over primary documents |
| **Judgement** | Is this market about to inflect? | Your own synthesis, supported by monitoring |

An agent is good at the first, useful for the second, and unreliable for the third. Being clear about which one you are asking saves a lot of time.

## Landscape: building the map

**Collect** from where the activity is visible:

- [Scrapy](../categories/osint.md) or [Crawlee](../categories/osint.md) for volume and JavaScript
- [Firecrawl](../categories/osint.md) when you want text rather than HTML
- The [YC API](../categories/company-discovery.md) for a cohort you can slice by sector
- [JobSpy](../categories/founder-discovery.md) for hiring, which shows where a market is growing

**Resolve** before you count. [dedupe](../categories/company-discovery.md), because a market map of eighty companies that is actually sixty is a market map you will mis-size.

**Store** somewhere queryable: [Postgres with pgvector](../categories/knowledge-management.md), or [NocoDB](../categories/deal-sourcing.md) if you would rather see a grid than write SQL. Publish it internally with [Datasette](../categories/portfolio-management.md) so anyone can ask their own questions.

**Then write it up** where it will be found next year: [Outline](../categories/knowledge-management.md) or [Docmost](../categories/knowledge-management.md), not a document on someone's laptop.

## Evidence: checking the claims

This is where open-source tooling has genuinely improved, and where citations stop being optional.

**Primary documents.** [paper-qa](../categories/due-diligence.md) answers questions from a set of papers with page-level citations. [Open US Law](../categories/legal.md) and [edgartools](../categories/investment-analysis.md) for regulatory and filing text. [OpenAlex](../categories/datasets.md) for publication records and citation impact.

**The open web.** [GPT Researcher](../categories/market-research.md) and [STORM](../categories/market-research.md) both keep source lists attached to claims. [browser-use](../categories/ai-agents.md) for sources with no API. [Firecrawl](../categories/osint.md) to get page content a model can actually read.

**Cross-document structure.** [GraphRAG](../categories/knowledge-management.md) when the question is relational: which companies share an investor, which founders came from the same place, where a supply chain concentrates. Flat similarity search cannot answer those, and it is worth knowing that before you conclude your tooling is broken.

**Your own corpus.** [RAGFlow](../categories/knowledge-management.md) or [LlamaIndex](../categories/ai-agents.md) over past memos and filings, so research compounds instead of being redone. [Khoj](../categories/market-research.md) if you want the same thing with less assembly.

## Judgement: forming the view

No tool does this part. What tools do is make sure the inputs were real.

The sequence that works:

1. **Collect the primary evidence first.** A landscape of company websites tells you what people claim. Filings, papers, patents, and job postings tell you what they do. Prefer the second.
2. **Write the counter-argument before the argument.** What would have to be true for this market to be a bad bet? Then go looking for that. Structured disagreement is where [AutoGen](../categories/ai-agents.md)'s bull-and-bear pattern comes from, and it works as a prompt even without agents.
3. **Record what you could not find.** A research document that says "we could not establish how many of these companies have revenue" is more useful than one that omits the gap, because it tells the next analyst where to start.
4. **Date everything.** A market view without dates is a market view that will be wrong and still quoted.

## Monitoring: keeping the map current

Research that is not maintained decays. The cheap version:

- [changedetection.io](../categories/deal-sourcing.md) for competitor pages that matter
- [TrendRadar](../categories/market-research.md) or [situation-monitor](../categories/market-research.md) for the macro backdrop
- [Dub](../categories/deal-sourcing.md) if the fund publishes anything, to know what it produced

The point is a weekly five-minute review, not a dashboard nobody opens. Set the alerts to something a person will act on and let the rest go.

## Recording sources properly

This is the least glamorous part and it is what makes research defensible.

- [Zotero](../categories/knowledge-management.md) for papers, reports, and filings, with metadata and citations
- [SingleFile](../categories/osint.md) for web pages, because pages change and "the site said X" is not a source
- [WhisperX](../categories/relationship-intelligence.md) for interviews and calls, with speaker labels
- [Logseq](../categories/knowledge-management.md) for the analyst's own linked notes, which over years becomes a private map of a market
- [Marimo](../categories/knowledge-management.md) for any analysis, so a number can be reproduced rather than trusted

A useful test: hand your research document to a colleague and ask them to find the source for any three claims. If they cannot, the research is not finished, however good it reads.

## What does not work

**Asking a model to research a market and trusting the output.** It will produce fluent, well-organised text about a market it has partially understood, with plausible citations that occasionally do not say what the text claims. Everything above exists to make that checkable.

**Benchmarking research agents on general tasks.** [DeepResearch Bench](../categories/market-research.md) is a good evaluation and its tasks are not venture tasks. A high score means the agent is competent at general research, not that it can size a market.

**Skipping the collection step.** An agent with no data sources will still write you something. It will be confident and it will be wrong, and it will look the same as the version built on real evidence.
