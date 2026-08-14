---
id: storage-mvcc-vacuum
node: storage.relational
type: qa
---
## Q
Postgres MVCC: what physically happens on `UPDATE`, and what operational problem does that create at high churn?

## A
Nothing is overwritten: `UPDATE` writes a **new row version** and marks the old one with the updating transaction's ID; each snapshot sees the versions visible to it. That's how readers never block writers.

Problem: dead versions accumulate as **bloat** — tables and indexes grow, scans wade through dead tuples, and **vacuum** must reclaim them. At high update churn, vacuum falling behind means degrading performance and, in the extreme, transaction-ID wraparound forcing an emergency shutdown.

Interview-grade mitigations: tune autovacuum aggressively on hot tables, keep long-running transactions off the primary (they pin old versions), and prefer HOT updates (don't index the churning column).
