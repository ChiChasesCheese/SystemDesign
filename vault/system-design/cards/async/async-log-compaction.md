---
id: async-log-compaction
node: async.log
type: qa
---
## Q
How does Kafka log compaction work, what does a compacted topic guarantee, and what is it for?

## A
A background cleaner rewrites old log segments, keeping **only the latest record per key**; a `null` value is a **tombstone** that marks the key for deletion (retained for a grace period so consumers see it before it vanishes). The active segment is never compacted, and offsets are preserved — they just become sparse.

Guarantee: a consumer reading from the beginning gets **at least the final state of every key** — a full snapshot plus recent history, in bounded space.

Use it for **changelog/state topics**: CDC feeds, materialized-view backing state (Kafka Streams), config/entity snapshots. Use time-based retention instead when you need *every* event, not just the last per key.
