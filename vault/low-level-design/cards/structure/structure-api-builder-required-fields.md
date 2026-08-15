---
id: structure-api-builder-required-fields
node: structure.api
type: qa
---
## Q
When does a fluent builder beat constructors/setters, and where do you enforce required fields and invariants with a builder?

## A
- Builder wins when a type has **several optional parameters** (telescoping-constructor smell) or you want an **immutable** object assembled step by step. Two params, all required → just use a constructor.
- **Required fields go in the builder's constructor** (can't even start without them); optional ones are fluent methods.
- **Cross-field invariants are validated once, in `build()`** (e.g. `start < end`), so an invalid object can never exist.

Bonus: the built class gets a private constructor taking the builder — no setters, so every instance is valid and thread-safe to share.
