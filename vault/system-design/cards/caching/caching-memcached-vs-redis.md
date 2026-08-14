---
id: caching-memcached-vs-redis
node: caching.strategies
type: qa
---
## Q
When is Memcached the right pick over Redis, and what does Redis add that decides most other cases?

## A
**Memcached**: multithreaded (one instance saturates all cores), simple slab-allocated LRU byte cache, very flat performance — right when the job is purely a look-aside blob cache at huge scale (Facebook's use).

**Redis/Valkey** adds: data structures (hashes, sorted sets, lists), atomic ops + Lua, per-key TTL with richer eviction, replication + failover + optional persistence, pub/sub and streams — right when the "cache" also does ranking, counters, sessions, locks, or queues. Being single-threaded per core, it scales by sharding instead.

2026 default: Redis/Valkey, unless the workload is strictly bytes-in/bytes-out at extreme throughput.
