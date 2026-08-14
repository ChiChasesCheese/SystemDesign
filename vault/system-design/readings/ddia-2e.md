---
nodes: [storage.internals, distributed.replication, distributed.transactions, async.streaming]
url: https://dataintensive.net/
tags: [book, canonical]
---
# Designing Data-Intensive Applications, 2nd ed. (Kleppmann & Riccomini, 2026)

The systematic backbone for the entire Storage / Distributed Data / Async
region of this map — the cards are recall hooks for what these chapters
explain properly. The 2nd edition adds cloud-native architecture
(storage–compute separation, object storage) and AI-era data systems.

**Reading order against this map:**
- Storage engines (B-trees vs LSM) → `storage.internals`
- Replication + Partitioning → `distributed.replication`, `distributed.partitioning`
- Transactions → `distributed.transactions`
- The trouble with distributed systems → `distributed.time`
- Derived data / stream processing → `async.streaming`
