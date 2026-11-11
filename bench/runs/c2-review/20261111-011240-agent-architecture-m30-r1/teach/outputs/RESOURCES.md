# Agent Architecture Resources

## Knowledge

- [Effective context engineering for AI agents (Anthropic)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Anthropic's own engineering writeup on treating context as a finite "attention budget" that degrades as it fills (context rot), and the two main fixes: just-in-time retrieval (loading only what's needed, when it's needed) and structured note-taking (writing small persistent notes outside the context window). Use for: O3, and any future lesson on compaction, sub-agents, or long-running agent design.
- [Context windows (Claude Platform Docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  The precise mechanics: a context window is all the text a model can reference in one request, measured in tokens; everything in the request (system prompt, every message, tool results, tool definitions) counts toward it; history is resent in full on every turn. Use for: the token/cost arithmetic behind O3, and anything about per-call pricing.
- [Memory tool (Claude Platform Docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  A concrete, working example of "notes as memory": a file-based store the model reads before starting work and writes to as it learns things, so state survives across separate sessions without keeping the whole transcript in context. Use for: O3's cross-session memory, and later, a real implementation pattern for the makerspace assistant's student-training records.

## Wisdom (Communities)

- [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/)
  Active subreddit with daily threads on agent setups, context/cost management, and real build problems. Use for: sanity-checking an architecture decision (e.g. "should this be a saved note or a retrieval call?") against what other builders have hit.
