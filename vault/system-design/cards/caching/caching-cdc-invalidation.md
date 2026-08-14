---
id: caching-cdc-invalidation
node: caching.invalidation
type: qa
---
## Q
Why drive cache invalidation from the database's change stream (CDC/binlog) instead of application code — and what gap remains?

## A
App-side invalidation must be remembered on *every* write path, and it silently fails when an app server crashes between DB commit and cache delete — stale until TTL. Tailing the binlog (Facebook's McSqueal pattern) makes every **committed** write reliably emit an invalidation: one choke point instead of N code paths, at-least-once with replay after consumer failure (deletes are idempotent, so duplicates are free).

Remaining gap: pipeline lag — a reader can re-populate the old value in the window before the invalidation arrives, so you still keep a TTL backstop (or leases, [[caching-lease-cas]]).
