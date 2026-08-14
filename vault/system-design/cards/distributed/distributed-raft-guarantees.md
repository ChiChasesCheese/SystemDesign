---
id: distributed-raft-guarantees
node: distributed.consensus
type: qa
---
## Q
What does Raft actually guarantee about leaders and logs, and what mechanism enforces each guarantee?

## A
- **Election safety**: ≤1 leader per term — each node votes once per term, and a candidate needs a **majority**; two majorities always intersect.
- **Leader completeness**: an elected leader already holds every committed entry — voters **refuse candidates whose log is less up-to-date** than theirs (compare last term, then length), so a majority-committed entry exists on at least one voter of any winning majority.
- **Log matching / state machine safety**: if two logs agree on an entry's index+term, they agree on everything before it (AppendEntries consistency check), so all nodes apply the same commands in the same order.

Consequence worth stating: entries flow only leader → follower; a new leader never overwrites committed entries, only uncommitted divergence.
