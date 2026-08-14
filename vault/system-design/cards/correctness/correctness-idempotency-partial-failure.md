---
id: correctness-idempotency-partial-failure
node: correctness.idempotency
type: qa
---
## Q
A payment handler claims its idempotency key, calls the card processor, then crashes before recording the result. The key is stuck "in-progress". What must recovery do?

## A
The processor may or may not have charged — so neither blind retry nor blind fail is safe.

- Attach a **lease/expiry** to the in-progress state; a stuck key past its lease goes to a **recovery step**, not straight to re-execution.
- Recovery **queries the downstream by ITS idempotency key** ("did charge X happen?") — possible only if you persisted the downstream key *before* the outbound call.
- Then finish deterministically: record the found result, or safely re-issue with the **same** downstream key so the processor dedups.

Rule: every external call inside an idempotent handler needs its own pre-persisted idempotency key — that's what makes the crash window recoverable ([[correctness-idempotency-concurrent-retries]]).
