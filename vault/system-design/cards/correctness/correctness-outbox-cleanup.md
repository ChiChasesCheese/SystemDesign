---
id: correctness-outbox-cleanup
node: correctness.outbox
type: qa
---
## Q
An outbox table in Postgres receives every event the system emits. What operational problem builds up, and how do you clean it without breaking the pattern?

## A
Published rows accumulate: table and index **bloat**, MVCC dead tuples from delete/update churn, vacuum pressure, and slowing relay polls.

- **Delete-after-ack** (or CDC style: insert+delete in the same txn, relay reads the WAL insert) keeps the table near-empty but maximizes churn.
- **Mark sent + batch-purge** after a retention window — retention gives you a redelivery/debug buffer but keeps bloat.
- At high volume: **time-partitioned outbox table**, drop old partitions — `DROP PARTITION` is instant metadata work, no vacuum debt.

Never purge unpublished rows; purge eligibility = acked by the relay AND older than the dedup window your consumers rely on.
