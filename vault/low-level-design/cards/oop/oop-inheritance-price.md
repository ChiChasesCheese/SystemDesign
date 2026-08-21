---
id: oop-inheritance-price
node: oop.pillars
type: qa
---
## Q
Inheritance buys polymorphism plus code reuse with one keyword. What price does it charge that composition doesn't?

## A
- **Strongest coupling available**: the subclass depends on base internals — base edits break children (fragile base class).
- **Fixed at compile time** and single-slot (one superclass); a composed collaborator is swappable at runtime and stackable.
- **Public is-a commitment**: every base contract now binds you (LSP), forever part of your API.

Hence: inherit for substitutable is-a, compose for reuse.

## Q zh
继承的隐藏成本是什么？什么时候组合是更好的选择？

## A zh
**继承的成本**：

1. **紧密耦合**：子类依赖于父类的实现细节，不仅仅是接口。父类改变打破子类。
2. **脆弱基类问题**：添加到父类的无辜方法可能意外破坏子类。
3. **单一父亲**：一个类只能从一个父类继承（多继承中有钻石问题）。
4. **接口污染**：子类继承所有父类方法，即使无关的。
5. **测试**：更难隔离测试；必须安装整个层次结构。

**组合是更好的选择何时**：
- **行为来自多个来源**。组合让你选择功能；继承是全或无。
- **行为在运行时改变**。交换一个字段比子类化容易。
- **不是「是一个」关系**。`Dog extends Animal` 有意义（是一个）；`Engine extends Machine` 但 `Car has an Engine`（组合，不是继承）。

**经验法则**：优先使用组合；只在真正的「是一个」关系和共享不可变行为时使用继承。
