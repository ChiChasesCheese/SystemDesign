---
id: principles-lsp-signals
node: principles.solid
type: qa
---
## Q
Name three code signals that a subclass violates LSP, and the standard fix.

## A
Signals:
- an override throws `UnsupportedOperationException` (or silently no-ops)
- overrides strengthen preconditions or weaken postconditions/invariants — `Square.setWidth` also changing height
- callers `instanceof`-check to dodge particular subclasses

Fix: the is-a is false — break the hierarchy or replace inheritance with composition. Substitutability under the base's contract, not real-world taxonomy, decides is-a.
