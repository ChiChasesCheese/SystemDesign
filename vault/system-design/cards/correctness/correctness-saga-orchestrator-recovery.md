---
id: correctness-saga-orchestrator-recovery
node: correctness.saga
type: qa
---
## Q
The saga orchestrator crashes mid-workflow. What must have been persisted for safe resume, and how are the resulting duplicates and silences handled?

## A
The orchestrator is a **persistent state machine**: it durably records the saga instance + current step *before* dispatching each command (its own DB write + command via outbox — the orchestrator has its own dual-write problem).

On resume, it re-reads state and re-dispatches the in-flight step, so:
- **Duplicates**: every participant command carries a deterministic id (`saga_id:step`) and participants are idempotent consumers.
- **Silence** (reply lost or participant down): per-step **timeouts** drive the state machine into retry or compensation — a saga must never wait forever.

This is exactly what workflow engines (Temporal) give you off the shelf: durable step state + deterministic replay, so you don't hand-roll the recovery matrix.
