---
id: method-extension-probe
node: method.evaluation
type: qa
---
## Q
The interviewer probes: "how would you add a new vehicle type / discount rule?" What separates a passing answer from a strong one?

## A
- **Passing**: correctly describing which code you'd edit.
- **Strong**: the change is *additive* — one new class or enum constant implementing an existing interface, registered in one place, zero edits to existing conditionals.

If your design would force shotgun edits, say so and name the refactor (extract a strategy interface) — owning the weakness scores better than defending it.
