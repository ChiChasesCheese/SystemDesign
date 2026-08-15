---
id: distributed-offline-client-writes
node: distributed.replication.multi-leader
type: qa
---
## Q
Why is an offline-capable mobile/desktop app a multi-leader system, and which two schema decisions does that force on you?

## A
Every device has a full local replica that **accepts writes while disconnected** and syncs later — that is exactly multi-leader, with the peculiar property that **replication lag is unbounded** (days, if the phone is in a drawer) and the "leader count" equals the user's device count.

Forced decisions:

- **Client-generated ids** (UUID/ULID, or `(device_id, local_seq)`) — server auto-increment ids can't be assigned offline, and two devices would mint the same one.
- **Mutations as intents, not absolute state** — store `add 2 to quantity` or a CRDT/OT operation rather than `quantity = 5`, so two devices' offline edits both survive the merge.

What stays impossible: **global invariants** (uniqueness, non-negative balance) cannot be checked offline, so those operations must be *provisional locally and confirmed by the server*, with a visible rollback path in the UI.
