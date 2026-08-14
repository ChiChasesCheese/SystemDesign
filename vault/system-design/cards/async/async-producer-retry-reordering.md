---
id: async-producer-retry-reordering
node: async.delivery
type: cloze
---
A Kafka producer with retries enabled and multiple in-flight batches can silently {{c1::reorder writes within a partition}} — batch 1 fails and is retried *after* batch 2 already landed. The fix is the {{c2::idempotent producer}}, whose per-partition sequence numbers let the broker reject out-of-sequence batches, preserving order with up to {{c3::5}} in-flight requests; the old folklore fix of `max.in.flight=1` traded away throughput for the same guarantee.
