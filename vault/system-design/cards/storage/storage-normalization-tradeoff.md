---
id: storage-normalization-tradeoff
node: storage.relational.operations
type: qa
---
## Q
Normalized vs denormalized schema: what exactly does each optimize, and what breaks when you denormalize?

## A
- **Normalized**: every fact stored **once** (many-to-one refs by ID). Optimizes writes and integrity — an update touches one row, no risk of divergent copies. Reads pay with joins.
- **Denormalized**: copies of data placed where they're read (author name embedded in each post). Optimizes **read locality** — one fetch, no joins. Writes now must find and update **every copy**, usually without a transaction spanning them; miss one and copies silently disagree.

Modern resolution: keep the system of record normalized; generate denormalized **derived views** (caches, search docs, read models) from its change stream, accepting eventual consistency there — see [[analytics-derived-data-framing]].
