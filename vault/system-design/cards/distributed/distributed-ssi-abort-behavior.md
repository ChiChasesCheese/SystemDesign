---
id: distributed-ssi-abort-behavior
node: distributed.transactions.concurrency-control
type: qa
---
## Q
Your Postgres app moves to `SERIALIZABLE` and starts throwing 40001 errors under load. What is SSI doing, and what are the levers?

## A
SSI never blocks; it tracks each transaction's **read set** (SIRead predicate locks) and aborts a transaction when a dangerous read-write dependency structure appears. Two properties to state:

- **Aborts are conservative** — the structure is a *potential* cycle, so SSI produces **false positives**: transactions that were actually serializable still get aborted. The rate climbs superlinearly with contention, and long-running transactions widen the window during which conflicts can be discovered.
- **Predicate-lock memory is finite**: when a transaction's read set exceeds the tracking budget (`max_pred_locks_per_transaction`), locks **escalate from tuple to page to relation granularity**, which coarsens the tracking and *increases* false aborts. Big sequential scans under SERIALIZABLE are self-defeating.

Levers: a **retry loop with backoff on 40001** (mandatory — it is a normal outcome, not an error); keep transactions short and read sets narrow (index them so they don't scan); mark long analytics as `READ ONLY DEFERRABLE`, which waits for a safe snapshot and can then never abort or cause aborts; and if contention is genuinely on hot rows, switch that path to explicit pessimistic locking instead.

## Q zh
可序列化快照隔离（SSI）如何检测冲突并回滚事务？

## A zh
SSI（在 PostgreSQL 中）使用**依赖追踪**而不是锁：
1. 每个事务维护读集（看到的行）和写集（修改的行）。
2. 事务T1提交时，系统检查任何**并发读者**是否依赖 T1 的写入（T1 修改了他们读的内容）。
3. 如果发现冲突的依赖，一个事务被标记为**冲突**并且失败/回滚。
4. 应用重试。

优点：不像两阶段锁那样阻塞；可序列化没有幻读。缺点：应用必须处理回滚和重试。
