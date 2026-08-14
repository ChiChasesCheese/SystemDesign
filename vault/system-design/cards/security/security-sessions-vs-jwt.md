---
id: security-sessions-vs-jwt
node: security.authn
type: qa
---
## Q
Server-side sessions vs JWTs: what does each trade away, and which one makes "log out this user now" hard?

## A
- **Sessions**: opaque id, state in a server store (Redis/DB). Instant revocation — delete the row — but every request costs a store lookup, and the store is shared infrastructure to scale.
- **JWTs**: claims signed into the token; any service verifies locally, no lookup, great for cross-service auth. But they are valid until expiry — **revocation is the hard part**: you need short lifetimes plus a denylist or key rotation, which quietly reintroduces the server-side state JWTs promised to remove.
