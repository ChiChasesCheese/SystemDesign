---
id: distributed-lag-anomalies
node: distributed.replication.leader
type: qa
---
## Q
Name the two classic read anomalies replication lag causes besides missing your own writes, and the guarantee that fixes each.

## A
- **Going backwards in time**: successive reads hit differently-lagged replicas, so data you already saw disappears. Fix: **monotonic reads** — pin a session to one replica (or track a min-version the serving replica must have).
- **Seeing effects before causes**: an answer replicates faster than the question it references. Fix: **consistent prefix / causal reads** — expose writes only in an order that preserves causality (per-partition ordering, causal tokens).

Both are session/ordering guarantees — far cheaper than making all reads linearizable, which is the sledgehammer answer.

## Q zh
读取从库延迟（read-after-write inconsistency）会导致什么异常？

## A zh
**场景**：客户端写入主库，立即读从库。从库可能还未复制该写入。客户端读到旧值→"我刚写的数据呢？"。

**异常类型**：
1. **Read-After-Write 不一致**：写入的数据在后续读取中消失。
2. **单调读不一致**：客户端先读从库 A（版本 v1），后读从库 B（版本 v0），看起来时间反向。
3. **因果一致性破裂**：写 A 依赖写 B，客户端读时看到 A 但没看到 B。

**缓解**：sticky session（同一客户端总是读同一从库，该从库复制快）。read from primary（重要读只读主库）。版本检查（客户端记录写入的版本，读时等待从库赶上）。
