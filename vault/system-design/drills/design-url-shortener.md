---
nodes: [foundations.method, foundations.estimation, storage.nosql, caching.strategies, distributed.partitioning.schemes, networking.dns]
tags: [classic, warmup]
---
# Drill: Design a URL shortener

The warm-up question, and the one people fail by treating it as trivial.
Short links for 100M new URLs a day, redirects served worldwide, links
that outlive the service that made them.

**Constraints to state and honor**
- 100M writes/day; reads are ~100× writes and spiky (one link can be 1% of global traffic for an hour).
- Redirect latency p99 under 50 ms anywhere in the world.
- Links are permanent unless an expiry is set; custom aliases are allowed.
- Deleted or expired links must stop resolving quickly — this is the part people forget.

**Grading points**
- The first three minutes spent narrowing scope — analytics? custom aliases? auth? — instead of drawing boxes ([[foundations-interview-opening-moves]], [[foundations-clarifying-questions-worth-asking]]).
- QPS and five-year storage derived out loud, and the derivation used to reject an over-built design ([[foundations-dau-to-qps]], [[foundations-storage-estimate-method]], [[foundations-when-estimates-change-design]]).
- Key generation compared honestly: counter + base62, hash + collision check, or a pre-minted key range per writer — and the collision cost of each.
- The shard key named as a one-way door, with hash partitioning on the short key chosen for even spread ([[distributed-shard-key-one-way-door]], [[distributed-hash-vs-range]], [[distributed-consistent-hashing]]).
- A key-value/wide-column store justified by the access pattern — one point lookup, no joins ([[storage-wide-column-modeling]], [[storage-document-vs-relational]]).
- Cache-aside on the read path, plus negative caching so a bad link does not become a database DDoS ([[caching-aside-vs-read-through]], [[caching-negative-caching]]).
- Deletes as tombstones and what that means for the cache — delete the key, do not update it ([[storage-tombstone-deletes]], [[caching-delete-not-update]]).
- DNS and anycast for the redirect domain, with TTL understood as the failover lever it is ([[networking-anycast-vs-geodns]], [[networking-dns-ttl-failover]]).

**Attempt log**
- [ ] Attempt 1 (date, 40 min, self-graded notes):
