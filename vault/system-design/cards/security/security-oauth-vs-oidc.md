---
id: security-oauth-vs-oidc
node: security.authn.oauth
type: qa
---
## Q
"Log in with Google" — is that OAuth2 or OIDC, and why is using a plain OAuth2 access token as proof of identity a bug?

## A
That's **OIDC** — an identity layer on top of OAuth2. OAuth2 alone answers "may this app access this resource?" (**delegation**); it says nothing about who the user is.

An access token is not audience-bound to your app: any app the user granted a token to could replay it against your backend and impersonate them. OIDC fixes this with the **ID token** — a JWT with the user's identity, signed by the provider, with an `aud` claim naming your client and a nonce — made to be verified, not forwarded.
