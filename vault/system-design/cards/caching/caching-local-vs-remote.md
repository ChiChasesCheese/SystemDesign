---
id: caching-local-vs-remote
node: caching.placement
type: qa
---
## Q
In-process (local) cache vs shared remote cache (Redis): what do you gain and lose with each, and what pattern combines them?

## A
- **In-process**: ~100ns–1µs access, no network hop — but each instance holds its own copy (memory × N, cold on every deploy) and **cross-instance invalidation is hard**, so nodes can disagree.
- **Remote (Redis/Memcached)**: one consistent copy, survives app restarts, shared hit rate — but every read pays ~0.5–1ms network RTT and the cache is an infra dependency to size and fail over.

Combine as a **two-tier cache**: tiny local L1 with short TTL for the hottest keys, Redis as L2, often with pub/sub invalidation broadcasts to local tiers.
