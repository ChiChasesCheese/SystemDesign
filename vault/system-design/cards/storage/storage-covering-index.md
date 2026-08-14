---
id: storage-covering-index
node: storage.relational
type: qa
---
## Q
What makes an index "covering" for a query, why is it dramatically faster, and what's the cost of covering everything?

## A
The index contains **every column the query needs** (key columns + `INCLUDE`d payload), so the engine answers from the index alone — an **index-only scan** — skipping the per-row hop to the heap/table (a random I/O per row in Postgres, unless the visibility map lets it skip the check).

For a 1000-row range that hop is often 90%+ of the cost; covering turns it into one contiguous index range read.

Cost: every extra indexed/included column makes **every write** update more index bytes, bloats index size, and slows vacuum — indexes are derived data you pay for on each mutation. Cover your hottest queries, not all of them.
