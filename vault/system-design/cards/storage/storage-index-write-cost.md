---
id: storage-index-write-cost
node: storage.relational.indexing
type: qa
---
## Q
A table has 9 indexes "just in case." Quantify what each additional index costs the write path, and how you decide which ones to drop.

## A
- Every `INSERT`/`DELETE` becomes **1 + N structure updates** — each index takes a random-ish write into a different B-tree page, plus WAL bytes for each. Insert throughput on a wide-indexed table commonly lands at a fraction of the same table with one index.
- `UPDATE` is the sharp edge in Postgres: if any **indexed** column changes (or the page has no free space), the HOT optimization is lost and the new row version must be inserted into **every** index, not just the one you touched.
- Indexes also multiply **vacuum/maintenance** work, bloat, and cache pressure — they compete with the table for buffer pool.

Drop by evidence: `pg_stat_user_indexes.idx_scan = 0` over a full business cycle (watch replicas too), plus indexes made redundant by a leftmost prefix of a wider one. Drop with `CONCURRENTLY`, and keep unique/constraint-backing indexes regardless of scan count.
