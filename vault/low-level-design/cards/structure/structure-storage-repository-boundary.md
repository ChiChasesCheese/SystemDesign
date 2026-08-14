---
id: structure-storage-repository-boundary
node: structure.storage
type: qa
---
## Q
In a 90-minute round with purely in-memory data, why wrap a `HashMap` in a repository interface (`save`, `findById`, `findByX`) instead of letting services touch the map?

## A
- **The classic follow-up is "now persist it"** — with `interface OrderRepository`, that's one new implementation; without it, every service changes.
- **Tests** get an obvious seam: inject an in-memory fake, no mocking framework.
- **One place for storage concerns**: locking, index maintenance, and defensive copies live behind the interface instead of leaking into business logic.

Cheap to do: the map-backed implementation is ~10 lines. Interviewers grade extensibility, and this is the highest-value seam per minute spent.
