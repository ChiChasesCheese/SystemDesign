---
id: caching-cache-warming
node: caching.strategies
type: qa
---
## Q
A new cache cluster (or one recovering from a flush) goes live cold. What happens at cutover, and what are three warming techniques?

## A
Hit rate starts at ~0%, so the database briefly receives the *full* read load it was never provisioned for — the cold-start herd can take it down (the math: [[caching-hit-rate-outage-math]]).

- **Shadow reads**: mirror production read traffic to the new tier for a while before cutover so it fills organically.
- **Preload**: replay a key-popularity log or copy hot entries from the old cluster/a snapshot.
- **Gradual ramp**: shift traffic in percentage steps sized so miss traffic stays inside DB headroom.

Same discipline applies after any mass-expiry event ([[caching-ttl-jitter]]).
