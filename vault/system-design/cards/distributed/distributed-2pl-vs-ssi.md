---
id: distributed-2pl-vs-ssi
node: distributed.transactions.concurrency-control
type: qa
---
## Q
Two-phase locking vs serializable snapshot isolation — how does each achieve serializability, what does each cost, and when does each win?

## A
- **2PL (pessimistic)**: acquire shared locks to read, exclusive to write, hold **all** locks until commit. Readers block writers and vice versa; cost = deadlocks (detected → abort) and terrible latency variance when anything queues behind a long transaction.
- **SSI (optimistic)**: run everything on an MVCC snapshot without blocking; track **read-write dependencies** between concurrent transactions and, at commit, abort one whenever a dangerous structure (potential cycle) appears. Cost = abort-and-retry work, which explodes under contention.

Choose 2PL-style pessimism when conflicts are frequent (hot rows — retrying is wasted work); SSI when the workload is mostly reads or conflicts are rare. Postgres `SERIALIZABLE` is SSI; classic SQL Server serializable is 2PL.

## Q zh
2PL 和 SSI 在锁和冲突检测上有什么区别？

## A zh
**2PL**（Two-Phase Locking）：事务在读或写数据时立即获取锁，持有到事务结束，防止并发冲突。写阻塞读，读阻塞写——高锁竞争。

**SSI**（Serializable Snapshot Isolation）：事务在快照上乐观执行，无锁获取，完成后检测是否有其他事务的冲突（reads/writes 依赖关系）。只有冲突时才中止并重试。高并发下低延迟，但需要重试开销。
