---
id: storage-partial-expression-index
node: storage.relational.indexing
type: qa
---
## Q
A 500M-row `jobs` table has 2k rows in `status='pending'` that a worker polls constantly. What index do you build, and what related index type fixes `WHERE lower(email) = ?`?

## A
A **partial index**: `CREATE INDEX ON jobs (run_at) WHERE status = 'pending'`.

- Size tracks the **2k live rows**, not 500M — it stays fully cached, and entries are removed as jobs complete, so the hot queue index never grows with history.
- Cheaper writes too: rows that don't satisfy the predicate are never indexed at all.
- The planner only uses it when it can prove the query's predicate **implies** the index predicate, so the constant must match (`status = 'pending'`, not a bound parameter in some engines).

For `lower(email)`, build an **expression index** — `CREATE INDEX ON users (lower(email))`. The index stores the computed value, so the query's expression must match the indexed one *textually*; that also makes it the standard way to enforce case-insensitive uniqueness.
