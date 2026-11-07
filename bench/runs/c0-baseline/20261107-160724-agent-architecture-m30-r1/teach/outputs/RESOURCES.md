# Agent architecture Resources

## Knowledge

- [Anthropic: "Effective context engineering for AI agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Anthropic's own engineering guidance on context windows, context rot, and agentic memory (note-taking files persisted outside the context window). Use for: anything about what to keep in context, what to retrieve, and what to save as memory.
- [Claude Platform Docs: "Context windows"](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Official reference on exactly what counts toward a context window (system prompt, messages, tool results, tool definitions, output) and how it accumulates turn by turn. Use for: tracing what a specific API call actually sends and pays for.
- [Claude Platform Docs: Glossary (tokens)](https://platform.claude.com/docs/en/about-claude/glossary)
  Official definition of a token and the rough characters-per-token ratio. Use for: estimating cost or size before writing code that calls the API.

## Wisdom (Communities)

- [claude.com/community](https://claude.com/community)
  Anthropic's official hub, linking to the Claude Discord and r/ClaudeAI, plus a Campus Program for student-run AI projects. Use for: sanity-checking an architecture decision (what to keep in context vs. retrieve vs. save) against people who have shipped agents.
