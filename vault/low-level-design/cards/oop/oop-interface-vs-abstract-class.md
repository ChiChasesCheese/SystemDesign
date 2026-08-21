---
id: oop-interface-vs-abstract-class
node: oop.interfaces
type: qa
---
## Q
Interface or abstract class — what's the decision rule? One example of each from a machine-coding problem.

## A
- **Interface**: a capability contract across otherwise-unrelated types; a class can hold many — `FareStrategy`, `Notifiable`.
- **Abstract class**: a family sharing **state and a partial implementation** — chess `Piece` holding position with abstract `possibleMoves()`.

Rule of thumb: no shared fields → interface; shared fields/protected helpers → abstract class. When torn, start with the interface — it's the weaker, easier-to-revise commitment.

## Q zh
什么时候使用接口 vs abstract class？

## A zh
- **Interface**：契约、行为列表。实现者承诺支持操作。多个接口。通常**无实现**（Java 8+ 默认方法是例外）。
- **Abstract class**：部分实现、共享基础设施。通常**有**字段和一些已实现方法。一个父类。

**何时选择**：
- **行为签名只**（许多无关的实现者做相同的事情）→ Interface。例：`Serializable`、`Runnable`。
- **共享实现或状态**→ Abstract class。例：`Repository` 的常见 CRUD 逻辑。
- **多个来源**→ Interface。例：`class Dog implements Animal, Comparable`。
- **一个语义的实现族**→ Abstract class。例：`Shape` 及其子类。

**现代倾向**：默认接口；只在需要状态或实现时升级到 abstract class。
