---
id: architecture-expand-contract
node: architecture.discovery
type: qa
---
## Q
You need a breaking API change (rename a field, change semantics) with consumers you don't control deploying on their own schedule. What's the migration pattern?

## A
**Expand and contract** (parallel change):
1. **Expand**: serve both old and new shapes (add the new field/endpoint/version alongside the old; dual-write or translate).
2. **Migrate**: consumers move at their own pace; you track usage of the old shape with metrics per consumer.
3. **Contract**: remove the old shape only when telemetry shows zero callers (then announce, then delete).

Guard the whole thing with **consumer-driven contract tests** (e.g. Pact): each consumer publishes the requests/fields it relies on, and the provider's CI fails before a deploy would break them — turning "did we break anyone?" from archaeology into a test failure.
