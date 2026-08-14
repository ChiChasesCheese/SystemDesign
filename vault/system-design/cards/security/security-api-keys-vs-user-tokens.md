---
id: security-api-keys-vs-user-tokens
node: security.authz
type: qa
---
## Q
API keys vs user tokens: what does each identify, and why must a multi-tenant API never authorize on the key alone?

## A
- **API key**: identifies an **application/tenant** — long-lived, no user context, ideal for server-to-server calls, metering, and rate limiting per customer. Store only a hash; support rotation with overlapping validity.
- **User token** (OAuth access token): identifies a **user (and scopes)** — short-lived, carries the actual authority to act on that user's data.

A key alone tells you *who is calling*, not *on whose behalf*. Authorizing tenant-scoped data by key without checking the acting user's rights is the classic **confused deputy** / BOLA vulnerability.
