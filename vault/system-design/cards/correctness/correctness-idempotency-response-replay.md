---
id: correctness-idempotency-response-replay
node: correctness.idempotency
type: qa
---
## Q
On an idempotency-key hit, why must the server replay the **stored response** rather than re-execute the handler "since it's idempotent anyway"?

## A
Re-execution can **diverge** from the original run: prices, FX rates, fees, or risk rules may have changed; generated values (ids, timestamps) differ; and referenced state may have moved on (the order it read is now cancelled). The client would see two *different* answers to the same request — breaking the contract that a retry is indistinguishable from the first attempt.

So the key record stores the **full response (status + body)** written when the operation completes, and every subsequent hit returns those bytes verbatim (Stripe model). Re-execution is only safe for truly deterministic, side-effect-free reads — which don't need idempotency keys at all.
