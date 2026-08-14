---
id: distributed-read-your-writes
node: distributed.consistency
type: qa
---
## Q
A user saves their profile, refreshes, and sees the old version (read hit a lagging replica). Name the missing guarantee and three ways to provide it without making all reads strong.

## A
**Read-your-writes (read-after-write) consistency** — a session-level guarantee, weaker than linearizability.

- **Route the writer's reads to the leader** for data they may have modified (or for N seconds after their last write).
- **Session token / monotonic timestamp**: client carries the LSN/version of its last write; a replica serves the read only if it has caught up to it (else wait or forward).
- **Client-side echo**: update local/app cache with the written value and serve the user's own view from it.

Scope it to the session — other users seeing the update a second late is usually fine.
