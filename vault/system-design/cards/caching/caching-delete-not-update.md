---
id: caching-delete-not-update
node: caching.invalidation
type: qa
---
## Q
On a DB write, why is *deleting* the cache key generally safer than *updating* it with the new value?

## A
Concurrent updates race: two writers can update the DB in one order and the cache in the opposite order, leaving the cache holding the **older value indefinitely** (until TTL, if any).

Delete-on-write makes the next reader repopulate from the DB, so the worst case is one extra miss instead of a persistent wrong value. Remaining race (read miss loads old value while a write lands) is narrow and bounded by TTL — which is why you keep a TTL even with explicit invalidation.
