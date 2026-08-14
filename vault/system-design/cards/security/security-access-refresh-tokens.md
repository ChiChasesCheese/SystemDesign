---
id: security-access-refresh-tokens
node: security.authn
type: qa
---
## Q
Why pair a short-lived access token (~5–15 min) with a long-lived refresh token, instead of one long-lived token?

## A
It splits the two jobs a single token can't do at once:

- The **access token** is verified statelessly on every request; keeping it short bounds the damage window if stolen and makes revocation "wait out the TTL."
- The **refresh token** is presented rarely, only to the auth server — the one place that checks server-side state, so it **can** be revoked instantly.

Modern hardening: **refresh token rotation** — each use issues a new one; reuse of an old refresh token signals theft and kills the whole session family.
