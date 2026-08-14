---
id: caching-refresh-ahead-fit
node: caching.strategies
type: qa
---
## Q
When is refresh-ahead worth the complexity over plain TTL + cache-aside, and what does it waste when misapplied?

## A
Refresh-ahead asynchronously reloads a key *before* its TTL expires, so hot keys never pay a miss.

- Worth it when: a small, predictable set of hot keys, expensive recomputation, and strict tail-latency SLOs (a miss = user-visible spike).
- Misapplied on a long-tail keyspace it **refreshes keys nobody will read again**, multiplying backend load instead of reducing it.

Rule of thumb: refresh-ahead for the head of the distribution, TTL-on-demand for the tail.
