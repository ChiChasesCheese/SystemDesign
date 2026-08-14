---
id: principles-when-inherit
node: principles.composition
type: qa
---
## Q
Composition is the default — so when is inheritance still the right call? Give the checklist.

## A
All must hold:
- genuine **is-a with full substitutability** — every base contract kept (LSP)
- the base is **stable** and you control or trust it
- you want **polymorphic identity plus a shared skeleton** (template method), not merely code reuse

Legit examples: abstract chess `Piece` → `Rook`/`Bishop`; framework base classes. Motive is only "I want those methods" → compose instead.
