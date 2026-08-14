---
id: correctness-idempotent-consumer-patterns
node: correctness.idempotency
type: qa
---
## Q
Beyond an idempotency-key table, name three ways to make a mutation safe to apply twice — and the classic operation that is NOT naturally idempotent.

## A
- **Natural idempotency**: absolute writes — `SET status = 'shipped'`, upsert by primary key. Applying twice converges to the same state.
- **Conditional write / compare-and-set**: `UPDATE ... WHERE version = 41` or `WHERE status = 'pending'` — the second application matches zero rows.
- **Dedup by processed-event id**: consumer records `(consumer, event_id)` with a unique constraint in the **same transaction** as its state change.

Not naturally idempotent: **relative updates** — `balance = balance + 100`. Any increment/decrement must be guarded by one of the above.
