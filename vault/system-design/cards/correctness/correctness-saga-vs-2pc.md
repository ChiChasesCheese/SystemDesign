---
id: correctness-saga-vs-2pc
node: correctness.saga
type: qa
---
## Q
Why do payment/order systems use sagas instead of distributed transactions (2PC) across services — and what do you give up?

## A
2PC requires every participant to hold **locks while blocked on a coordinator** — across heterogeneous services (some of which are external APIs that simply don't speak 2PC), that means unbounded lock holding and availability coupled to the slowest participant.

A **saga** replaces the atomic transaction with a sequence of local transactions, each with a **compensating action** to semantically undo it on failure.

You give up **isolation** (the "I" in ACID): intermediate states are visible to other transactions — an order can be seen "reserved" and then get cancelled. Atomicity becomes "eventually all steps or all compensations."
