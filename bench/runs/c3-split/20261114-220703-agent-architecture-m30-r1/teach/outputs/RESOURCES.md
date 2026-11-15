# Agent architecture — Resources

## Knowledge

- [Anthropic: "Effective context engineering for AI agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Official engineering guidance on the context window, the agent loop, compaction/context editing, and structured note-taking as memory. Use for: O3, context and memory, and anything later on compaction.
- [Redis: "LLM context windows: what they are & how they work"](https://redis.io/blog/llm-context-windows/)
  Explains tokens, context-window sizing, cost, and the "lost-in-the-middle" accuracy effect. Use for: why bigger windows don't remove the need for retrieval.
- [addyosmani/agent-engineer, "05-memory-and-context" README](https://github.com/addyosmani/agent-engineer/blob/main/05-memory-and-context/README.md)
  Clear context-window-vs-memory distinction; within-session vs. cross-session storage; retrieval and summarization as memory strategies. Use for: O3's core "what's kept between steps vs. sessions" distinction.
- [Anthropic: "The components of agent memory"](https://www.anthropic.com/research/components-of-agent-memory)
  Background on how agent memory is structured. Use for: deeper follow-up on memory architecture.
- [Claude Platform Docs: "Memory tool"](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  A concrete, shipped example of notes-as-memory and just-in-time retrieval. Use for: a real implementation example when Riley wants to see code.

## Wisdom (Communities)

- Gap: no community identified yet for agent architecture design review practice. Riley's cohort/design team itself may serve this role; revisit if the mission calls for outside peer review.
