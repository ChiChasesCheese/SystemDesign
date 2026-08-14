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
