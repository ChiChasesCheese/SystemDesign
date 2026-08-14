---
id: distributed-multi-leader-fit
node: distributed.replication
type: qa
---
## Q
When is multi-leader replication the right call despite its conflict problem, and what are the main conflict-resolution options?

## A
Right call when writes must be accepted in **multiple locations independently**: multi-region apps writing locally (cross-region RTT too high for one leader), offline-capable clients (calendar/notes apps), collaborative editing.

Conflicts are inherent — the same key can be written concurrently on two leaders:
- **LWW (last-write-wins)** — simple, but silently drops one write and trusts clocks.
- **CRDTs / mergeable types** — counters, sets, text that merge deterministically.
- **App-level resolution** — keep siblings and merge on read, or route conflicts to custom logic.

Best mitigation: partition so each record has a **home leader** (e.g. user's region), making conflicts rare by construction.
