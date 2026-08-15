---
id: ai-grounding-citations
node: ai.rag
type: qa
---
## Q
What does "grounding" mean in a RAG system, and what do enforced citations buy you beyond user trust?

## A
**Grounding**: the answer must be supported by the retrieved passages — the prompt instructs the model to answer *only* from provided context and to **abstain** when the context doesn't contain the answer (the abstain path is what kills hallucinated answers on retrieval misses).

Citations (chunk/source IDs attached to claims) buy:
- **Verifiability**: users and reviewers can check the source.
- **Automated eval**: a groundedness checker can verify each claim is entailed by its cited chunk, and gate deploys on it.
- **Debuggability**: a wrong answer becomes attributable — bad chunk retrieved vs model ignoring a good chunk.

Caveat: models can cite plausibly but wrongly, so citation presence is not proof — verification is a separate check.
