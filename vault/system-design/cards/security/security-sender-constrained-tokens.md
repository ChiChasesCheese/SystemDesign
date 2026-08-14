---
id: security-sender-constrained-tokens
node: security.authn
type: qa
---
## Q
What weakness do bearer tokens have by construction, and how do sender-constrained tokens (DPoP, mTLS-bound) fix it?

## A
A **bearer** token authorizes *whoever holds it* — exfiltrate it (logs, XSS, compromised proxy) and it replays perfectly until expiry.

**Sender-constrained** tokens bind the token to a key only the legitimate client holds:

- **DPoP**: client generates a keypair; the token is bound to the public key, and every API call carries a short-lived signed proof (covering method + URL + timestamp). A stolen token without the private key is useless.
- **mTLS-bound**: token is bound to the client certificate's thumbprint; the API checks the TLS client cert matches.

Used where token theft is the top risk: financial-grade APIs (FAPI), high-value service credentials. Cost: key management and one signature per request.
