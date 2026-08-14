---
id: async-cdc-initial-snapshot
node: async.streaming
type: qa
---
## Q
You turn on CDC for a table that already has 500M rows. How do you get the existing data plus ongoing changes without loss or inconsistency?

## A
**Snapshot + WAL handoff**: record the current log position (LSN/GTID), read a consistent snapshot of the table, then stream the WAL **from the recorded position**. Rows changed during the snapshot appear twice (snapshot version, then change event) — safe because CDC consumers must be idempotent upserters anyway.

Naive alternatives fail: WAL-only misses all pre-existing rows; dump-then-tail-from-"now" loses changes made during the dump.

At 500M rows a blocking snapshot is impractical — modern connectors (Debezium) do **incremental snapshots**: chunked key-range reads interleaved with live streaming, deduplicated via watermarks, resumable mid-way.
