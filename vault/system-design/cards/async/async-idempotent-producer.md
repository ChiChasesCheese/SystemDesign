---
id: async-idempotent-producer
node: async.delivery.exactly-once
type: qa
---
## Q
Kafka's idempotent producer: what mechanism deduplicates, and which duplicates does it NOT eliminate?

## A
The broker assigns each producer a **producer id (PID)**; the producer stamps every batch with a **per-partition sequence number**. On a retry, the broker sees the sequence it already appended and discards the duplicate — exactly-once *append per producer session per partition*, on by default in modern Kafka.

It does NOT cover:
- **Application-level resends** — a new producer instance (new PID) after a crash, or your app calling `send()` twice.
- Duplicates from **consumer replays** downstream.

So it fixes broker-retry duplicates only; end-to-end dedup still needs [[correctness-idempotent-consumer-patterns]] or transactions.
