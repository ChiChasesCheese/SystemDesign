---
id: caching-write-through-vs-behind
node: caching.strategies
type: qa
---
## Q
Write-through vs write-behind (write-back): what does each cost you, and what breaks in write-behind if the cache node dies?

## A
- **Write-through**: write goes to cache *and* store synchronously. Cost: every write pays store latency; cache is never fresher than needed. Safe but slow.
- **Write-behind**: write acks after hitting the cache; the store is updated asynchronously in batches. Cost: **acknowledged writes are lost** if the cache node crashes before flush, and the store lags so other readers see stale data.

Write-behind fits high-write, loss-tolerant data (counters, view stats) — never money or anything the store must durably own at ack time.
