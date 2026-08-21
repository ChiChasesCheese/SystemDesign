---
id: distributed-deadlock-handling
node: distributed.transactions.concurrency-control
type: qa
---
## Q
Under 2PL, what makes the deadlock rate explode, how do engines resolve deadlocks, and what do you change in the application?

## A
Rate scales viciously: deadlock frequency grows roughly with **concurrency squared and transaction length to the fourth power**, divided by the number of distinct lockable items (Gray's classic estimate). Practical reading: doubling the statements inside a transaction hurts ~16x more than doubling the number of clients — **long transactions are the problem**, not load.

Resolution, two families:

- **Detection**: build the waits-for graph, find a cycle, kill the cheapest victim (InnoDB's detector; it can be disabled at very high concurrency, falling back to `innodb_lock_wait_timeout`, default 50 s). Victim gets a retryable error.
- **Prevention by priority**: order transactions by start timestamp and never let a cycle form — **wound-wait** (older transaction wounds the younger holder) or wait-die; CockroachDB and Spanner-style systems use this, since a distributed waits-for graph is expensive to build.

Application fixes: acquire locks in a **consistent global order** (sort ids before updating), shorten transactions (never hold a lock across an RPC or user think-time), and make every write path **retryable and idempotent**.

## Q zh
分布式死锁是什么，怎样检测和打破？

## A zh
**死锁**：两个或多个事务互相等待彼此持有的锁，形成环形依赖（A 等待 B 的锁，B 等待 A 的锁）。

**检测**：全局等待图（wait-for graph）：追踪所有事务和锁的依赖关系，检测环。超时检测：事务如果超过阈值时间未获得锁，假设发生死锁。

**打破**：**中止最小代价的事务**：选择回滚对工作最小的事务（by 日志大小或已执行操作数）。**超时中止**：设置锁等待超时，超时自动中止事务。

权衡：精确检测成本高，超时检测可能误杀无死锁的事务。
