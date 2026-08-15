---
id: async-dlq-poison-pill
node: async.delivery.guarantees
type: qa
---
## Q
When should a message go to a dead-letter queue, and what two things must you decide about the messages that land there?

## A
Move a message after **N failed attempts with backoff** when the failure is *non-transient* (malformed payload, business rule violation) — retrying a poison pill forever burns capacity and, in ordered/partitioned systems, blocks everything behind it.

Decisions:
- **Ordering**: DLQ'ing a message means later messages for the same key are processed first; you must either tolerate that or park the whole key.
- **Drain policy**: DLQ needs an owner, alerting, and a redrive path (fix + replay) — an unmonitored DLQ is just silent data loss with extra steps.
