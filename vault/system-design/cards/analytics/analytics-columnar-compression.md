---
id: analytics-columnar-compression
node: analytics.olap
type: qa
---
## Q
Name the two compression tricks that make columnar storage so effective, and why sorting the column first multiplies their effect.

## A
- **Dictionary encoding**: replace repeated values with small integer codes (a `country` column becomes 1–2 bytes per row).
- **Run-length / bitmap encoding**: store "value X repeats N times" or one bitmap per distinct value — a bitmap over a low-cardinality column also turns `WHERE` predicates into fast bitwise AND/ORs.

Sorting first puts equal values **adjacent**, turning millions of rows into a handful of runs. The catch: you only get one sort order per copy, so systems keep the sort key aligned with the most common filter (or store multiple sort orders across replicas).
