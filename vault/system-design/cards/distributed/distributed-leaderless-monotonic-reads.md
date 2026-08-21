---
id: distributed-leaderless-monotonic-reads
node: distributed.replication.leaderless
type: qa
---
## Q
In a Dynamo-style store with W=2, R=2, N=3, a client reads a value and then reads it again and gets an *older* value. Explain how, and why the leader-based fix doesn't apply.

## A
A write reaches replicas one at a time. Read 1's coordinator happened to contact `{A, B}` where A had the new value; read 2's coordinator contacted `{B, C}` — neither of which was updated yet — so it legally returns the old one. Both quorums were valid; quorum overlap guarantees you *can* see the latest acknowledged write, not that you **stop** seeing it. That's a **monotonic reads** violation.

The leader-based fix — pin the session to one replica — doesn't work here because there is no fixed replica per key: **a different coordinator picks a different subset each request**, and any node can coordinate. Leaderless fixes instead:

- Have the client carry the **highest version it has seen** and reject/retry a quorum result older than it.
- Turn on **synchronous read repair** so a read that observes the new value pushes it to a write quorum before returning.

## Q zh
无主复制中怎样保证单调读（monotonic reads）？

## A zh
**单调读问题**：写 v1 到副本 A，写 v2 到副本 A 和 B。客户端先读副本 A（看到 v2），后读副本 B（还是旧值 v0）。客户端看到时间反向（v2 → v0）。

**解决方案**：
1. **版本检查**：客户端记录读到的最大版本，下次读时确保副本已复制该版本才返回。
2. **Sticky session**：同一客户端总是从同一副本读，保证单调性（代价是故障时可用性差）。
3. **因果一致性**：用向量时钟等机制保证读的因果序列。

权衡：单调读 vs 可用性/响应时间。
