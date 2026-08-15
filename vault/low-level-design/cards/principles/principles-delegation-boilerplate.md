---
id: principles-delegation-boilerplate
node: principles.composition
type: qa
---
## Q
"Just use composition" — name the two real costs of replacing inheritance with delegation, and how each is mitigated.

## A
- **Forwarding boilerplate**: to keep the wrapped type's interface you hand-write N one-line methods, and each new interface method must be added to every wrapper. Mitigation: a reusable `ForwardingX` base your wrappers extend (Effective Java's skeletal forwarding class), IDE-generated delegates, Kotlin `class A(b: B) : B by b`, Lombok `@Delegate`.
- **Lost self-reference (the SELF problem)**: the inner object calls *its own* methods, not the wrapper's — so a counting/logging decorator misses calls the wrapped object makes internally, and the inner object passing `this` to a callback leaks the undecorated object.

The second cost is fundamental, not syntax; but note it's the same self-use that makes inheritance fragile — composition at least makes it visible.
