---
id: storage-index-leftmost-prefix
node: storage.relational.indexing
type: qa
---
## Q
You have a composite B-tree index on `(tenant_id, created_at)`. Which of these can use it efficiently: (a) `WHERE tenant_id = ?`, (b) `WHERE created_at > ?`, (c) `WHERE tenant_id = ? AND created_at > ?` — and why?

## A
(a) and (c). A composite index is sorted by the **leftmost column first**; entries for one `tenant_id` are contiguous, and within them sorted by `created_at`.

(b) alone can't seek — matching rows are scattered across every tenant's section, forcing a full index/table scan.

Ordering rule: put **equality columns first, then the range column**; a range on an earlier column stops the index being useful for later columns.
