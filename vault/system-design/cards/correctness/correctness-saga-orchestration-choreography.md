---
id: correctness-saga-orchestration-choreography
node: correctness.saga
type: qa
---
## Q
Orchestrated vs choreographed saga: how does each work, and when do you pick which?

## A
- **Choreography**: each service reacts to the previous service's events (order-created → payment listens → payment-charged → inventory listens). No central brain. Fine for **2–3 steps**; beyond that the workflow exists nowhere — you can't see state, and compensation paths sprawl across services.
- **Orchestration**: a coordinator (state machine, often Temporal/Step Functions) commands each step and drives compensations on failure. Workflow state is explicit, observable, and testable; the orchestrator is extra infra and a dependency.

Pick orchestration for anything money-shaped or with >3 steps; the "orchestrator = single point of failure" worry is solved by persisting its state and making step handlers idempotent.
