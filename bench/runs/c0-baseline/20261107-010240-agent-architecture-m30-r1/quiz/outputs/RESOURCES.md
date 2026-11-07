# Agent architecture Resources

## Knowledge

- [Article: "Building effective agents" (Anthropic)](https://www.anthropic.com/engineering/building-effective-agents)
  Primary source for workflows vs. agents: workflows run LLMs and tools through code paths the programmer fixed in advance; agents let the model direct its own steps and tool use at runtime. States the decision rule plainly: use a workflow when a task decomposes into fixed, predictable subtasks; use an agent only when the number and order of steps can't be known ahead of time. Use for: objective O4 (workflows vs. agents, and when a fixed workflow is the better choice).

## Gaps

- No source yet for memory, retrieval over long manuals, or multi-agent systems (objectives O3 and O5). Find one before teaching or quizzing those.
