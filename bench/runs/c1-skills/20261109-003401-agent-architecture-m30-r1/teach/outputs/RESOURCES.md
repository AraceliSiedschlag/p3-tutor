# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Defines the context window, explains "context rot" (accuracy drops as the window fills), how context grows within an agent's steps, and the two patterns for memory that outlive a single context: structured notes written outside the window, and just-in-time retrieval with lightweight pointers (file paths, queries) instead of pre-loading everything. Use for: anything about what an agent keeps between steps, between sessions, and how retrieval works.
- [Article: "What Is Context Engineering?" (IBM Think)](https://www.ibm.com/think/topics/context-engineering)
  Plain-language framing of the context window as "the model's short-term memory," plus a six-step breakdown of context management (selection, structuring, compression, sequencing, tool/memory integration). Use for: a simpler second pass on the same ideas, or when a figure needs a clean definition to caption.

## Wisdom (Communities)

- [r/AI_Agents](https://www.reddit.com/r/AI_Agents/)
  Active practitioner subreddit where builders trade real trade-offs on context and memory design (one thread: "most AI agent teams are secretly just context engineering teams"). Use for: sanity-checking a memory/retrieval design for the makerspace assistant against what other small teams actually shipped.

## Gaps

- No source yet on concrete per-token pricing or prompt-caching mechanics, which the mission's budget constraint will eventually need; deferred for a lesson on cost specifically, so this one stays conceptual.
