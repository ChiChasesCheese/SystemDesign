---
id: distributed-phantoms-predicate-locks
node: distributed.transactions
type: qa
---
## Q
What is a phantom, why can't row locks stop it, and how do databases approximate predicate locks in practice?

## A
A **phantom**: one transaction's write (an insert, or an update moving a row into range) changes the result of another transaction's **search condition** — e.g. two bookings both query "room 101 free 12–1pm?", find no rows, and both insert. Row locks fail because **you can't lock a row that doesn't exist yet**.

- **Predicate locks** — lock the condition itself, check every write against all outstanding predicates — are correct but too expensive.
- Real systems use **index-range (next-key) locks**: lock the index entries covering the searched range, including gaps, so a conflicting insert blocks (InnoDB next-key locking; serializable 2PL generally). No usable index → the lock degrades to the whole table.

Same read-predicate-then-write shape as [[distributed-write-skew]], but on rows that don't exist yet.
