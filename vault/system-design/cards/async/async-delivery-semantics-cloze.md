---
id: async-delivery-semantics-cloze
node: async.delivery.guarantees
type: cloze
---
Delivery semantics follow from when you ack: acking **before** processing gives {{c1::at-most-once}} (crash loses the message), acking **after** processing gives {{c2::at-least-once}} (crash causes redelivery), and "exactly-once" in practice means {{c3::at-least-once delivery plus idempotent (deduplicating) processing}}.
