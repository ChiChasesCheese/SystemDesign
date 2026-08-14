---
id: correctness-saga-compensation-race
node: correctness.saga
type: qa
---
## Q
A saga cancellation can race its own forward action: the "release seat" compensation arrives at a participant **before** the delayed "reserve seat" command. What happens, and what's the fix?

## A
Naively, the release is a no-op ("nothing reserved"), then the late reserve lands and **holds the seat forever** — the saga believes it rolled back, the participant disagrees.

Fix: compensation must be a **tombstone, not just an undo**. The participant records "saga X: cancelled" so a forward command arriving after its own compensation is **rejected**, not applied. Requires per-saga state at the participant and a retention window longer than max command delay.

General rule: with at-least-once delivery and no ordering across queues, every participant must handle each saga command **in any order and any multiplicity** — commutativity of cancel-before-act is part of the contract.
