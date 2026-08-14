---
id: storage-search-sync
node: storage.search
type: qa
---
## Q
How do you keep Elasticsearch/OpenSearch in sync with the primary database, and why is "write to both from the app" the wrong answer?

## A
Dual writes from the app have **no transaction spanning both stores**: a crash or failed second write leaves them silently diverged, and retries can reorder updates.

Standard answer: **CDC** — tail the DB's WAL/binlog (Debezium → Kafka → indexer) so the DB stays the single source of truth and the index is a derived, eventually consistent view; ordering per key comes from the log. Complement with periodic **full reindex/backfill** to heal drift and handle mapping changes (build a new index, then alias-swap).
