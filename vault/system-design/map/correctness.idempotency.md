%% trellis:begin %%
# Idempotency
*Correctness Patterns*

Idempotency keys, dedup windows, and designing every mutation to survive a retry.

**Requires:** [[async.delivery|Delivery Semantics]]

**Unlocks:** [[correctness.ledger|Ledgers & Reconciliation]]

## Readings
- [[stripe-idempotency|Designing robust and predictable APIs with idempotency (Stripe)]]

## Drills
- [[design-notification-fanout|Design a notification service]]
- [[design-payment-ledger|Design a payment ledger service]]

## Cards (7)
- [[correctness-dedup-window]]
- [[correctness-idempotency-concurrent-retries]]
- [[correctness-idempotency-key-design]]
- [[correctness-idempotency-partial-failure]]
- [[correctness-idempotency-payload-hash]]
- [[correctness-idempotency-response-replay]]
- [[correctness-idempotent-consumer-patterns]]
%% trellis:end %%

## Notes
