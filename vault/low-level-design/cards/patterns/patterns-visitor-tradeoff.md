---
id: patterns-visitor-tradeoff
node: patterns.behavioral
type: qa
---
## Q
Visitor makes one thing easy and one thing hard. Which, and what property of the class hierarchy must hold before you use it?

## A
Visitor flips the extension axis:

- **Easy: adding operations.** A new operation over the hierarchy (type-check, pretty-print, evaluate over an AST) is one new visitor class — no touching the element classes.
- **Hard: adding element types.** A new element forces a new `visit` method on **every existing visitor** — it's the exact mirror of adding a method to every subclass.

Precondition: the element hierarchy is **stable** and the set of operations keeps growing (compilers, document models). If new element types arrive often, visitor is the wrong trade — use plain polymorphic methods. Mechanism worth naming: `element.accept(visitor)` → `visitor.visit(this)` is **double dispatch**, selecting behavior on both runtime types.

## Q zh
Visitor 是什么，它在结构中增加什么，它何时被证明是值得的？

## A zh
**Visitor**：给树（AST、菜单、场景图）上的每个节点**注入新的操作**，而不修改节点类。

```java
interface Expr { Object accept(Visitor v); }
class BinOp implements Expr { 
    Object accept(Visitor v) { return v.visit(this); }
}
```

**增加的复杂性**：
- 两种方法分派（`accept()` + `visit()`）。
- 添加节点类型需要更新所有访问者。
- 代码在访问者中分散。

**何时值得**：
- **许多独立操作**（打印、类型检查、代码生成）在**固定的树结构**上。
- 操作**经常改变**；节点类型**很少**改变。
- 你避免了「把所有逻辑塞进节点」的诱惑。

**何时不值得**：
- 几个操作或常添加新节点类型。直接在节点中放置方法。
