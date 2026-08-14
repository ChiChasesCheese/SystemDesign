---
id: async-event-sourcing-vs-cdc
node: async.streaming
type: qa
---
## Q
Event sourcing and CDC both give you "a stream of changes." What is the fundamental distinction, and when do you pick each?

## A
- **Event sourcing**: domain events (`OrderCancelled`) are the **source of truth**, written first, expressing *intent*; current state is a derived projection. The application must be designed around it — replay, versioned event schemas, projections.
- **CDC**: the mutable database stays the source of truth; the stream is a **derived byproduct** of row changes (`UPDATE orders SET status=...`), capturing *effect* without intent, and leaking the table schema as your public contract.

Pick CDC to bolt streaming onto an **existing** CRUD system with zero app changes; pick event sourcing when the domain needs **intent-level history and audit** (ledgers, workflow). Middle path: keep CRUD + publish explicit events via an outbox ([[correctness-outbox-mechanism]]).
