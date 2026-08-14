---
id: correctness-saga-compensation-limits
node: correctness.saga
type: qa
---
## Q
"On failure, just run the compensations." What three realities make saga compensation harder than a rollback?

## A
- **Compensation is semantic undo, not rollback**: a refund is a new transaction (fees, records, latency), and some actions are **non-compensatable** — you can't un-send a wire or un-ship a package. Order steps so the *pivot* (point of no return) comes after everything retriable, e.g. authorize card early, **capture last**.
- **Compensations can fail too** — they must be idempotent and retried forever (or page a human); there is no compensation for the compensation.
- **No isolation**: other transactions saw the intermediate state (lost update, dirty read). Countermeasures: *semantic locks* (mark rows `PENDING`), reordering, or commutative operations.
