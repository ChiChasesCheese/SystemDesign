---
id: async-exactly-once-myth
node: async.delivery
type: qa
---
## Q
An interviewer asks: "Can a message broker give you exactly-once delivery?" What is the correct senior answer?

## A
No — **exactly-once *delivery* is impossible** over an unreliable network: if the ack is lost, the sender cannot distinguish "processed, ack lost" from "never processed", so it must either retry (duplicate) or not (loss).

What systems achieve is **effectively-exactly-once *processing***: at-least-once delivery + dedup at the consumer (idempotency keys, transactional offsets-plus-output as in Kafka transactions, or naturally idempotent writes). The guarantee lives at the endpoints, not in the pipe.
