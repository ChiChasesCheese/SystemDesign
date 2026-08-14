---
id: distributed-local-first-limits
node: distributed.crdt
type: qa
---
## Q
A local-first app (Automerge/Yjs-style) writes to the local replica and syncs in the background. What does the server shrink to, and which requirements force real server-side logic back in?

## A
The server shrinks to a **dumb relay + durable store of encrypted ops/states** — it never resolves conflicts, because CRDT merge runs on every client; clients get zero-latency writes, offline operation, and multi-device sync for free ([[distributed-multi-leader-fit]]: this is multi-leader with merge by construction).

Forced back to a coordinating server (or consensus):

- **Global invariants**: unique usernames, seat sold once, balance ≥ 0 — CRDTs converge but can't enforce "at most one".
- **Authoritative side effects**: payments, emails — must happen exactly once, somewhere.
- **Metadata growth**: tombstones/edit history need compaction, and text CRDTs pay per-character metadata.

Interview line: CRDTs remove coordination from *data merging*, not from *invariants*.
