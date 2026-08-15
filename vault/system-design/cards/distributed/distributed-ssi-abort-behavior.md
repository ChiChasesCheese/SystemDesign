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
