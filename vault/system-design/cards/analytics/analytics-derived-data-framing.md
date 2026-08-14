---
id: analytics-derived-data-framing
node: analytics.derived
type: qa
---
## Q
What distinguishes a "system of record" from "derived data", and why does the distinction change how you operate each?

## A
- **System of record**: the authoritative first write; if it's lost, the data is gone. Must be durable, transactional, carefully protected.
- **Derived data**: any transformation of it — caches, search indexes, materialized views, warehouse tables, ML features. Lost or corrupted? **Recompute it from the source.**

Operational consequences: derived stores can be rebuilt at will (so schema/mapping changes are cheap — build new, swap), can be eventually consistent, and there can be many of them, each shaped for one read pattern. Trouble starts when a store's role is ambiguous — nobody knows if it can be safely dropped and rebuilt. Related: [[storage-search-not-sot]].
