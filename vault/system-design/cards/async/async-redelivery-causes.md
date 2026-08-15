---
id: async-redelivery-causes
node: async.delivery.guarantees
type: qa
---
## Q
Your consumer code is bug-free and the broker is healthy. Name the concrete events that still cause the same message to be processed twice — and the one that means two consumers run it *at the same time*.

## A
- **Ack/offset commit lost** — you processed, then the ack or commit didn't land (crash, network drop, broker leader change). The broker re-delivers.
- **Lease expiry mid-processing** — SQS visibility timeout elapses, or Kafka `max.poll.interval.ms` is exceeded and the member is evicted. The broker assumes you died and hands the message to **another consumer while yours is still running**: redelivery here is *concurrent*, so idempotency must be race-safe (atomic insert on a unique key), not read-then-check.
- **Rebalance / partition reassignment** between processing and commit — the new owner restarts from the last committed offset.
- **Operational replay** — DLQ redrive, offset reset, or a backfill re-runs a window on purpose.
- **Producer resend after an ambiguous ack** — this one arrives as a *different broker message id* for the same business event, so dedup must key on a **producer-supplied business/event id**, never on the broker's message id or offset.
