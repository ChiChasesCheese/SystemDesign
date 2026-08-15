---
id: distributed-anti-entropy-cost
node: distributed.replication.leaderless
type: qa
---
## Q
Anti-entropy repair is "just a background job" — what does it actually cost, and what breaks if you skip it for too long?

## A
Cost: each pair of replicas builds a **Merkle tree over its ranges** (full read of the data on disk — CPU + IO comparable to a table scan), exchanges hashes top-down, then streams only the differing leaf ranges. So the *comparison* is cheap in bandwidth but the **tree build is a full scan of every replica**, which is why full repair is scheduled off-peak and throttled, and why it is the dominant operational cost of large Cassandra clusters.

Skip it too long and you get **deleted data resurrecting**: deletes are tombstones with a grace period (`gc_grace_seconds`, 10 days by default). If a replica missed the tombstone and the tombstone is garbage-collected elsewhere before repair runs, that replica re-propagates the **old live value** and the row comes back. Rule: repair every range within the grace period, or raise the grace period.
