---
id: distributed-fixed-partition-count
node: distributed.partitioning.rebalancing
type: cloze
---
The fixed-partition trick: create far more logical partitions than nodes up front (say 1024 partitions on 10 nodes) and rebalance by {{c1::reassigning whole partitions to different nodes — the key-to-partition function never changes, only the partition-to-node map}}. Adding a node then means {{c2::stealing a few partitions from every existing node, and only the partitions being moved are in flight; reads/writes keep going against the old owner until the handover completes}}. The permanent cost is that the partition count is effectively {{c3::fixed for the life of the dataset, so it caps the maximum number of nodes (one partition per node) and sets a floor on per-partition overhead (memory, files, repair units) when the cluster is small}}. Elasticsearch's per-index shard count and Kafka's per-topic partition count are the same design — which is why {{c4::increasing partitions later requires a reindex/split, and for Kafka breaks key-to-partition ordering for existing keys}}.
