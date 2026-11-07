# Agent architecture Resources

## Knowledge

- [Anthropic: "Effective context engineering for AI agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Anthropic's own applied AI team on the context window, context rot, compaction and structured note-taking as memory. Use for: anything about what the model sees per call, what to keep versus persist, and just-in-time vs. upfront retrieval.
- [Anthropic: "Building effective agents"](https://www.anthropic.com/engineering/building-effective-agents)
  The foundational framing of an agent as a model augmented with retrieval, tools and memory, plus when a fixed workflow beats an agent. Use for: objective O3's memory/retrieval basics, and later for workflows-versus-agents and multi-agent objectives.
- [IBM: "What is retrieval-augmented generation (RAG)?"](https://www.ibm.com/think/topics/retrieval-augmented-generation)
  Plain, vendor-neutral walkthrough of chunking a document and searching it so only the relevant piece is loaded. Use for: designing `search_manuals`-style tools over the machine manuals.

## Wisdom (Communities)

- [r/LLMDevs](https://www.reddit.com/r/LLMDevs/)
  Developer-focused subreddit where memory, retrieval and RAG pipeline design are everyday threads. Use for: sanity-checking the makerspace assistant's memory and retrieval design before a team review.

## Gaps

- No source yet specifically on workflows vs. agents, or on when splitting work across multiple agents pays off — needed for later mission objectives on architecture choice and multi-agent systems.
