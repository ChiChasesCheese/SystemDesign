---
id: async-materialized-view-refresh
node: async.streaming
type: qa
---
## Q
You keep a denormalized read model (search index, cache, analytics table) fed from a change stream. How do you (a) keep it fresh and (b) fix it when it's wrong?

## A
- **Fresh**: a stream consumer applies each change; freshness = consumer lag, which you monitor as *lag age* (seconds behind), not message count. Writes must be idempotent (upsert keyed by entity id + version) because the stream is at-least-once.
- **Wrong**: don't patch it — **rebuild by replay**: reprocess the log from the start (or from a snapshot) into a new view, then cut reads over. This is the payoff of keeping the log as source of truth: derived data is disposable.
