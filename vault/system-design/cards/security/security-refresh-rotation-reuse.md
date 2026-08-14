---
id: security-refresh-rotation-reuse
node: security.authn
type: qa
---
## Q
How does refresh token rotation turn token theft into a detectable event, and what happens on reuse?

## A
**Rotation**: every refresh issues a *new* refresh token and invalidates the one just used — each token is single-use, so a stolen refresh token stops working as soon as either party (thief or legitimate client) refreshes next.

**Reuse detection**: if an already-rotated token is presented again, two parties hold tokens from the same lineage — proof of theft. The server revokes the **entire token family** (the whole session), forcing re-authentication for both.

This is why rotation is mandatory for refresh tokens in browsers/SPAs, where long-lived tokens can't be stored safely. Builds on [[security-access-refresh-tokens]].
