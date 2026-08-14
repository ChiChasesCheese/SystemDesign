---
id: async-consumer-groups-offsets
node: async.log
type: qa
---
## Q
In a Kafka consumer group, when should you commit offsets relative to processing, and what does each choice cost you?

## A
- **Commit after processing** → at-least-once: a crash between process and commit replays messages, so downstream must be idempotent. This is the default correct choice.
- **Commit before processing** → at-most-once: a crash loses messages. Only acceptable for droppable data (metrics, best-effort notifications).
- Also know: parallelism is capped at partition count — one partition is consumed by at most one member of a group, so 20 consumers on 10 partitions leaves 10 idle.
