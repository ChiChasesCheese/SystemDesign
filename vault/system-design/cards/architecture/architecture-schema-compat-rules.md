---
id: architecture-schema-compat-rules
node: architecture.discovery
type: qa
---
## Q
You must evolve an event/API schema while old consumers and old producers are still live. Which changes are safe, and which direction of compatibility do you need?

## A
Safe (compatible) changes: **add optional fields with defaults**; never remove, rename, retype, or reuse a field/tag number — deprecate and leave it.

- **Backward compatibility**: new readers handle old data — needed to read history (logs, stored events).
- **Forward compatibility**: old readers tolerate new data (ignore unknown fields) — needed because producers upgrade before consumers (or vice versa) during rolling deploys.
- In a log-based world you effectively need **both** ("full" compatibility), enforced mechanically by a **schema registry** that rejects breaking publishes — not by code review.
