# AI Agents for VC

_Research that runs while you sleep._

Research agents, browser agents, multi-agent systems, orchestration, MCP servers, document agents, and financial agents.

**14 project(s)** &nbsp;·&nbsp; [← back to index](../README.md) &nbsp;·&nbsp; metadata updated 2026-09-14

> Every field below is read from the GitHub API at the date stamped above. The VC use case and tier are editorial judgement. See [METHODOLOGY.md](../METHODOLOGY.md).

---

### Dify

> Build and operate LLM applications without much code.

`langgenius/dify` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | AI Agents for VC |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | unverified (Other) |
| **Stars** | 155.7k |
| **Forks** | 24.6k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | partial (open core) |

**VC use case**

Where a fund's internal AI tools get assembled: a document assistant, a research workflow, a deal triage form, with a usable interface and logs. Useful when the person building it is an analyst rather than an engineer.

**Why it's interesting**

It covers the operational side that prototypes lack, including logs, evaluation, and deployments, in a visual interface.

**Good for**

- Internal tools
- Document RAG
- Research automation

**Limitations**

Licence is not a standard SPDX identifier, with a commercial cloud. Visual builders become limiting when logic gets complicated.

**Links:** [GitHub](https://github.com/langgenius/dify) &nbsp;·&nbsp; [Site](https://dify.ai)

---

### LangChain

> The most widely used framework for LLM applications.

`langchain-ai/langchain` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | AI Agents for VC |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 146.3k |
| **Forks** | 24.4k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | yes |

**VC use case**

Its value to a fund is mostly in the integrations catalogue: whatever system holds the data, someone has already written the connector. Useful when assembling internal tooling quickly.

**Why it's interesting**

Being the default means the ecosystem, examples, and accumulated answers are larger than for any alternative, which shortens debugging.

**Good for**

- Internal tools
- Integrations
- Prototyping

**Limitations**

Heavily criticised for abstraction overhead and frequent breaking changes. For a focused pipeline, the smaller frameworks are usually easier to maintain.

**Links:** [GitHub](https://github.com/langchain-ai/langchain) &nbsp;·&nbsp; [Site](https://docs.langchain.com/langchain/)

---

### browser-use

> Let a model drive a real browser.

`browser-use/browser-use` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | AI Agents for VC |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 114.6k |
| **Forks** | 12.6k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-13) |
| **Self-hostable** | yes |

**VC use case**

The tool that makes research agents actually work, because most of the useful public information sits behind JavaScript, logins, and search boxes rather than an API. A fund agent can check a competitor's pricing, a company register, or a portfolio dashboard the same way a person would.

**Why it's interesting**

It converts pages into a structure a model can act on, and it inspects the page to decide what to click rather than replaying recorded steps. That resilience is what makes unattended runs possible.

**Good for**

- Research automation
- Data collection
- Internal agents

**Limitations**

Still fails on complex flows, and unaided multi-step browsing burns tokens quickly. Anything involving a logged-in account needs care about terms and about credentials.

**Links:** [GitHub](https://github.com/browser-use/browser-use) &nbsp;·&nbsp; [Site](https://browser-use.com)

---

### Awesome MCP Servers

> The catalogue of MCP servers and connectors.

`punkpeye/awesome-mcp-servers` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ◇ **VC-adaptable** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | AI Agents for VC |
| **VC relevance** | VC-adaptable — a general tool a fund adopts directly for a specific venture task. |
| **License** | MIT |
| **Stars** | 95k |
| **Forks** | 16.1k |
| **Language** | unknown |
| **Status** | Active (last push 2026-09-13) |
| **Self-hostable** | yes |

**VC use case**

When a fund needs an agent to reach a system, the connector probably already exists. This is the index to check before writing one, covering everything from databases and filings to productivity tools.

**Why it's interesting**

It is the community's map of a fast-moving protocol, which is more current than any vendor list.

**Good for**

- Tool discovery
- Agent tooling
- Integrations

**Limitations**

Quality varies wildly between entries: some are weekend projects, some are maintained. Check the repository before depending on one.

**Links:** [GitHub](https://github.com/punkpeye/awesome-mcp-servers) &nbsp;·&nbsp; [Site](https://glama.ai/mcp/servers)

---

### MCP Servers

> Reference implementations of the Model Context Protocol.

`modelcontextprotocol/servers` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | AI Agents for VC |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | unverified (Other) |
| **Stars** | 90.3k |
| **Forks** | 11.6k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-03) |
| **Self-hostable** | yes |

**VC use case**

MCP is how an assistant gets access to real systems, and this is where the working patterns live: files, databases, git, search, and the plumbing for connecting them. For a fund building internal tooling it is the starting point rather than a blank page.

**Why it's interesting**

The protocol is now widely adopted, so a connector written once works across many clients. Reading the reference servers is the fastest way to understand what an agent integration should look like.

**Good for**

- Agent tooling
- Internal integrations
- Data access

**Limitations**

Reference implementations, not supported products: expect to harden anything you depend on. Access control for what an agent may touch is your problem.

**Links:** [GitHub](https://github.com/modelcontextprotocol/servers) &nbsp;·&nbsp; [Site](https://modelcontextprotocol.io)

---

### OpenHands

> An agent that writes and runs code to finish tasks.

`OpenHands/OpenHands` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | AI Agents for VC |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 87.8k |
| **Forks** | 11.5k |
| **Language** | TypeScript |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | yes |

**VC use case**

Relevant in two directions: a platform team can use it to build internal tooling faster, and a technical diligence reviewer can use it to inspect a target's repository and answer questions about its architecture.

**Why it's interesting**

It works in a sandboxed environment with a real terminal and editor, so it can verify its own work rather than only producing code that looks right.

**Good for**

- Technical due diligence
- Internal tooling
- Code review

**Limitations**

Runs code, which means it needs a real sandbox and supervision. Token cost on anything substantial is significant.

**Links:** [GitHub](https://github.com/OpenHands/OpenHands) &nbsp;·&nbsp; [Site](https://openhands.dev)

---

### AutoGen

> Multiple agents that talk to each other.

`microsoft/autogen` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | AI Agents for VC |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | CC-BY-4.0 |
| **Stars** | 61k |
| **Forks** | 9.2k |
| **Language** | Python |
| **Status** | Active (last push 2026-04-15) |
| **Self-hostable** | yes |

**VC use case**

Useful where a task benefits from separate perspectives: one agent argues the bull case, another the bear case, a third checks the facts. Also the pattern for splitting work by role, which maps onto how a diligence team divides a deal.

**Why it's interesting**

It comes from Microsoft Research with the conversation model documented, and the multi-agent pattern is the interesting part rather than the orchestration plumbing.

**Good for**

- Agent architecture
- Research automation
- Internal tooling

**Limitations**

Multi-agent systems multiply cost and failure modes, and the conversation pattern can look impressive while producing less than one well-specified agent.

**Links:** [GitHub](https://github.com/microsoft/autogen) &nbsp;·&nbsp; [Site](https://microsoft.github.io/autogen/)

---

### CrewAI

> Define a team of agents with roles and tasks.

`crewAIInc/crewAI` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | AI Agents for VC |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 58.5k |
| **Forks** | 8.4k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | yes |

**VC use case**

The most readable way to describe a multi-step research process: name the roles, give each a task, and let it run. Useful for prototyping an internal workflow before committing to heavier engineering.

**Why it's interesting**

The role-and-task vocabulary maps onto how people describe work, which lowers the barrier for someone who is not primarily an engineer to specify a tool.

**Good for**

- Prototyping
- Research automation
- Internal tooling

**Limitations**

Less control over exactly what happens than a graph-based approach, which matters when the output feeds a decision. Abstraction gets leaky on complex tasks.

**Links:** [GitHub](https://github.com/crewAIInc/crewAI) &nbsp;·&nbsp; [Site](https://crewai.com)

---

### LlamaIndex

> Connect models to your own data.

`run-llama/llama_index` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | AI Agents for VC |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 52.2k |
| **Forks** | 8.1k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

The most common foundation for a fund's document assistant: load a data room, build an index, and query it with citations. Its connector catalogue covers the sources diligence material actually arrives in.

**Why it's interesting**

It solves the ingestion and retrieval problem that sits between a document set and a usable assistant, and it is the most used option in this space.

**Good for**

- Document RAG
- Data-room search
- Internal tools

**Limitations**

The library is large and its abstractions shift between versions, so pin versions. Retrieval quality is still your responsibility.

**Links:** [GitHub](https://github.com/run-llama/llama_index) &nbsp;·&nbsp; [Site](https://developers.llamaindex.ai)

---

### LangGraph

> Agents as explicit graphs with state.

`langchain-ai/langgraph` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | AI Agents for VC |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 41.6k |
| **Forks** | 7k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-13) |
| **Self-hostable** | yes |

**VC use case**

The right shape for a diligence workflow, where steps depend on what earlier steps found and a human needs to approve before the next stage. You can model that as a graph with checkpoints, which also means a run can be paused and resumed.

**Why it's interesting**

It makes control flow explicit rather than hoping a model sequences steps correctly, including cycles, retries, and human-in-the-loop pauses. That is what makes an agent auditable enough to use on money.

**Good for**

- Diligence workflows
- Internal agents
- Agent orchestration

**Limitations**

A framework to learn, and its abstractions move quickly between versions. Overkill for a single-prompt task.

**Links:** [GitHub](https://github.com/langchain-ai/langgraph) &nbsp;·&nbsp; [Site](https://docs.langchain.com/oss/python/langgraph/)

---

### DSPy

> Program model pipelines instead of writing prompts.

`stanfordnlp/dspy` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | AI Agents for VC |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 38k |
| **Forks** | 3.3k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-11) |
| **Self-hostable** | yes |

**VC use case**

Prompt engineering does not survive a model upgrade, and a fund's internal tools have to last years. DSPy compiles declarative modules against examples, so the pipeline can be recompiled for a new model instead of rewritten.

**Why it's interesting**

It treats prompts as a compilation target rather than an artefact to maintain by hand, which is the correct answer to prompt fragility.

**Good for**

- Internal tooling
- Prompt maintenance
- Research automation

**Limitations**

Needs a set of examples to optimise against, which is real work up front. Concepts take time to absorb.

**Links:** [GitHub](https://github.com/stanfordnlp/dspy) &nbsp;·&nbsp; [Site](https://dspy.ai)

---

### OpenAI Agents SDK

> A small framework for agents, tools, and handoffs.

`openai/openai-agents-python` &nbsp;·&nbsp; 🔥 **Recommended** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | AI Agents for VC |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | MIT |
| **Stars** | 29.4k |
| **Forks** | 4.7k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | yes |

**VC use case**

The lowest-ceremony way to build a working agent with tool calls and handoffs. Good for a fund that wants to test whether an automated research step is worth building out before investing in a bigger framework.

**Why it's interesting**

Deliberately minimal, with a handful of primitives rather than a large abstraction layer, so the code stays readable to whoever inherits it.

**Good for**

- Prototyping
- Internal agents
- Research automation

**Limitations**

Closest to one provider's ecosystem, though it supports others. Minimal means you build the surrounding pieces yourself.

**Links:** [GitHub](https://github.com/openai/openai-agents-python) &nbsp;·&nbsp; [Site](https://openai.github.io/openai-agents-python/)

---

### Heurist Agent Framework

> A multi-interface agent framework with several front ends.

`heurist-network/heurist-agent-framework` &nbsp;·&nbsp; 🧪 **Experimental** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _framework_

| | |
|---|---|
| **Category** | AI Agents for VC |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | unverified (Other) |
| **Stars** | 826 |
| **Forks** | 90 |
| **Language** | Python |
| **Status** | Active (last push 2026-09-02) |
| **Self-hostable** | yes |

**VC use case**

Shows how to expose the same agent through different interfaces: API, chat, and a web app. Useful when internal tooling needs to serve both an analyst working in a notebook and a partner who wants a chat window.

**Why it's interesting**

The multi-interface approach is the practical detail most frameworks skip, and it is often what stops an internal tool from being adopted.

**Good for**

- Internal tools
- Agent architecture
- Research

**Limitations**

Broad surface area with a small team, so individual components vary in maturity.

**Links:** [GitHub](https://github.com/heurist-network/heurist-agent-framework) &nbsp;·&nbsp; [Site](https://agent.heurist.ai/)

---

### AutoGPT

> The project that made autonomous agents mainstream.

`Significant-Gravitas/AutoGPT` &nbsp;·&nbsp; 📚 **Research** &nbsp;·&nbsp; ▫ **Infrastructure** &nbsp;·&nbsp; _software_

| | |
|---|---|
| **Category** | AI Agents for VC |
| **VC relevance** | Infrastructure — a building block you construct venture tooling with, not something an analyst uses standalone. |
| **License** | unverified (Other) |
| **Stars** | 187.3k |
| **Forks** | 46k |
| **Language** | Python |
| **Status** | Active (last push 2026-09-14) |
| **Self-hostable** | yes |

**VC use case**

Historical context more than a tool: this is what made the autonomous agent category legible to investors, and understanding its failure modes explains the design of everything built since.

**Why it's interesting**

Reading why it was exciting and why it did not work is the fastest way to develop judgement about agent claims in a pitch.

**Good for**

- Understanding the category
- Investment thesis work
- Research

**Limitations**

Overwhelmed by later frameworks for actual work, and the licence is not a standard SPDX identifier. Use it for context, not production.

**Links:** [GitHub](https://github.com/Significant-Gravitas/AutoGPT) &nbsp;·&nbsp; [Site](https://agpt.co)

---
