---
id: security-secrets-handling
node: security.authz
type: qa
---
## Q
Where do service credentials (DB passwords, API keys) live in a well-designed 2026 system, and what beats static secrets entirely?

## A
- Never in code, images, or plain env files — those leak via repos, logs, and crash dumps.
- **Secret manager** (Vault, AWS/GCP Secrets Manager): centralized storage, access audit, automatic **rotation**; apps fetch at startup or lease dynamically.
- Better: **eliminate static secrets** — workload identity (IAM roles, SPIFFE, OIDC federation between platforms) issues short-lived credentials based on *what the workload is*, so there is nothing long-lived to steal or rotate.

Service-to-service trust inside the mesh: **mTLS**, so both ends authenticate with certificates and traffic is encrypted everywhere, not just at the edge.
