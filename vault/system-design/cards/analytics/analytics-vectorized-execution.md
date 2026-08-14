---
id: analytics-vectorized-execution
node: analytics.olap
type: qa
---
## Q
What is vectorized execution, and what cost of the classic row-at-a-time (Volcano) model does it eliminate?

## A
Operators process **batches of a few thousand column values at a time** (a "vector") instead of pulling one row through the whole operator tree per `next()` call.

That kills the Volcano model's overhead: one virtual function call and branch per row per operator, terrible CPU cache behavior. Vectors sized to fit **L1/L2 cache** are processed in tight loops the compiler turns into **SIMD** instructions — one instruction operating on many values.

Result: analytical engines (DuckDB, ClickHouse, Snowflake) are CPU-efficient enough that scans are often bound by decompression bandwidth, not per-row bookkeeping.
