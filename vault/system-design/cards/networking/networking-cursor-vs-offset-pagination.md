---
id: networking-cursor-vs-offset-pagination
node: networking.api-styles
type: qa
---
## Q
Offset vs cursor pagination in an API — what breaks with `OFFSET` at depth and under concurrent writes?

## A
- **Cost**: `OFFSET n` scans and discards n rows — page 10,000 does O(n) work; deep pagination becomes a DB DoS.
- **Instability**: rows inserted/deleted between page fetches shift every offset → items duplicated or skipped mid-scroll.

**Cursor (keyset)**: return an opaque token encoding the last seen sort key; next page is `WHERE (created_at, id) < (cursor) ORDER BY created_at, id LIMIT k` — index seek, O(log n), stable under writes.

Price: no "jump to page N", and the sort key must be unique and immutable (hence the id tiebreaker).
