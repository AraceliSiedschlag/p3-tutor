# Agent architecture Resources

## Knowledge

- [Anthropic: "Effective context engineering for AI agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Explains context rot (recall degrades as the context window fills), and the just-in-time retrieval vs. upfront-loading tradeoff. Use for: why "more context" is not free, retrieval design.
- [Anthropic Platform Docs: "Context windows"](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Defines the context window precisely: everything the model processes for one call, and that history is resent each step, not retained by the model. Use for: the mechanics of what's "in context" at a given moment, token cost.
- [Anthropic Platform Docs: "Memory tool"](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  How an agent writes and reads its own persistent notes outside the context window. Use for: notes vs. retrieval, cross-session persistence.
- [LangChain: "Context Engineering for Agents"](https://www.langchain.com/blog/context-engineering-for-agents)
  A practitioner framing of the same context-window and memory tradeoffs. Use for: a second worked framing of context engineering, cross-checking Anthropic's.
- [Helix DB: "LLM Memory Architecture: How Agents Remember Across Sessions"](https://www.helix-db.com/content/guides/llm-memory-architecture-how-agents-remember-across-sessions)
  Explains that nothing persists between sessions unless written to external storage and reloaded. Use for: session-to-session memory design.

## Wisdom (Communities)

- r/LocalLLaMA and agent-framework Discords (e.g. LangChain's)
  Active communities where context/memory design patterns for real agents get discussed and critiqued. Use for: checking a context or memory design against what practitioners have hit in practice. Optional for Riley; no opt-out noted yet in NOTES.md.
