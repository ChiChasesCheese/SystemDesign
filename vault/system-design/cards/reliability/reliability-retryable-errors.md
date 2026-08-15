---
id: reliability-retryable-errors
node: reliability.resilience.retries
type: qa
---
## Q
Classify which failures are worth retrying and which are not — and explain why a *timeout* is the hardest case.

## A
- **Retry**: connection refused / reset / DNS failure *before* the request was sent (nothing executed), `503`, `429` (obey `Retry-After`), gRPC `UNAVAILABLE` / `RESOURCE_EXHAUSTED`, and read-only requests that failed anywhere.
- **Never retry**: deterministic client errors — `400`, `401`, `403`, `404`, `422`, gRPC `INVALID_ARGUMENT` / `PERMISSION_DENIED`. The same request will fail identically; retrying only burns budget and hides the bug.
- **Timeout / `502` / `504` on a write is ambiguous**: you cannot distinguish "never arrived" from "succeeded, response lost". Blind retry risks a double charge; giving up risks losing a completed order the user thinks failed.

The fix is to remove the ambiguity, not to guess: send an **idempotency key** so the server can recognize the retry and replay the original outcome. Then every write becomes retryable by construction — "retryable" is a property you design in, not one you discover in the error code.
