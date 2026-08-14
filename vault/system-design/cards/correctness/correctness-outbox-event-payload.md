---
id: correctness-outbox-event-payload
node: correctness.outbox
type: qa
---
## Q
Fat events vs thin events in an outbox: what does each carry, and what race does the thin style cause?

## A
- **Fat (event-carried state)**: the outbox row snapshots all needed state *as of the transaction* (`OrderPlaced` + items, amounts, addresses). Consumers are self-sufficient; no read-back. Cost: bigger rows, schema is a public contract you must version.
- **Thin (notification)**: just `order_id` + type; consumers call back to fetch details. Race: by the time the consumer reads, the entity has **changed or vanished** — it sees state from a *later* version than the event describes, or reads the same state twice across different events. It also re-couples consumers to the producer's API and adds read load.

Fintech default: **fat events** — the snapshot-at-commit is exactly what audit and downstream ledgers need.
