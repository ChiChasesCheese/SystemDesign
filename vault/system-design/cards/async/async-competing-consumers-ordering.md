---
id: async-competing-consumers-ordering
node: async.queues
type: qa
---
## Q
Why do competing consumers on a classic queue destroy message ordering even though the queue is FIFO — and what are the fixes when per-entity order matters?

## A
FIFO only governs *dispatch*. With N consumers, messages for the same entity run **concurrently** (msg 2 can finish before msg 1), and a nack/redelivery re-enqueues a message *behind* ones sent after it. Prefetch buffers make the interleaving worse.

Fixes:
- **Partition by entity key** with one consumer per partition (Kafka model, SQS FIFO message groups).
- **Single-active consumer** per queue (RabbitMQ) — order preserved, parallelism sacrificed.
- Make consumers **order-tolerant**: version numbers + last-writer-wins or conditional updates, treating order as unguaranteed.
