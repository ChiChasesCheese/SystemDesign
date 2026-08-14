---
id: security-oauth-code-pkce
node: security.authn
type: qa
---
## Q
In the OAuth2 authorization code flow, why does the client exchange a code instead of receiving tokens directly in the redirect — and what does PKCE add?

## A
The redirect travels through the **browser** (URL, history, referrers, extensions) — an untrusted channel. The short-lived, one-time **code** is useless there because tokens are only issued on a direct **back-channel** call from the client to the token endpoint.

**PKCE** binds the code to whoever started the flow: the client sends a hash of a random verifier up front and must present the verifier at exchange, so an intercepted code can't be redeemed. Mandatory for public clients (SPAs, mobile) with no client secret — and now recommended for all clients (OAuth 2.1 default).
