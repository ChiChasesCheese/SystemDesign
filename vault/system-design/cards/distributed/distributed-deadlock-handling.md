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
