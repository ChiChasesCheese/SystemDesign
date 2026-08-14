---
id: analytics-row-vs-column-layout
node: analytics.olap
type: qa
---
## Q
An analytical query averages one column over 100M rows. Why does a row-store (OLTP) engine do orders of magnitude more I/O than a column store, even with the same data?

## A
A row store lays each row's columns contiguously, so reading one column drags **every other column of every row** through disk and memory — and B-tree indexes don't help a full scan.

A column store lays each **column** contiguously: the query reads only the 1–2 columns it touches, and those columns compress far better (similar values adjacent), often 10x+ — so bytes scanned drops by both column selection *and* compression.

That's the whole OLTP/OLAP split: point reads and updates want rows together; scans and aggregates want columns together.
