---
id: oop-equals-hashcode-contract
node: oop.values
type: qa
---
## Q
You override `equals` on `Money` but not `hashCode`. `set.add(new Money(5, USD))` then `set.contains(new Money(5, USD))` returns **false**. Explain, and state the contract that was broken.

## A
`HashSet` looks in the bucket chosen by `hashCode` first. Two equal objects with different identity hash codes land in different buckets, so `equals` is never even called.

Contract: **equal ⇒ equal hash codes** (the converse is not required — collisions are legal, just slower). Also required: reflexive, symmetric, transitive, consistent, and `x.equals(null) == false`.

Two practical consequences:
- **Symmetry with subclasses**: `instanceof` in a superclass `equals` lets `sub.equals(super)` disagree with `super.equals(sub)`; `getClass() !=` avoids that but forbids subclass equality entirely.
- Only fields that never change may participate — otherwise a mutation strands the object in the wrong bucket.
