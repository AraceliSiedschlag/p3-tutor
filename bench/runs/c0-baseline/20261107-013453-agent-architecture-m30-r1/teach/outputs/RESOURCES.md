# Agent Architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Primary source for O3. Defines context as the tokens given to the model each call, explains context rot, and covers structured note-taking (memory outside the context window) and just-in-time retrieval. Use for: anything about memory, notes, or retrieval design.
- [Docs: "Context windows" (Claude Platform Docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Technical reference: what counts toward the window, token accumulation across turns, context window sizes, and what happens on overflow. Use for: concrete numbers and token/cost mechanics.
- [Docs: "Memory tool" (Claude Platform Docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  A concrete, file-based implementation of cross-session notes. Use for: a worked pattern if the team wants to see memory built rather than just described.

## Wisdom (Communities)

- [GenAI_Agents (GitHub)](https://github.com/PaperArmada/GenAI_Agents)
  Open collection of agent build-outs, beginner to advanced, with an associated community for questions. Use for: seeing how other small teams split memory from retrieval in real code, and sanity-checking the makerspace assistant's design.

## Gaps

- No source yet specifically on retrieval-augmented generation (RAG) implementation mechanics (chunking, embeddings, vector search) for when the team gets past "retrieve the relevant manual page" and into building search_manuals for real.
