# Agent architecture Resources

## Knowledge

- [Article: "Building Effective Agents" (Anthropic)](https://www.anthropic.com/research/building-effective-agents)
  Draws the architectural line this workspace uses for O4: workflows are "systems where LLMs and tools are orchestrated through predefined code paths," agents are "systems where LLMs dynamically direct their own processes and tool usage." Use for: workflows vs. agents, when to prefer a fixed workflow, and later the specific workflow patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer).

## Gaps

- No source yet specifically on context and memory for long manuals (retrieval), which is next in the mission after O4.
