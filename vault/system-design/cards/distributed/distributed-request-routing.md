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

## Q zh
分布式系统中的请求路由是什么？客户端如何找到正确的分片？

## A zh
客户端需要知道哪个服务器/分片持有一个键。**路由**是将键映射到分片/服务器的过程。

方法：
- **一致性哈希** — 客户端计算 hash(key)，找最近的节点。
- **范围分片** — 键被范围分配（如 A-M 到服务器 1，N-Z 到服务器 2）；客户端根据键进行查表。
- **中间代理** — 客户端发送到代理，代理知道映射并转发。

如果映射改变（节点故障），客户端重新路由和重试。
