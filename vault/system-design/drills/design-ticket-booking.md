---
nodes: [distributed.transactions.isolation, distributed.transactions.concurrency-control, correctness.saga, storage.relational.indexing, traffic.rate-limiting]
tags: [classic, correctness]
---
# Drill: Design seat booking

Sell 60,000 seats for one concert to 2 million people who all arrive at
10:00:00. Double-selling a seat is unacceptable; so is a queue that
appears to have sold out while seats sit in abandoned carts.

**Constraints to state and honor**
- One seat, one buyer. No overselling under any interleaving.
- Seats are held for 10 minutes during checkout, then released automatically.
- Payment is an external call that can succeed slowly, fail, or time out ambiguously.
- The 10:00 spike is 100× the steady-state rate and lasts three minutes.

**Grading points**
- The isolation level named, and the anomaly it does and does not prevent — read committed is not enough here ([[distributed-isolation-anomalies]], [[distributed-read-committed-anomalies]], [[distributed-repeatable-read-dialects]]).
- Write skew identified as the failure mode for "count the free seats, then insert", and why it survives snapshot isolation ([[distributed-write-skew]], [[distributed-phantoms-predicate-locks]]).
- A concrete mechanism chosen: a unique constraint on (event, seat), `SELECT … FOR UPDATE`, or serializable isolation with retry — with the cost of each ([[distributed-2pl-vs-ssi]], [[distributed-ssi-abort-behavior]], [[distributed-mvcc-defaults]]).
- Deadlock behavior anticipated when two carts grab overlapping seats in different orders ([[distributed-deadlock-handling]]).
- The hold as a state with an expiry, reclaimed by a sweeper that is safe to run twice ([[distributed-mvcc-visibility]], [[correctness-idempotency-key-design]]).
- Booking and payment as a saga with a real compensation, and the compensation's limits stated — a refund is not an undo ([[correctness-saga-orchestration-choreography]], [[correctness-saga-compensation-limits]], [[correctness-saga-vs-2pc]]).
- The saga's isolation gap acknowledged: another user can see intermediate state mid-saga ([[correctness-saga-isolation]], [[correctness-saga-compensation-race]]).
- An ambiguous payment timeout resolved by idempotency key and status query, never by retrying blind ([[correctness-idempotency-partial-failure]], [[correctness-idempotency-response-replay]]).
- Indexes chosen for the hot query, with the write cost of each index acknowledged at 100× load ([[storage-index-selectivity]], [[storage-covering-index]], [[storage-index-write-cost]]).
- The spike absorbed by a waiting room and per-user limits rather than by hoping the database holds ([[traffic-rate-limiting-vs-load-shedding]], [[traffic-shedding-response]], [[traffic-rate-limit-key-choice]]).

**Attempt log**
- [ ] Attempt 1 (date, 45 min, self-graded notes):
