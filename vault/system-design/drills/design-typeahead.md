---
nodes: [storage.search, caching.placement, networking.cdn, distributed.partitioning.indexes, foundations.numbers]
tags: [classic, latency]
---
# Drill: Design search typeahead

Suggestions on every keystroke, for a search box used a billion times a
day. The latency budget is so tight that it decides the architecture,
which is exactly why this question is asked.

**Constraints to state and honor**
- p99 under 100 ms end to end, including the network — so the compute budget is a few tens of milliseconds.
- A keystroke is a request: 10× the query volume of search itself.
- Suggestions are ranked by popularity, refreshed at least daily; trending terms should appear within minutes.
- Personalized suggestions for signed-in users, without breaking the cache.

**Grading points**
- The latency budget decomposed before any design: RTT, TLS, service, index lookup — and what is left over ([[foundations-latency-network-rtts]], [[foundations-latency-requirement-precision]], [[networking-tls-resumption]]).
- Prefix index structure chosen and its memory cost stated; segments and near-real-time refresh explained rather than assumed ([[storage-inverted-index]], [[storage-search-segments]], [[storage-search-nrt-refresh]]).
- Sharding by prefix versus by document, with scatter-gather fanout costed and avoided where possible ([[distributed-secondary-index-partitioning]], [[distributed-scatter-gather-fanout-math]], [[distributed-avoiding-scatter-gather]]).
- Tail-latency amplification recognised: at fanout 20, the p99 of a shard is the p50 of the query ([[foundations-tail-latency-amplification]], [[foundations-p999-cost]]).
- Cache placement argued top-down — browser, edge, service-local, shared — with the cost of each extra hop ([[caching-local-vs-remote]], [[caching-layer-absorption]], [[caching-placement-cost-of-depth]]).
- The head of the distribution served from the edge, with a cache key that does not include the user for anonymous traffic ([[networking-cdn-what-belongs-at-edge]], [[networking-cdn-cache-key]], [[networking-cdn-stale-while-revalidate]]).
- Personalization applied as a re-rank on a cached candidate set, so one user's history cannot fragment the cache ([[caching-hot-key-replication]]).
- Popularity computed offline in batch and shipped as a new index generation, with trending handled by a separate faster path ([[analytics-batch-vs-stream]]).

**Attempt log**
- [ ] Attempt 1 (date, 40 min, self-graded notes):
