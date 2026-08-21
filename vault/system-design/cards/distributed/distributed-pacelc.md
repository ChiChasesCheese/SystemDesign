---
id: distributed-pacelc
node: distributed.cap
type: qa
---
## Q
What does PACELC add over CAP, and how do DynamoDB and Spanner classify under it?

## A
The **ELC part**: *Else* (no partition, i.e. almost always), you still trade **Latency vs Consistency** — strong consistency requires coordination (quorum/leader round-trips) on every operation, paying latency even on a healthy network.

- **DynamoDB (default), Cassandra: PA/EL** — on partition choose availability; normally choose low latency (eventual consistency).
- **Spanner, CockroachDB, ZooKeeper: PC/EC** — on partition refuse minority-side operations; normally pay coordination latency for strong consistency.

Interview use: PACELC explains why "strongly consistent" systems are slower *every day*, not just during rare partitions.

## Q zh
PACELC 定理说什么？它与 CAP 有什么关系？

## A zh
**PACELC**：如果有**分割**，选择可用性 (A) 或一致性 (C)；否则（在正常运行下）权衡延迟 (L) vs 一致性 (C)。

CAP 说分割时不能同时有一致性和可用性。PACELC 说即使没有分割，你也在权衡：强一致性要求等待副本确认（高延迟），弱一致性更快（低延迟但可能过时数据）。

现实系统：Dynamo/Cassandra 选 AP（分割时可用），低延迟；许多 SQL 数据库选 CP，更强保证。
