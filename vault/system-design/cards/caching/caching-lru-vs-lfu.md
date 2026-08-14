---
id: caching-lru-vs-lfu
node: caching.invalidation
type: qa
---
## Q
Your cache hit rate collapses whenever a nightly batch job scans the full table. Which eviction policy is failing, and what do you switch to?

## A
**LRU** — a one-time scan touches every key once and evicts the genuinely hot working set (cache pollution / scan thrash).

Switch to a frequency-aware policy: **LFU** or modern hybrids like **TinyLFU/W-TinyLFU** (Caffeine's default) or Redis's `allkeys-lfu`, which require repeated access before a key can displace established hot entries. LRU remains fine when recency really does predict re-use, e.g. session-like access patterns.
