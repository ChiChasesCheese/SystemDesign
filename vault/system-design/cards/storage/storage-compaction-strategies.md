---
id: storage-compaction-strategies
node: storage.internals
type: qa
---
## Q
Size-tiered vs leveled compaction in an LSM engine: how does each organize SSTables, and which workload picks which?

## A
- **Size-tiered** (Cassandra STCS): wait for ~4 similar-sized SSTables, merge into one bigger; tiers of ever-larger files. Each byte is rewritten few times (**low write amp**) but key ranges overlap across many files (**high read/space amp** — worst case ~2x space during a merge).
- **Leveled** (RocksDB/LevelDB): levels L1, L2... each ~10x larger, with **non-overlapping** key ranges within a level; a lookup checks at most one file per level. Low read/space amp, but data is rewritten into each level it descends through (**write amp ~10 per level**).

Pick size-tiered for write-heavy/append-mostly (logs, time-series); leveled when reads and space matter more than peak ingest. See [[storage-amplification-triangle]].
