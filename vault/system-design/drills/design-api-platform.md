---
nodes: [security.authn.tokens, security.authn.oauth, security.authz, networking.api-styles, traffic.gateways]
tags: [flagship, security]
---
# Drill: Design a public API platform

Open your product to third-party developers: their apps act on behalf of
your users, your own mobile client uses the same edge, and machine-to-
machine integrations run unattended. Authentication, authorization, and
the gateway that enforces both.

**Constraints to state and honor**
- Three caller classes: first-party mobile, third-party apps acting for a user, and server-to-server integrations.
- A revoked grant must stop working in seconds, not at token expiry.
- Partners need stable API contracts; you need to keep shipping weekly.
- A stolen token must not be replayable from another machine.

**Grading points**
- The grant type chosen per caller class, with the implicit flow rejected and PKCE explained as what it defends against ([[security-oauth-grant-selection]], [[security-oauth-code-pkce]], [[security-oauth-vs-oidc]]).
- Scopes and audience distinguished — what the token may do versus who may accept it ([[security-oauth-scopes-vs-audience]], [[security-confused-deputy]]).
- Short access tokens plus rotating refresh tokens, with reuse detection as the theft signal ([[security-access-refresh-tokens]], [[security-refresh-rotation-reuse]]).
- The stateless-JWT-versus-session trade taken seriously, given the seconds-to-revoke requirement ([[security-sessions-vs-jwt]]).
- Browser token storage decided explicitly, with the XSS consequence of each option ([[security-oauth-browser-token-storage]]).
- Sender-constrained tokens (mTLS or DPoP) named as the answer to replay, and mTLS versus tokens for service-to-service argued ([[security-sender-constrained-tokens]], [[security-mtls-vs-tokens-s2s]]).
- Authorization model chosen — RBAC, ABAC, or relationship-based — with the query it has to answer at request time ([[security-rbac-vs-abac]], [[security-api-keys-vs-user-tokens]]).
- Secrets for partner integrations stored and rotated without downtime ([[security-secrets-handling]], [[security-secrets-rotation-live]]).
- The gateway's job scoped: authn, quotas, and routing centralized, business logic kept out ([[traffic-gateway-centralizes]], [[traffic-gateway-risks]], [[traffic-reverse-proxy-vs-gateway]]).
- Timeout budgets propagated from the edge inward, and request buffering understood before it becomes a memory incident ([[traffic-timeout-budget-propagation]], [[traffic-gateway-buffering]]).
- API style and versioning decided for a public contract — REST as default, gRPC where justified, pagination that survives inserts ([[networking-rest-as-default]], [[networking-grpc-over-rest]], [[networking-cursor-vs-offset-pagination]], [[networking-webhooks-vs-polling]]).

**Attempt log**
- [ ] Attempt 1 (date, 45 min, self-graded notes):
