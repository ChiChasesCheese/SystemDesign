---
id: storage-search-not-sot
node: storage.search
type: qa
---
## Q
Why is a search cluster the wrong system of record, even though it stores full documents?

## A
- **No real transactions or strong consistency**: writes become visible only after a refresh (near-real-time, ~1s), and multi-document updates aren't atomic.
- **Rebuildability is the design assumption**: mapping changes, analyzer changes, and version upgrades routinely require a full reindex — trivial if the truth lives elsewhere, catastrophic if it doesn't.
- Durability and dedup/versioning stories are weaker than a proper database's.

Treat search as a **derived view**: source of truth in the DB, index rebuilt from it at will.
