---
id: security-rbac-vs-abac
node: security.authz
type: qa
---
## Q
When does RBAC stop being enough and force a move toward ABAC (or relationship-based) authorization?

## A
RBAC (user → roles → permissions) breaks when the decision depends on **context the role can't encode**:

- **Resource ownership/relationships**: "editors can edit *documents in their own workspace*" — pure RBAC needs a role per workspace (role explosion); ReBAC systems (Zanzibar-style, e.g. SpiceDB/OpenFGA) model this directly.
- **Runtime attributes**: time of day, device posture, data classification, tenant of the request.

Rule of thumb: RBAC for coarse, stable job functions; ABAC/ReBAC when policies mention properties of the **resource or environment**, not just the user.
