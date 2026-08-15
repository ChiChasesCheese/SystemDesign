---
id: method-final-twenty-minutes
node: method.delivery
type: qa
---
## Q
20 minutes left. Two features are half-written and nothing has been run end-to-end yet. What is the order of operations?

## A
1. **Freeze scope immediately** — no new feature enters the file after this point.
2. **Delete or stub the half-written branches.** Code that doesn't compile costs more than a missing feature; a one-line `throw new UnsupportedOperationException("out of scope")` reads as a decision.
3. **Get it running** (~8 min): compile, wire dependencies by hand in `main`, fix crashes.
4. **Demo driver** (~7 min): happy path + one edge case, printed output.
5. **Narrate** (~5 min): what's in, what's stubbed, where each stub plugs in.

Half-finished code scores as broken code; a stub scores as scoping.
