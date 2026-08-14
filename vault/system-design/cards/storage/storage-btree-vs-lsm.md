---
id: storage-btree-vs-lsm
node: storage.internals
type: qa
---
## Q
When do you pick an LSM-tree engine (RocksDB, Cassandra) over a B-tree engine (Postgres, InnoDB), and what do you pay for it?

## A
Pick LSM for **write-heavy** workloads: writes are sequential appends (memtable + WAL, flushed to sorted SSTables), so ingest throughput far exceeds a B-tree's random in-place page writes.

You pay with:
- **Read amplification** — a point read may check the memtable plus several SSTable levels (bloom filters mitigate).
- **Compaction** — background rewriting that steals I/O/CPU and causes latency spikes when it falls behind.

B-trees win on read-heavy/mixed workloads and give predictable point/range read latency; each key lives in exactly one place.
