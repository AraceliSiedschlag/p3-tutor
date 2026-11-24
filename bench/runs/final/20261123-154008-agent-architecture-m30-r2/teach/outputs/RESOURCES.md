# Agent Architecture Resources

## Knowledge

- [Context windows — Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Official definition of the context window: what counts as input (system prompt, conversation, tool definitions and results) and output, the fixed token size shared between them, what carries forward turn to turn within a session, and context rot. Use for: anything about what the model sees on a given call, and about context limits.
- [Memory tool — Claude Platform Docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  How an agent persists information between sessions by writing to storage outside the context window and reading it back later. Use for: notes-as-memory, what survives (or does not) between sessions.
- [What is Retrieval Augmented Generation (RAG)? — IBM](https://www.ibm.com/think/topics/retrieval-augmented-generation)
  Clear overview of retrieval as a technique for pulling only the relevant slice of a large external source into the prompt. Use for: what retrieval is and how it differs from loading a whole document.
- [Understanding Retrieval Augmented Generation — AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/what-is-rag.html)
  Explains why retrieval is used instead of retraining a model on new or large knowledge sources. Use for: the case for retrieval, keeping answers current and accurate from material larger than the context window.

## Wisdom (Communities)

_None yet._

## Gaps

- No community resource identified yet for agent architecture design review practice; revisit once the mission's design-review phase is closer.
