---
id: reliability-data-residency-conflict
node: reliability.multi-region
type: qa
---
## Q
Data residency law says EU user data stays in the EU, but your DR plan fails everything over to us-east. How do these conflict, and what architecture resolves it?

## A
Residency caps where data may be **replicated** — you cannot fail EU data over to a US region, so a global active-passive design is illegal for that data, and residency shrinks your failure-domain choices.

Standard resolution: **partition by user home region** —

- Each user's data lives and replicates **only within its jurisdiction** (e.g. two EU regions for EU users) — failover stays in-boundary.
- A thin **global layer** (routing/directory metadata, nothing personal) sends each request to the user's home partition.
- Accept the trade: an EU user traveling in the US eats cross-ocean latency; that's the compliance cost, not a bug.
