---
id: reliability-deploy-strategies
node: reliability.resilience.containment
type: qa
---
## Q
Blue-green vs canary vs rolling deployment: what does each optimize for, and which one actually validates a release?

## A
- **Rolling**: replace instances in batches. Cheap (no spare fleet), but old and new run mixed for a while and rollback means rolling again — slowest to undo.
- **Blue-green**: full duplicate fleet, atomic traffic switch. **Fastest rollback** (flip back), no version mixing — but 2x capacity cost, and 100% of users hit a bad release at once.
- **Canary**: route a small slice (1→5→25→100%) to the new version while comparing its SLIs against baseline. The only strategy that **validates with real traffic before full exposure** — requires automated metric analysis to be more than theater.

Modern default: canary for validation, with blue-green-style instant rollback as the escape hatch. All three require [[architecture-schema-compat-rules]]-style compatibility since two versions run concurrently.
