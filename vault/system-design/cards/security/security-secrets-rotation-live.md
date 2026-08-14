---
id: security-secrets-rotation-live
node: security.authz
type: qa
---
## Q
How do you rotate a database password or a JWT signing key without restarting services or dropping a single request?

## A
Never flip atomically — rotate with an **overlap window** where two versions are valid:

- **Consumed secrets** (DB passwords): create the new credential *alongside* the old (two-user or dual-password scheme), let clients hot-reload it (watch the secret mount / re-fetch on auth failure / short Vault leases that force re-fetch), then revoke the old only after telemetry shows zero use.
- **Signing keys**: publish old + new public keys in JWKS with `kid`s; **sign with new, verify with both** until every token signed by the old key has expired, then drop it.

Design rule: any service that can only read its secrets at boot has made rotation an outage — build reload in from day one.
