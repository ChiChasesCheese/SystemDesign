---
id: async-eos-sink-determinism
node: async.delivery.exactly-once
type: qa
---
## Q
A Flink job runs with exactly-once checkpointing and writes each result to Postgres. What are the only two sink designs that make the end-to-end result exactly-once, and what silently breaks both?

## A
On recovery the job rewinds to the last checkpoint and **re-emits** everything after it, so the sink must absorb the replay:

- **Idempotent sink** — an upsert on a deterministic primary key (e.g. `(entity_id, window_end)` or `(topic, partition, offset)`), so a re-applied write converges. Cheapest and the usual answer.
- **Two-phase-commit sink** — write into an open sink transaction, *pre-commit* on checkpoint barrier, *commit* only when the checkpoint is confirmed complete; on restart, re-open and commit pending transactions by a recoverable transaction id. Fragile in practice: the sink's transaction timeout must exceed your longest checkpoint interval + recovery, or the pre-committed data is silently rolled back.

What breaks both: **non-determinism in the replayed path** — `uuid4()` keys, `now()` in the key or payload, or ordering that depends on arrival — because the replay then produces *different* rows instead of overwriting the old ones. Sinks with no key and no transaction (append-only HTTP calls, emails, payment APIs) can never be more than at-least-once without their own idempotency key.
