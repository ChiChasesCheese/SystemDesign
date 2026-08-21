---
id: distributed-consistent-hashing
node: distributed.partitioning.schemes
type: qa
---
## Q
In consistent hashing, what fraction of keys moves when a node joins an N-node ring, why is that the whole point, and what problem do virtual nodes solve?

## A
Only ~**K/N** of K keys move — the keys between the new node and its predecessor on the ring. With naive `hash(key) mod N`, changing N remaps **almost every key**, which would flush caches or trigger a full data reshuffle; consistent hashing makes membership change cheap.

**Virtual nodes** (each physical node owns many ring positions, e.g. 100–256) fix two issues: with few positions, random placement makes ownership arcs **wildly uneven**, and a leaving node dumps its entire range onto **one successor**. Vnodes even out load and spread a departed node's data across the whole cluster.

## Q zh
一致哈希是什么，它解决了什么问题？

## A zh
**一致哈希**：将 key 和 server 都映射到一个哈希环上，key 的值对应环上最近的顺时针 server。

**解决的问题**：
- **普通哈希 hash(key) % n** 当 server 数 n 变化时，所有 key 都要重新定位（雪崩）。
- **一致哈希**：加减 server 时，只有该 server "邻近" 的 key 需要迁移，迁移量 ∝ 1/n（增量不太大）。

**改进**：虚拟节点（virtual nodes）解决 server 分布不均匀的问题。
