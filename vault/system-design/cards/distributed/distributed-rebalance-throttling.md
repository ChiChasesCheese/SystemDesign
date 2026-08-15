---
id: distributed-rebalance-throttling
node: distributed.partitioning.rebalancing
type: qa
---
## Q
Why is fully automatic, unthrottled rebalancing a well-known way to turn a small failure into an outage — and what are the standard guards?

## A
Rebalancing consumes exactly the resources you are short of: disk IO, network, and page cache, **at the moment the cluster is already degraded**. The cascade: a node is falsely declared dead (GC pause, slow disk) → the cluster starts re-replicating its data → the extra load slows *other* nodes past the failure detector's threshold → they're declared dead too → more rebalancing. This death spiral has taken down real clusters that never lost a machine.

Guards:

- **Rate limits**: cap stream throughput and concurrent recoveries (Cassandra `stream_throughput_outbound`, Elasticsearch `cluster.routing.allocation.node_concurrent_recoveries` and the recovery byte budget).
- **Delay before acting**: don't move data until the node has been gone for N minutes (Elasticsearch `index.unassigned.node_left.delayed_timeout`, default 1m) — most node absences are restarts.
- **Human in the loop**: automatic *proposal*, operator-approved *execution*, for the largest moves.
