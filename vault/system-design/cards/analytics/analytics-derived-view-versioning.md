---
id: analytics-derived-view-versioning
node: analytics.derived
type: qa
---
## Q
A bug shipped in the transformation logic behind a derived table that consumers query in production. What's the safe repair pattern?

## A
**Build v2 side-by-side, then swap** — never patch in place:

1. Fix the logic, run it as a new derived view from the retained log / raw source, writing to a separate table or index.
2. Let it catch up to the live position; validate against v1 (row counts, spot diffs).
3. Atomically repoint consumers (alias swap, view redefinition, config flip) and keep v1 briefly for rollback.

This works only because inputs are immutable and the view is recomputable — the same property behind [[analytics-idempotent-reruns]] and search's reindex-then-alias-swap. In-place patching risks serving a half-fixed view and leaves no rollback.
