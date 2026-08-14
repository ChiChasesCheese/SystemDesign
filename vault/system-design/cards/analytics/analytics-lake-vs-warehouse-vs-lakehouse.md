---
id: analytics-lake-vs-warehouse-vs-lakehouse
node: analytics.warehouse
type: qa
---
## Q
Warehouse vs data lake vs lakehouse — what does each own, and what gap does the lakehouse close?

## A
- **Warehouse** (Snowflake, BigQuery): the engine owns storage *and* format — great SQL performance, transactions, governance; but data is locked to one engine and non-SQL access (ML, Spark) is awkward.
- **Data lake**: raw files (Parquet) in object storage, any engine reads them — cheap and open, but no transactions, no schema enforcement, easy to rot into a "data swamp".
- **Lakehouse**: lake storage + an **open table format** (Iceberg/Delta) adding ACID commits, schema evolution, and time travel — so multiple engines share one governed copy.

The lakehouse closes the gap of choosing between *open/cheap* and *reliable/managed*.
