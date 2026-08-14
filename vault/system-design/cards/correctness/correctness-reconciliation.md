---
id: correctness-reconciliation
node: correctness.ledger
type: qa
---
## Q
Your ledger has idempotency keys, an outbox, and zero-sum checks. Why do you still run reconciliation against the payment processor, and what does the job actually do?

## A
Because those patterns protect *your* writes — they can't see the **external world disagreeing**: charges that succeeded at the processor after you recorded a timeout-failure, fees and FX applied on their side, chargebacks, or plain bugs on either end. Reconciliation is the safety net that catches what every other control missed.

The job: ingest the processor's **settlement report**, match line-items to ledger entries (by processor id / idempotency key), and bucket every mismatch — **missing ours** (they have it, we don't), **missing theirs**, **amount/state mismatch** — into a workqueue with an owner and an aging SLA. Match rate and unresolved-break age are the health metrics; run it daily at minimum.
