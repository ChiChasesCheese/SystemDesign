---
id: storage-inverted-index
node: storage.search
type: qa
---
## Q
What is an inverted index, and why can't a B-tree index on a text column do the same job?

## A
A map from **term → posting list of documents containing it** (plus positions/frequencies), built after analysis (tokenizing, lowercasing, stemming). A query intersects/unions the posting lists of its terms, then ranks by relevance (TF-IDF/BM25).

A B-tree indexes the **whole column value** in sort order: it can answer prefix matches (`LIKE 'foo%'`) but not "documents containing this word anywhere", relevance ranking, or fuzzy/multi-term queries — those need per-term postings.
