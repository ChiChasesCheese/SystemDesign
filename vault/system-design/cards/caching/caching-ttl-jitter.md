---
id: caching-ttl-jitter
node: caching.invalidation
type: cloze
---
When many keys are warmed at the same moment (deploy, cache flush, midnight job), identical TTLs make them all expire together and hammer the backend at once. The fix is {{c1::adding random jitter to each TTL (e.g. `ttl + rand(0, 10%·ttl)`)}} so expiries spread out; for a single hot key, use {{c2::a lock / single-flight recompute (one request rebuilds, others serve stale)}} to stop a stampede.
