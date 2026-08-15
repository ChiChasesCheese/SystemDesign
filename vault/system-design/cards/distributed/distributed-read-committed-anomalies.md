---
id: distributed-read-committed-anomalies
node: distributed.transactions.isolation
type: qa
---
## Q
Give a concrete anomaly that read committed permits but repeatable read/snapshot isolation prevents, and one that *both* permit.

## A
**RC permits read skew (non-repeatable read).** Accounts A and B hold $500 each. Your report reads A ($500), a transfer of $100 A→B commits, then your report reads B ($600) — it reports $1100, money that never existed. RC takes a **new snapshot per statement**, so a multi-statement read sees a moving world; SI takes one snapshot for the whole transaction and reports $1000. Same bug class breaks backups and analytical queries, which is why they run at RR/SI.

**Both permit lost update.** `SELECT counter` → app adds 1 → `UPDATE counter = 6`; two sessions do it concurrently and one increment vanishes. Fixes: an atomic write (`UPDATE ... SET n = n + 1`), an explicit `SELECT ... FOR UPDATE`, or compare-and-set on a version column. (Postgres RR does detect this particular one and aborts; MySQL RR does not.)

Interview framing: RC's guarantee is only "no dirty reads/writes" — it says nothing about a transaction seeing a *consistent* database.
