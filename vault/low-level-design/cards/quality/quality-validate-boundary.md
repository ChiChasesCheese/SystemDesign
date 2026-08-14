---
id: quality-validate-boundary
node: quality.errors
type: qa
---
## Q
"Validate at the boundary" — what does it mean structurally, and how do value objects make re-validation unnecessary?

## A
Structurally: all input crosses **one checkpoint** (API handler, command constructor) where it's checked and **converted into types that can't hold invalid data**. Inside that boundary, code trusts its inputs — no defensive re-checking scattered through every layer.

The mechanism is **"parse, don't validate"**: instead of passing a `String` plus the knowledge that someone once checked it, construct `Email.of(raw)` which **throws on bad input and cannot exist invalid**. The type system then carries the proof everywhere the value goes.

```java
record Email(String value) {
    Email { if (!value.matches(".+@.+")) throw new InvalidEmailException(value); }
}
```

Interview payoff: "invalid states are unrepresentable" — invariants live in constructors, not in every method that touches the data.
