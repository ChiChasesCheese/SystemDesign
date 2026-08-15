---
id: distributed-rendezvous-hashing
node: distributed.partitioning.schemes
type: qa
---
## Q
Rendezvous (highest-random-weight) hashing vs a consistent-hashing ring — how does it work, and when is it the better pick?

## A
For a key, compute `hash(key, node)` for **every** node and pick the node with the highest score; for k replicas, take the top k. Membership change moves only the keys whose winner disappeared — the same minimal-disruption property as a ring, with **no tokens, no vnodes, and no ring state to distribute**. Weighting is a simple per-node multiplier on the score.

Prefer it when:

- The node set is **small and known to every client** (cache tiers, load balancers, shard maps of tens of nodes) — lookup is O(n) per key, which only hurts at large n (cacheable, or use its logarithmic variants).
- You need **ordered replica selection** or per-node weights without hand-tuning token counts.

Prefer the ring when node counts are large or the map must be gossiped incrementally. Related cousin: **Maglev hashing**, which builds a lookup table for O(1) hits and near-perfect balance, used for L4 load balancing.
