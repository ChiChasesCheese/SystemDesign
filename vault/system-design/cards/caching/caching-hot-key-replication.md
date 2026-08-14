---
id: caching-hot-key-replication
node: caching.placement
type: qa
---
## Q
One cache key (a celebrity's profile during an event) exceeds what a single cache node can serve. Why doesn't adding nodes help, and what does?

## A
Sharding places each key on exactly **one** node — more nodes just move the key; that node's NIC and CPU still cap the key's throughput.

- **Key replication**: write the value under R suffixed copies (`key#1..#R`), readers pick one at random — R× read capacity, at the cost of R× invalidation fan-out and R-way brief inconsistency.
- **Local L1 for the hottest set**: an in-process cache with second-level TTLs absorbs most reads before they reach the shared tier ([[caching-local-vs-remote]]).

Detect hot keys by sampling key frequency at the client — before the node melts, not after.
