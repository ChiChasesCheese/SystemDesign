---
id: correctness-dedup-window
node: correctness.idempotency
type: qa
---
## Q
How long do you retain idempotency keys / dedup records, and what goes wrong at each extreme?

## A
Retention must **exceed the maximum retry horizon** of every client and queue in front of you — including delayed retries from DLQ redrives and mobile clients replaying after days offline. Stripe retains keys ~24h; payment systems with async retries often keep 7–30 days.

- **Too short**: a retry after expiry is treated as new → duplicate charge. This is the silent failure mode.
- **Too long / forever**: unbounded storage, and a hot unique index; mitigate with TTL + moving dedup responsibility to a natural business key (e.g. one charge per `order_id`) which never expires.
