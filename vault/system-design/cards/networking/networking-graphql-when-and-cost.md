---
id: networking-graphql-when-and-cost
node: networking.api-styles
type: qa
---
## Q
What client situation makes GraphQL earn its complexity, and what two operational problems does it import?

## A
Earns it when **many diverse clients need different slices of the same graph** (mobile vs web vs partners) — clients query exactly the fields they need, killing over-/under-fetching and per-client backend endpoints (BFFs).

Costs:
- **Caching gets hard**: everything is a POST to one endpoint, so HTTP/CDN caching no longer works for free.
- **Unbounded query cost**: clients can write pathological nested queries — you must add depth/complexity limits and solve N+1 with dataloaders.
