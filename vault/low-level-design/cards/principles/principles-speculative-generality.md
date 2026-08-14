---
id: principles-speculative-generality
node: principles.simplicity
type: qa
---
## Q
Name three concrete signs of the *speculative generality* smell, and the refactor for each.

## A
- Interface/abstract class with exactly one implementation and no test-seam need → **collapse hierarchy / inline**.
- Parameters or type parameters added "for flexibility" but never varied → **remove parameter**.
- Hooks and fields exercised only by tests, never by production code → **delete**.

It's YAGNI applied retroactively: generality that never earned its keep is a cost with no buyer.
