# Agent architecture resources

## Knowledge

- [Anthropic: "Effective context engineering for AI agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Anthropic's own engineering writeup on managing a context window as a limited resource: context rot, just-in-time retrieval, sub-agents, and structured note-taking as memory outside the window. Use for: anything to do with O3 (context and memory) and later, deciding what to delegate to a sub-agent.
- [Claude Docs: "Context windows"](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  The precise, vendor-specific definition of what counts toward a context window (system prompt, messages, tool results, tool definitions, output), sizes by model, and overflow behavior. Use for: exact mechanics of what one model call reads, and why it costs what it costs.
- [AWS Prescriptive Guidance: "Understanding Retrieval Augmented Generation"](https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/what-is-rag.html)
  Vendor-neutral walkthrough of the RAG pattern: embeddings, a vector database, a retriever, an orchestrator. Use for: naming the pieces of a retrieval design at a review, independent of which model or vendor is used.

## Wisdom (Communities)

- [Claude developer community](https://claude.com/community)
  Official community with channels on agents, tool use, and production integrations, where people building real agents compare context and memory designs. Use for: sanity-checking the makerspace assistant's design before the design review.

## Gaps

- No source yet specifically on sizing a model budget for a small, sponsor-funded project (cost-per-request tradeoffs at prototype scale rather than production scale). Worth finding when cost estimation for the design review comes up.
