---
id: ai-chunking-failure-modes
node: ai.rag
type: qa
---
## Q
Documents must be split into chunks before embedding. What breaks with chunks that are too big, too small, or split naively — and what does good chunking do instead?

## A
- **Too big**: one embedding averages many topics — the vector matches nothing sharply, and each hit burns context budget on mostly-irrelevant text.
- **Too small**: chunk lacks its own context ("it increased by 40%" — what did?); the answer gets **severed across chunk boundaries** so no single retrieved chunk contains it.
- **Naive fixed-size splits**: cut mid-sentence, mid-table, mid-code-block — the classic silent RAG quality killer.

Good practice: split on **document structure** (headings, paragraphs), add **overlap** between neighbors, and prepend context (title/section path, "contextual chunking") so each chunk is self-describing. Chunking is set at **index time** — changing it means re-processing the corpus.
