---
id: architecture-microservices-tax
node: architecture.services
type: qa
---
## Q
Name the operational bill that arrives with microservices — the things a monolith gave you for free.

## A
- **In-process call → network call**: latency, partial failure, timeouts/retries/circuit breakers on every edge; a deep call graph multiplies tail latency and failure probability.
- **Debugging becomes distributed tracing**: no single stack trace or debugger; you need correlation ids, centralized logging, and tracing infra just to answer "what happened".
- **Transactions become sagas/outboxes**: cross-entity consistency stops being `BEGIN...COMMIT`.
- **Deploy/testing surface explodes**: N pipelines, version-compatibility matrices, contract tests, per-service on-call.

The senior framing: microservices trade **development-time coupling** for **runtime and operational complexity** — worth it only when the org-scaling benefit outweighs this bill.
