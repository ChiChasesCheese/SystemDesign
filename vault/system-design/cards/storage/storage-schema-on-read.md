---
id: storage-schema-on-read
node: storage.nosql
type: qa
---
## Q
"Schemaless" document stores still have a schema. Where does it live, and when is schema-on-read genuinely better than schema-on-write?

## A
It's **implicit in the reading code** (schema-on-read): the database enforces nothing, so every consumer must handle every historical shape ever written. Schema-on-write (relational DDL) enforces one shape at insert time.

Schema-on-read wins when:
- Records are **genuinely heterogeneous** (per-integration payloads, user-defined fields) — a fixed schema would be a sparse mess of nullable columns.
- Shape is dictated by **external systems** you don't control.
- Evolution: new fields just appear — no migration step; readers use defaults for old records.

The trade: relational `ALTER TABLE` is a one-time explicit migration (fast in Postgres — metadata-only for nullable adds); schema-on-read smears that migration across all reading code **forever**.
