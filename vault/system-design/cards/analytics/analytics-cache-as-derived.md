---
id: analytics-cache-as-derived
node: analytics.derived
type: qa
---
## Q
Reframe cache invalidation as a derived-data problem. What does the reframing buy you over app-managed invalidation?

## A
A cache entry is a **materialized view of a query**; "invalidation" is just view maintenance. Instead of application code remembering to delete keys on every write path (dual-write: miss one path or crash mid-way and the cache lies indefinitely), subscribe a maintainer to the database's **change log (CDC)** and update/evict affected keys from there.

Buys you:
- **Completeness**: every committed write reaches the cache exactly once, in log order — no forgotten code path.
- **Rebuildability**: cold cache or bad entries? Replay/backfill like any derived view.

TTLs remain as the backstop bounding staleness when the pipeline breaks, not the primary mechanism.
