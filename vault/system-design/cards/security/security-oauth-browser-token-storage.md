---
id: security-oauth-browser-token-storage
node: security.authn.oauth
type: qa
---
## Q
Why was the implicit flow deprecated, and — since code+PKCE replaced it — where should an SPA keep the resulting tokens in 2026?

## A
**Implicit died** because it returned the access token in the **URL fragment**: it leaked into browser history, referrers, logs and extensions; it was unbound (no PKCE, no client authentication, so a token could be injected from another flow); and it could not issue refresh tokens, forcing either long-lived access tokens or hidden-iframe renewals that third-party cookie blocking has since killed.

PKCE fixes *code interception*, not *token custody* — the SPA still ends up holding a bearer token in JS, where any XSS or compromised npm dependency exfiltrates it.

The 2026 default is the **BFF (backend-for-frontend)**: a server-side component runs the code+PKCE exchange, keeps access/refresh tokens server-side, and gives the browser only an `HttpOnly; Secure; SameSite` session cookie, proxying API calls. If tokens must live in the browser, the minimum bar is: in-memory only (never `localStorage`), short access-token TTL, **rotating refresh tokens with reuse detection**, and ideally sender-constrained (DPoP) tokens so a stolen one is not replayable.
