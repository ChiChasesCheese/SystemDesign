---
id: distributed-or-set
node: distributed.crdt
type: qa
---
## Q
Replicated set: replica A removes element x while replica B concurrently re-adds x. Why do naive sets and 2P-Sets get this wrong, and how does an OR-Set resolve it?

## A
- **Naive set**: add/remove don't commute, so replicas that see them in different orders diverge — no well-defined answer.
- **2P-Set**: removals go to a tombstone set that wins forever — once removed, x can **never be re-added**.
- **OR-Set (observed-remove)**: every add attaches a **unique tag**; remove deletes only the tags the remover had *observed*. B's concurrent re-add carries a fresh tag A never saw, so it survives the merge — **add wins over concurrent remove**, and re-adding after removal works.

Cost: tag/tombstone metadata grows with operations and needs eventual compaction. LWW-element-sets avoid the metadata but inherit timestamp data loss ([[distributed-lww-danger]]).
