---
id: distributed-anti-entropy-cost
node: distributed.replication.leaderless
type: qa
---
## Q
Anti-entropy repair is "just a background job" — what does it actually cost, and what breaks if you skip it for too long?

## A
Cost: each pair of replicas builds a **Merkle tree over its ranges** (full read of the data on disk — CPU + IO comparable to a table scan), exchanges hashes top-down, then streams only the differing leaf ranges. So the *comparison* is cheap in bandwidth but the **tree build is a full scan of every replica**, which is why full repair is scheduled off-peak and throttled, and why it is the dominant operational cost of large Cassandra clusters.

Skip it too long and you get **deleted data resurrecting**: deletes are tombstones with a grace period (`gc_grace_seconds`, 10 days by default). If a replica missed the tombstone and the tombstone is garbage-collected elsewhere before repair runs, that replica re-propagates the **old live value** and the row comes back. Rule: repair every range within the grace period, or raise the grace period.

## Q zh
反熵修复的成本是什么？

## A zh
**I/O 和网络成本**：需要扫描所有副本的所有数据，比较哈希或完整值，然后修复差异。对于大数据集，这是 O(n)。

**background repair**：通常在后台定期运行（周级或月级），不阻塞前台请求。但如果数据量大，修复周期会很长，故障发生时可能已经有旧数据。

权衡：定期反熵确保最终一致，但成本高；替代方案是依赖 read repair（只修复被读到的不一致）。
