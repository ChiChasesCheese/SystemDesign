---
id: oop-association-vs-dependency
node: oop.relationships
type: qa
---
## Q
`NotificationService` appears as a constructor-injected field of `OrderService` in one design, and as a parameter of `checkout(cart, notifier)` in another. Name each relationship and what the choice signals.

## A
- **Field** → association: structural, long-lived — "OrderService *has* a notifier."
- **Parameter/local** → dependency: transient uses-a, the weakest coupling in UML.

Signal: keep it a dependency while only one operation needs it; promote to an association when most methods do. Weakest workable relationship wins — it minimizes what a change can break.

## Q zh
UML 中的 association vs dependency——区别是什么，何时选择哪一个声明？

## A zh
- **Association**（实线）：对象有**持久的、结构性的**关系。一个对象**持有**另一个的引用，通常作为字段。例：`Order` 有许多 `LineItem`。
- **Dependency**（虚线）：一个类**临时依赖**另一个，通常为了调用方法。通常**局部**（参数、返回值）或**临时**。例：`OrderProcessor.process(Order)` 取决于 `PaymentService`。

**何时声明**：
- 如果关系**长期存在**且对象标识很重要→ Association。
- 如果关系是**临时的、仅用于**一次交互→ Dependency。

在代码中：
```java
class Order {
    LineItem[] items;  // 关联——字段
    void process(PaymentService p) { ... }  // 依赖——参数
}
```
