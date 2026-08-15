---
id: structure-state-entry-exit-actions
node: structure.state-machines
type: qa
---
## Q
Entering SHIPPED must email the customer, stop the cancellation timer, and release the reserved stock. Where do these side effects belong, and what's the ordering rule?

## A
On the machine, not the callers — otherwise every call site must remember the full list:

- **Exit action** of the old state: undo what the state owned (stop the cancel timer, release the hold).
- **Entry action** of the new state (Moore) — runs no matter which transition arrived. Effects specific to *one* transition go on that transition (Mealy).

Ordering rule: **guard → mutate state → then effects**, and effects must run *outside* any lock and after the state change is committed. Otherwise you email "shipped" for a transition that then fails a later check, or an exception mid-effect leaves the entity between states.

Make effects a list of collected commands the machine emits and the caller executes — that also keeps the transition logic testable without stubbing the mailer.
