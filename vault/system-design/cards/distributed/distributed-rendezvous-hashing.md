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

## Q zh
什么是会合哈希（rendezvous hashing）？它与一致性哈希有何不同？

## A zh
**一致性哈希**：映射键 → 一个环上的位置，节点也映射到环；键找最近的顺时针节点。节点加入/离开时，仅一些键移动。

**会合哈希**：对每个 key，计算 hash(key, node) 对所有节点，选择最高哈希的节点。更简单且对节点加入/离开中的数据移动更敏感，但更容易推理且无虚拟节点复杂性。

权衡：一致性哈希最小化重新映射（更好的性能），会合哈希更简洁但在扩展时移动更多数据。
