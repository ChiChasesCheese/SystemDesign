---
id: distributed-repeatable-read-dialects
node: distributed.transactions.isolation
type: qa
---
## Q
Postgres and MySQL/InnoDB both offer `REPEATABLE READ`. Name three behavioral differences that bite in production.

## A
- **Phantoms**: InnoDB RR blocks them for *locking* reads via next-key (gap) locks; Postgres RR is snapshot isolation — plain reads never see phantoms, but nothing prevents a concurrent insert from breaking an invariant you checked (write skew stays possible in both).
- **Write-write conflicts**: Postgres RR **aborts** the second transaction with `could not serialize access due to concurrent update` (SQLSTATE 40001) — your app *must* have a retry loop. InnoDB instead **blocks on the row lock** and proceeds with the newly committed row, so you get no error and a possibly wrong result.
- **Locking reads see a different world**: in InnoDB, `SELECT ... FOR UPDATE` reads the **latest committed** row, not the transaction's snapshot — so a plain `SELECT` and a `SELECT ... FOR UPDATE` in the same transaction can return different values for the same row. Postgres keeps the snapshot and errors instead.

Takeaway for design docs: "repeatable read" names a *level*, not a behavior — always state the engine, and always write the retry loop.

## Q zh
不同数据库的可重复读隔离级别有何不同？

## A zh
**PostgreSQL 可重复读** — MVCC 快照隔离。事务看到开始时的一致快照。不能看到后来的变化（防止非重复读），但不能看到幻读（范围内的新行）除非...实际上通过 MVCC 防止。

**MySQL 可重复读** — 类似但使用间隔锁捕获范围，部分防止幻读但不完全。

**Oracle 和 SQL Server** — 类似于 PostgreSQL（MVCC）。

关键点：即使都叫可重复读，不同实现通过不同机制（锁 vs MVCC）实现，行为可能不同。
