---
id: async-retry-delay-implementation
node: async.queues
type: qa
---
## Q
Your consumer needs retries with backoff (5s, 1m, 10m), but the broker delivers immediately. How is delayed retry actually implemented, and what does it cost you?

## A
- **Kafka**: no native delay — use **tiered retry topics** (`orders-retry-5s`, `-1m`, `-10m`); a failed message is republished to the next tier, whose consumer pauses until the message's due time, then finally to the DLQ.
- **RabbitMQ**: per-message TTL + dead-letter exchange, or the delayed-message plugin.
- **SQS**: native per-message delay / visibility-timeout extension — simplest option.

Cost: the message **leaves its original ordering context** — anything behind it proceeds, so retried messages are processed out of order and consumers must tolerate that (version checks, idempotency). If strict per-key order matters, you must instead block the key (or partition) while retrying in place.
