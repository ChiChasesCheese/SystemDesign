---
id: storage-tombstone-deletes
node: storage.nosql
type: qa
---
## Q
Why is a delete in Cassandra actually a *write*, and what makes "using a wide-column table as a queue" a famous anti-pattern?

## A
Data lives in immutable SSTables across replicas, so a delete writes a **tombstone** — a marker that shadows older values until compaction physically removes both, only after `gc_grace_seconds` (default ~10 days, kept so a down replica can learn of the delete; purge earlier and the value **resurrects** via read repair or the recovered replica).

Queue anti-pattern: enqueue-then-delete leaves partitions that are mostly tombstones; every read must scan **thousands of tombstones to find one live row**, latency climbs until reads abort (`tombstone_failure_threshold`). Rapid create-delete churn belongs in a log/queue (Kafka), not an LSM wide-column store.
