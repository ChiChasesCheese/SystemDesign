---
id: distributed-2pl-vs-ssi
node: distributed.transactions
type: qa
---
## Q
Two-phase locking vs serializable snapshot isolation — how does each achieve serializability, what does each cost, and when does each win?

## A
- **2PL (pessimistic)**: acquire shared locks to read, exclusive to write, hold **all** locks until commit. Readers block writers and vice versa; cost = deadlocks (detected → abort) and terrible latency variance when anything queues behind a long transaction.
- **SSI (optimistic)**: run everything on an MVCC snapshot without blocking; track **read-write dependencies** between concurrent transactions and, at commit, abort one whenever a dangerous structure (potential cycle) appears. Cost = abort-and-retry work, which explodes under contention.

Choose 2PL-style pessimism when conflicts are frequent (hot rows — retrying is wasted work); SSI when the workload is mostly reads or conflicts are rare. Postgres `SERIALIZABLE` is SSI; classic SQL Server serializable is 2PL.
