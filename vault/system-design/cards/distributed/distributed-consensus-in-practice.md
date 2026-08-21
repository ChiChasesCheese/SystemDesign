---
id: distributed-consensus-in-practice
node: distributed.consensus
type: qa
---
## Q
Where does consensus actually sit in production architectures, and why don't you run your main data path through it?

## A
It sits in the **control plane**, on small state: leader election, cluster membership, shard→node maps, distributed locks, config — via etcd/ZooKeeper (Kubernetes, Kafka's KRaft), or per-shard Raft groups replicating a WAL (CockroachDB, TiDB, Kafka partitions).

You keep bulk data off a single consensus group because every write pays a **quorum round-trip and one leader's throughput cap** — it doesn't scale horizontally; you scale by running **many independent Raft groups** (one per shard/partition). Interview phrasing: "consensus for coordination and metadata; replication + partitioning for data, often consensus-per-shard."

## Q zh
实际中使用的共识算法有哪些，各有什么权衡？

## A zh
**Raft**：易于理解，领导者选举清晰。缺点：严格的领导者依赖，log 重放可能慢，单点写吞吐。

**Paxos**：容错性更强，但复杂难以理解。多 leader 变种可能提高吞吐。

**Zookeeper**：ZAB 协议，强一致，但设计用于配置管理和领导者选举（低写频率）。

**Etcd**：基于 Raft，易用，适合配置和服务发现。

权衡点：强一致性 vs 可用性，实现复杂度 vs 性能，log 管理成本。
