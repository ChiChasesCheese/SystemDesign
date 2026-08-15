---
id: security-oauth-scopes-vs-audience
node: security.authn.oauth
type: qa
---
## Q
Scopes vs audience: what does each one constrain, and why is "the token has scope `orders:read`, so let the request through" an authorization bug?

## A
- **Scope** = *what the user delegated to this client* — a coarse, consent-visible capability (`orders:read`). It only ever **narrows** what the client may ask for.
- **Audience (`aud`)** = *which resource server may accept this token*. Every RS must reject tokens not minted for it (along with `iss`, signature, `exp`), or a token issued for the low-value analytics service can be replayed against the payments service — a classic confused deputy.

The bug is treating scope as a permission check. Scope says the client is *allowed to ask*; it says nothing about whether **this subject** owns **this object**. You still need the object-level check: `order.tenant_id == token.tenant_id`, `order.user_id == token.sub`. Effective permission is the **intersection** of the user's real rights and the token's scope.

Practical rule: request per-resource tokens (`resource`/`audience` parameter at the token endpoint) so a leak is bounded to one service, and keep scopes coarse — fine-grained policy belongs in the resource server, not in the token.
