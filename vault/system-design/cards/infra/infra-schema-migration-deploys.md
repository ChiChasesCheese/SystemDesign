---
id: infra-schema-migration-deploys
node: infra.delivery
type: qa
---
## Q
Why are database schema changes the riskiest class of deploy, and how does expand–contract make them safe?

## A
Two reasons: during any rolling or canary deploy, **old and new code run against the same schema simultaneously**; and destructive migrations (drop, rename, type change) **cannot be rolled back** — the data is gone.

Expand–contract at the schema level:
1. **Expand**: additive-only change (new nullable column / new table) that old code safely ignores.
2. **Migrate**: ship code that dual-writes, backfill old rows asynchronously, then switch reads to the new shape.
3. **Contract**: drop the old column in a *later* deploy, only after telemetry shows nothing reads it.

Rule: every migration must be compatible with the code version before *and* after it — never couple a destructive migration to the code deploy that wants it.
