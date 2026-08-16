---
nodes: [async.queues, async.delivery.guarantees, correctness.outbox, correctness.idempotency, reliability.resilience.retries]
tags: [classic, correctness]
---
# Drill: Design a notification service

Every product grows one: push, SMS, and email triggered by events from a
dozen services. It looks like plumbing until you notice that every failure
mode here is visible to the user as a duplicate message at 3 a.m.

**Constraints to state and honor**
- 100M notifications/day, bursty: a marketing send is 20M in ten minutes.
- A user must never receive the same notification twice; a critical alert must never be silently dropped.
- Third-party providers (APNs, a carrier gateway, an email vendor) fail partially, rate-limit you, and occasionally accept and then lose a message.
- Per-user preferences, quiet hours, and a hard cap of N marketing messages per day.

**Grading points**
- The dual-write problem named the moment the design writes to a database and publishes an event ([[correctness-dual-write-problem]]).
- Transactional outbox with a relay, including what the relay does after it crashes between send and mark-sent ([[correctness-outbox-mechanism]], [[correctness-outbox-relay-lag]], [[correctness-outbox-cleanup]]).
- The event payload decided deliberately — identifier versus full state — and the consequence for consumer coupling ([[correctness-outbox-event-payload]]).
- At-least-once delivery accepted, with dedup pushed to the consumer and a stated dedup window ([[async-delivery-semantics-cloze]], [[correctness-idempotent-consumer-patterns]], [[correctness-dedup-window]]).
- Idempotency key designed from the event, not generated at send time, so a retry collapses ([[correctness-idempotency-key-design]], [[correctness-idempotency-concurrent-retries]]).
- Retries with exponential backoff and jitter, honoring provider-supplied backoff, with a total deadline rather than infinite hope ([[reliability-server-driven-backoff]], [[reliability-retryable-errors]], [[reliability-deadline-propagation]]).
- Retry storms recognised as an amplifier, and the budget or circuit that contains them ([[reliability-retry-storm]], [[async-retry-delay-implementation]]).
- Poison messages to a dead-letter queue with an operator path back, not a silent drop ([[async-dlq-poison-pill]]).
- Priority separated by queue: the marketing burst must not delay a two-factor code ([[async-queue-backpressure]], [[async-broker-selection]]).

**Attempt log**
- [ ] Attempt 1 (date, 40 min, self-graded notes):
