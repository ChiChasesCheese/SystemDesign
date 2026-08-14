---
id: security-confused-deputy
node: security.authz
type: qa
---
## Q
An internal reporting service with read access to *all* tenants' data serves any caller that asks. A low-privilege client requests another tenant's report and gets it. Name the vulnerability class and the fix.

## A
**Confused deputy**: a privileged service is tricked into using *its own* authority on behalf of a less-privileged caller. Classic instances: internal services trusting any in-network caller, SSRF against cloud metadata endpoints (the VM is the deputy), cross-account access without an external ID.

Fix — make authorization decisions on the **originating principal**, not the deputy:

- **Propagate end-user/tenant context** through the call chain (on-behalf-of token exchange, signed user context), and check it at the data layer.
- Scope the deputy's own credentials down (per-tenant creds, external IDs for cross-account roles) so it *cannot* over-reach even when confused.
