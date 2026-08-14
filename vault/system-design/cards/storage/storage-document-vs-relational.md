---
id: storage-document-vs-relational
node: storage.nosql
type: qa
---
## Q
When does a document store (MongoDB-style) genuinely beat relational, and what access pattern signals you chose wrong?

## A
Document wins when data is naturally an **aggregate read/written as a unit** — the whole document loads in one op, schema varies per record, and locality beats joins (e.g. a product page, a user profile with embedded settings).

Warning signs you chose wrong: queries that constantly reach **across** documents (many-to-many relationships, cross-entity analytics) — you end up doing joins in application code, or duplicating data and hand-rolling consistency.

Note the gap has narrowed: Postgres `jsonb` covers many "flexible schema" cases inside a relational engine.
