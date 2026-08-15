---
id: async-stale-event-ordering
node: async.delivery.guarantees
type: qa
---
## Q
Your handler is idempotent and the topic is keyed by entity, yet a profile occasionally reverts to an old address. Why isn't idempotency enough, and what is the fix?

## A
Per-partition ordering only holds for the **stream as stored**, not for the order your handler *observes*. Any of these re-orders events for one key: a failed message retried after backoff while later messages proceed, a DLQ redrive replayed hours later, a rebalance replaying from an older offset, or concurrent handler threads within one partition. Idempotency makes a repeat harmless; it does not make a **stale** write harmless.

Fixes — make the handler **order-insensitive**, not just repeat-insensitive:
- Carry a monotonic **version/sequence from the source** (row version, LSN, event seq) and apply conditionally: `UPDATE ... WHERE version < :v`. Stale events match zero rows.
- Prefer **commutative** state (set union, max, CRDT-ish counters) over "set to this value".
- If neither is possible, you must **park the whole key** on failure (stop the partition or a per-key queue) rather than skipping ahead — that is the real cost of strict per-key ordering.
