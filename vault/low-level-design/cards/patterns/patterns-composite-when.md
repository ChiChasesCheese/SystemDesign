---
id: patterns-composite-when
node: patterns.structural
type: qa
---
## Q
What problem shape calls for Composite, and what's the design tension inside the pattern?

## A
Use it when clients must treat **individual objects and groups of them uniformly** through one interface — the domain is a part-whole **tree**: file/directory, UI widget/container, single item/bundle in an order, expression AST.

```java
interface Node { long size(); }        // File returns bytes;
class Dir implements Node {            // Dir sums children — caller can't tell
    long size() { return children.stream().mapToLong(Node::size).sum(); }
}
```

Tension: put child-management (`add`/`remove`) on the common interface and leaves get meaningless methods (**transparency**, GoF's choice); put it only on the composite and clients must downcast (**safety**). Say which you chose and why.

Don't force it when the "hierarchy" is only ever one level deep — a plain list is simpler.
