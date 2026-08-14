---
id: architecture-api-versioning-strategies
node: architecture.discovery
type: qa
---
## Q
URI versioning (/v2/) vs header versioning vs "no versions, additive-only": when is each the right API evolution strategy?

## A
- **Additive-only evolution** (no version bumps): the modern default — only compatible changes ([[architecture-schema-compat-rules]]), clients ignore unknown fields, breaking changes handled by expand-contract ([[architecture-expand-contract]]). Cheapest: one live version to operate.
- **URI versioning** (`/v2/`): for rare, genuinely breaking redesigns with external consumers — explicit, cacheable, easy to route/deprecate per version. Cost: you now run and support N versions, and internal models fork.
- **Header/date versioning** (e.g. Stripe's pinned API dates): many small versions with server-side translation layers down to one internal model — great DX, but the translation-chain machinery is expensive to build.

Anti-pattern: reflexively minting `/v2/` for changes that could have been additive.
