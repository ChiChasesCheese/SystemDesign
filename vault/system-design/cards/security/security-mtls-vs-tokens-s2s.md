---
id: security-mtls-vs-tokens-s2s
node: security.authz
type: qa
---
## Q
For service-to-service auth, mTLS and signed tokens (JWTs) are often used *together*. What does each prove that the other cannot?

## A
- **mTLS** proves **workload identity at the channel level**: "this connection really is from billing-service" (cert issued via SPIFFE/mesh CA), plus encryption. But it says nothing about the individual request — every request on the pipe looks the same.
- **Tokens** carry **per-request claims**: which end user this call is on behalf of, scopes, audience, expiry. But a token alone doesn't authenticate the channel and can be replayed if exfiltrated.

So: mTLS answers *"which service is calling?"*, tokens answer *"with what authority, for whom, for this request?"*. Deep systems need both — see [[security-confused-deputy]] for why service identity alone is insufficient.
