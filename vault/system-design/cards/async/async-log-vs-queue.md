---
id: async-log-vs-queue
node: async.log
type: qa
---
## Q
What does an append-only log (Kafka) give you that a traditional broker queue (RabbitMQ/SQS) fundamentally cannot?

## A
**Replay.** A queue deletes messages on ack; the log retains them for a retention window (or forever with compaction), and consumers just track offsets.

That enables:
- **Rebuilding derived state** (new index, new materialized view, bug fix) by re-reading from offset 0.
- **Multiple independent consumer groups** reading the same history at their own pace.
- The log acting as **system of record** for event-sourced designs.

Trade-off: no per-message ack/retry/DLQ semantics built in — a stuck message blocks its partition (head-of-line blocking).
