---
id: analytics-idempotent-reruns
node: analytics.batch
type: qa
---
## Q
Why are batch jobs designed so the whole run can be thrown away and re-executed, and what two properties of the job make that safe?

## A
Because failure handling *and* bug recovery both become "just run it again": a crashed job, a bad deploy, or a logic error discovered next week are all fixed by rerunning over the unchanged input. DDIA calls this **human fault tolerance** — the cheapest recovery story in data engineering.

Required properties:
- **Immutable inputs**: the job never mutates its source; it reads raw data and writes elsewhere.
- **Deterministic, atomically-published outputs**: same input → same output, made visible in one atomic step (temp dir + rename, or overwrite a whole partition / table-format snapshot commit) so partial output from a failed attempt is never observed and reruns replace rather than double-count.
