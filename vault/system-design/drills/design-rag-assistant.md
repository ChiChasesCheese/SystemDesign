---
nodes: [ai.rag, ai.vector-search, ai.foundations, ai.evals, storage.search]
tags: [flagship, ai]
---
# Drill: Design a retrieval-augmented assistant

An assistant answering questions over 10 million internal documents, with
citations, for 50,000 employees. Permissions are per-document, the corpus
changes hourly, and a confident wrong answer is worse than no answer.

**Constraints to state and honor**
- Answer in under 3 seconds, with citations a reader can open and verify.
- A user must never see content from a document they cannot open — including through a summary.
- New and edited documents are searchable within an hour; deletions immediately.
- You will be asked, at review time, to prove the thing got better after your last change.

**Grading points**
- The two pipelines separated cleanly: offline ingestion/indexing and online retrieval/generation, each with its own failure modes ([[ai-rag-two-pipelines]]).
- RAG argued against the alternatives — fine-tuning and long context — on freshness, cost, and attribution ([[ai-rag-vs-finetune-vs-longcontext]], [[ai-context-window-budget]]).
- Chunking treated as a design decision with named failure modes, not a parameter copied from a tutorial ([[ai-chunking-failure-modes]], [[ai-embeddings-as-coordinates]]).
- Hybrid retrieval — lexical plus vector — with the query types each one rescues ([[ai-hybrid-retrieval]], [[storage-inverted-index]]).
- ANN index chosen with its recall/latency/memory trade explicit, and the build and update cost stated ([[ai-hnsw-vs-ivf]], [[ai-ann-tradeoff]], [[ai-index-maintenance]]).
- Permission filtering done inside retrieval, with the recall cost of post-filtering named as the reason ([[ai-filtered-vector-search]]).
- Freshness handled for edits and deletes, including tombstones in the index and the corpus-drift problem ([[ai-corpus-freshness]], [[storage-search-nrt-refresh]], [[storage-search-sync]]).
- Retrieve-then-rerank as the standard quality lever, with its latency cost budgeted ([[ai-retrieve-then-rerank]], [[ai-retrieval-eval]]).
- Grounding enforced structurally — citations tied to retrieved spans, refusal when retrieval is empty ([[ai-grounding-citations]], [[ai-guardrails-validation]]).
- Evaluation designed before launch: a fixed eval set with retrieval and answer metrics, plus tracing and prompt regression tests in CI ([[ai-eval-set-vs-ab]], [[ai-prompt-regression-testing]], [[ai-pipeline-tracing]], [[ai-llm-judge-biases]]).

**Attempt log**
- [ ] Attempt 1 (date, 45 min, self-graded notes):
