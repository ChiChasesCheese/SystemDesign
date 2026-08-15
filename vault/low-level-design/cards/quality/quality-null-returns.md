---
id: quality-null-returns
node: quality.errors
type: qa
---
## Q
Your repository's `findById` can miss. Rank the return-type options for "not found" and say when absence should be an exception instead.

## A
- **Best: `Optional<Order>`** — absence is in the signature; the compiler makes every caller decide (`orElseThrow`, `map`, default). For collections, return an **empty collection**, never null.
- **Acceptable: null object** (`GuestUser.ANONYMOUS`) — only when there's a genuinely sensible do-nothing/default behavior; a null object that silently absorbs real work hides bugs.
- **Worst: return `null`** — moves the check to every caller, and the NPE fires far from the cause.

Absence should **throw** when it violates an invariant — the caller holds an id the system itself issued (`getById` on a just-created order), so "missing" means corruption, not a normal outcome. Pattern: offer `findById → Optional` and `getById → throws NotFoundException`, and let callers state their expectation.
