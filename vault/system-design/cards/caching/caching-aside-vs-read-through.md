---
id: caching-aside-vs-read-through
node: caching.strategies
type: qa
---
## Q
Cache-aside and read-through both populate the cache on a miss. What actually differs, and when does that difference matter?

## A
**Who owns the load logic.** In cache-aside the *application* checks the cache, fetches from the DB on miss, and writes the cache; in read-through the *cache layer* fetches from the store itself.

- Cache-aside: works with any dumb cache (Redis/Memcached), app can cache arbitrary computed shapes, but every service duplicates the load logic.
- Read-through: centralizes loading (e.g., a caching library or proxy with a loader), enables built-in coalescing of concurrent misses, but ties the cached shape to the store's data model.
