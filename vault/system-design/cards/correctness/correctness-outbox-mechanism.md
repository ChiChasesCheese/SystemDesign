---
id: correctness-outbox-mechanism
node: correctness.outbox
type: qa
---
## Q
Walk through the transactional outbox pattern: what happens in the transaction, how do events reach the broker, and what guarantee do you end up with?

## A
1. In **one local transaction**: apply the state change AND insert the event row into an `outbox` table. Atomic — either both exist or neither.
2. A **relay** moves outbox rows to the broker: either a poller (`SELECT ... FOR UPDATE SKIP LOCKED`, publish, mark sent) or **CDC tailing the WAL** (Debezium outbox routing — lower latency, no polling load).
3. Relay marks/deletes rows only *after* broker ack → a crash re-publishes → guarantee is **at-least-once**, so consumers dedup by the event id stored in the outbox row.

You've traded "maybe lost" for "maybe duplicated" — which idempotency can fix, whereas a lost event is unrecoverable.
