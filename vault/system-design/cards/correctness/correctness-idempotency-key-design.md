---
id: correctness-idempotency-key-design
node: correctness.idempotency
type: qa
---
## Q
Design the idempotency-key flow for a `POST /payments` endpoint (Stripe-style). Who generates the key, what does the server store, and what does a retry get back?

## A
- **Client generates** the key (UUID) *per operation intent* — one key per "charge this cart once", reused across all retries of that intent, never per HTTP attempt.
- Server, in the **same transaction** as the side effect, inserts the key into a keyed store (unique constraint) along with request hash and, on completion, the **serialized response**.
- A retry with the same key returns the **stored original response** (same status code and body) — it does not re-execute.
- If the retry's request body differs from the stored hash, reject with 422: same key + different params is a client bug, not a retry.
