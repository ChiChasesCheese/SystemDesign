---
id: async-kafka-transactions-eos
node: async.delivery.exactly-once
type: qa
---
## Q
How does Kafka achieve exactly-once for a consume-transform-produce pipeline (Kafka Streams), and where does the guarantee stop?

## A
The producer opens a **transaction** that atomically commits both the **output records** and the **input consumer offsets** (offsets are just writes to an internal topic). Crash → transaction aborts → offsets not committed → reprocess and rewrite; downstream consumers with `isolation.level=read_committed` never see aborted records. A stable `transactional.id` + epoch **fences zombie producers** — an old instance's commits are rejected.

The guarantee stops at Kafka's edge: any **external side effect** (HTTP call, email, non-transactional DB write) inside the loop can still happen twice. External sinks need their own idempotent or transactional write ([[async-exactly-once-myth]]).
