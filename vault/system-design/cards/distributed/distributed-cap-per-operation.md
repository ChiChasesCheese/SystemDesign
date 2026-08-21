---
id: distributed-cap-per-operation
node: distributed.cap
type: qa
---
## Q
Why is "is this system CP or AP?" the wrong granularity — and what is the right one? Give two real examples.

## A
The C/A trade is made **per operation**, not per system — the same store can serve some requests linearizably and others stale.

- **Cassandra/DynamoDB**: consistency level is chosen per read/write (`QUORUM` vs `ONE`; DynamoDB's `ConsistentRead` flag) — one table serves both CP-ish and AP-ish traffic.
- **ZooKeeper**: writes go through consensus, but reads are served **locally by any replica** (possibly stale) unless the client issues `sync` first — so even a "CP" system defaults to non-linearizable reads for speed.

Interview move: instead of labeling the system, state which *operations* need linearizability and pay for only those.

## Q zh
CAP 定理是按操作还是按系统应用的？

## A zh
**按操作**。一个分布式系统在整体上不能选择 CAP 的组合，而是每个操作在分区情况下选择：
- 返回**一致且最新的数据**（放弃可用性，如 Consul 的同步 read）
- 或返回**可能不一致的但总是可用的数据**（放弃一致性，如 Dynamo 的最终一致）

好的系统根据操作的需要灵活选择。
