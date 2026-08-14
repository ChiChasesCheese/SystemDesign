---
id: foundations-clarifying-questions-worth-asking
node: foundations.method
type: qa
---
## Q
Interviewer says "design X" with no details. Which clarifying questions actually change the design (vs filler)?

## A
Questions whose answers select an architecture:

- **Read/write ratio** — decides caching and replication strategy.
- **Scale** (DAU, data size) — one box vs sharded fleet.
- **Consistency vs availability priority** — e.g. can a user briefly see stale data?
- **Latency-sensitive paths** — which operations must be fast vs can be async.

Filler: questions about UI details or features you'd scope out anyway.
