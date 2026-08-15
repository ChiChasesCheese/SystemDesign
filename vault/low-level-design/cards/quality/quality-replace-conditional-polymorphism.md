---
id: quality-replace-conditional-polymorphism
node: quality.refactoring
type: qa
---
## Q
"Replace conditional with polymorphism" — what's the trigger, and when is the switch actually the better design?

## A
Trigger: the **same** `switch`/`if`-on-type appears in **multiple places** — each new type means shotgun surgery across all of them. Move each branch's body into a subclass/strategy override; dispatch replaces the conditionals.

```java
switch (emp.type) { ENGINEER -> base*1.1; MANAGER -> base+bonus; }  // in pay(), inBonus(), inReport()...
// becomes: emp.pay() — one class per type owns all its branches
```

Keep the switch when:

- It occurs **once** — polymorphism trades one readable block for classes scattered across files.
- New **operations** are more frequent than new **types** — polymorphism optimizes for adding types; a switch (or visitor) optimizes for adding operations. That's the expression problem: pick the axis that actually varies.
