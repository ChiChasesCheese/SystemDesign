---
id: quality-extract-method-triggers
node: quality.refactoring
type: qa
---
## Q
Extract method: what are the two classic triggers, and what does a well-composed method look like afterward?

## A
Triggers:

- **A comment announcing a block** — `// validate input` above six lines means the block wants to be `validateInput()`; the name replaces the comment.
- **A fragment you must study to see what it does** — or one you'd like to reuse or test in isolation.

Target shape (**composed method**): the body reads as a sequence of same-altitude, intention-named steps —

```java
void checkout(Cart c) {
    validate(c);
    var total = priceWithDiscounts(c);
    charge(c.customer(), total);
    emitReceipt(c, total);
}
```

Each step is one level of abstraction; details live one call down. When several extracted methods keep sharing the same parameters, that's the follow-on trigger for **extract class**.
