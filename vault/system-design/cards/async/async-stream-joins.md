---
id: async-stream-joins
node: async.streaming
type: qa
---
## Q
Stream-stream join vs stream-table join: how does each maintain state, and what goes wrong with each?

## A
- **Stream-stream** (clicks ⋈ impressions): both sides are buffered in a **windowed state store**; each arrival probes the other side's buffer. Failure mode: the window bounds the wait — a match arriving later than the window is silently a non-join, so window size trades completeness against state size.
- **Stream-table** (orders ⋈ customer profile): the table side is a **changelog materialized into a local store** (compacted topic → RocksDB); each event looks up current state. Failure mode: **time skew** — the event may join against a *newer* table version than existed at event time; versioned/temporal joins fix this at extra state cost.

Both require **co-partitioning**: same key, same partition count, or a repartition (shuffle) topic is inserted first.
