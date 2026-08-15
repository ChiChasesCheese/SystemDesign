---
id: distributed-request-routing
node: distributed.partitioning.rebalancing
type: qa
---
## Q
A client holds a key — how does the request find the right partition's node? Give the three routing approaches and where the partition map lives.

## A
- **Ask any node**: nodes share the map (gossip) and forward misdirected requests — no extra infra, one possible extra hop (Cassandra, Riak).
- **Routing tier**: a partition-aware proxy in front forwards requests (Mongo's `mongos`, Vitess's `vtgate`).
- **Partition-aware client**: the client library caches the map and connects directly — fewest hops, smartest clients (Kafka producers, Redis Cluster clients).

The map must be authoritative somewhere: either a **coordination service** (ZooKeeper/etcd — HBase, Kafka historically) that notifies routers on rebalancing, or **gossip + version numbers** so stale routers learn the truth from the nodes they hit. The failure mode to mention: routing on a stale map during a rebalance.
