---
id: storage-inmemory-advantage
node: storage.internals
type: qa
---
## Q
A disk database with its working set fully in OS page cache still loses to Redis. If not disk reads, what is the in-memory store's real advantage — and how does it get durability anyway?

## A
It skips the machinery of pretending memory is disk: no encoding rows into disk-page format, no buffer-pool management, and it can use structures impractical to serialize to disk — Redis's sorted sets, native lists, HyperLogLog. Plus a single-threaded event loop with no locking on the hot path.

Durability without losing the speed: writes are **appended to a log** (Redis AOF, `everysec` fsync by default) and/or periodic **snapshots** (RDB); recovery replays them. The dataset must fit in RAM — the log is for recovery, not for reads. Trade-off: `everysec` risks ~1s of writes on crash.
