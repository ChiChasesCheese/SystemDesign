---
id: distributed-phantoms-predicate-locks
node: distributed.transactions.isolation
type: qa
---
## Q
What is a phantom, why can't row locks stop it, and how do databases approximate predicate locks in practice?

## A
A **phantom**: one transaction's write (an insert, or an update moving a row into range) changes the result of another transaction's **search condition** — e.g. two bookings both query "room 101 free 12–1pm?", find no rows, and both insert. Row locks fail because **you can't lock a row that doesn't exist yet**.

- **Predicate locks** — lock the condition itself, check every write against all outstanding predicates — are correct but too expensive.
- Real systems use **index-range (next-key) locks**: lock the index entries covering the searched range, including gaps, so a conflicting insert blocks (InnoDB next-key locking; serializable 2PL generally). No usable index → the lock degrades to the whole table.

Same read-predicate-then-write shape as [[distributed-write-skew]], but on rows that don't exist yet.

## Q zh
什么是幻读？谓词锁如何防止它？

## A zh
**幻读**：事务重复相同的范围查询但得到不同的行数，因为另一个事务在该范围内插入了。例如：BEGIN; SELECT * FROM users WHERE age > 18; ... (另一个事务插入 age 21 的用户) ... SELECT * FROM users WHERE age > 18; 返回不同的行。

**谓词锁**：lock 不是单个行而是查询谓词（age > 18）。如果事务声明对该范围感兴趣，插入必须检查是否冲突。实现困难：需要跟踪所有活跃谓词并在插入时检查。大多数数据库改用范围锁或重复读隔离级别（MVCC）。
