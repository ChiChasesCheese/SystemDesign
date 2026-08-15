---
id: storage-index-selectivity
node: storage.relational.indexing
type: qa
---
## Q
There is a B-tree index on the column, but `EXPLAIN` shows a sequential scan. Give the two distinct reasons a planner *chooses* not to use it, and the one that means it *cannot*.

## A
**Chooses not to (cost):**
- **Low selectivity** — the predicate matches a large fraction of rows. An index scan costs ~1 random heap I/O per matching row; a seq scan reads pages sequentially. Above roughly **5–10% of the table** the seq scan wins, so `WHERE status = 'active'` on a 90%-active table correctly ignores the index.
- **Bad or stale statistics** — the planner's row estimate is wrong (skewed values, no `ANALYZE` after a bulk load, correlated columns it assumes are independent). The plan is optimal *for the estimate*, not for reality.

**Cannot (non-sargable predicate):** the indexed column is wrapped or coerced — `WHERE lower(email) = ?`, `WHERE created_at::date = ?`, `LIKE '%foo'`, or an implicit type cast on the column side. The index is sorted on the raw column, so no seek range exists.
