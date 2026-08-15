---
id: security-oauth-grant-selection
node: security.authn.oauth
type: qa
---
## Q
Pick the grant: (a) a nightly batch job calling a partner API, (b) a web app acting for a signed-in user, (c) a smart TV app. What makes (a) fundamentally different from the others?

## A
- (a) **Client credentials** — the app authenticates *as itself* with a secret or (better) mTLS / signed JWT assertion.
- (b) **Authorization code + PKCE** — a user is present and consents to delegation.
- (c) **Device authorization grant** — the TV shows a code, the user completes the flow on a phone, and the device polls the token endpoint.

The difference: client credentials has **no resource owner**. The token carries no `sub` for a human and no consent, so the resource server must authorize on the **client's** identity and scopes, and any per-user data access has to be constrained some other way (tenant-scoped credentials, an explicit `act`/on-behalf-of exchange). Treating a client-credentials token as "some user" is how batch jobs end up with cross-tenant reach.

Two anti-patterns: using client credentials from a browser or mobile app (a **public client** cannot hold a secret — use code+PKCE), and password grant (ROPC), which is removed in OAuth 2.1 because it hands your credentials to the client and cannot do MFA or federation.
