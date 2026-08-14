---
id: correctness-idempotency-concurrent-retries
node: correctness.idempotency
type: qa
---
## Q
Two requests with the same idempotency key arrive concurrently (client timeout fired while the original was still running). What must the server do?

## A
- The key insert's **unique constraint** makes exactly one request the winner; the loser must NOT run the operation.
- The loser either **waits** for the winner's result or returns **409/425 "in progress"** with Retry-After — never a second execution, never an error implying the payment failed.
- Key record needs a state machine (`started` → `succeeded`/`failed`) so a crash mid-operation leaves a detectable `started` row for recovery, instead of a key that permanently blocks or silently double-charges.
- The check-then-act must be a single atomic insert — a read-then-insert race is exactly the double-charge you built this to prevent.
