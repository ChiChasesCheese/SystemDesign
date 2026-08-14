---
id: correctness-dual-write-problem
node: correctness.outbox
type: qa
---
## Q
A service commits to Postgres, then publishes an event to Kafka. Enumerate the failure modes of this "dual write" — and why wrapping both in try/catch doesn't fix it.

## A
- **Commit then crash before publish** → state changed, event lost; downstream never learns. (The common, silent one.)
- **Publish then commit fails** → phantom event for state that doesn't exist.
- **Retry the publish** after ambiguity → duplicates, and possibly out of order.

Try/catch can't help because there is **no atomic commit spanning two independent systems** — the broker doesn't participate in the DB transaction, and 2PC across DB + Kafka is impractical (broker support, blocking coordinator). The fix is to make the event part of the DB transaction: the transactional outbox.
