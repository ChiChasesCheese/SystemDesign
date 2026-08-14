---
id: storage-search-nrt-refresh
node: storage.search
type: qa
---
## Q
In Elasticsearch, a document is indexed successfully but a search doesn't find it for another second. Explain the mechanism — and why durability is a *separate* knob.

## A
Searchability requires a **refresh**: buffered docs are written into a new in-memory **segment** and only then become visible to queries. Refresh runs every 1s by default ("near-real-time") because opening segments per-document would be ruinously expensive.

Durability is independent: every operation is also appended to the **translog** (fsynced by default before acking), so an un-refreshed doc survives a crash — it's durable but not yet searchable.

Levers: lengthen `refresh_interval` (or `-1`) during bulk loads for big ingest speedups; use `?refresh=wait_for` when a workflow must read-its-write; GET-by-ID bypasses refresh entirely.
