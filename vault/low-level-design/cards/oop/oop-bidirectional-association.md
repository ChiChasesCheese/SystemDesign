---
id: oop-bidirectional-association
node: oop.relationships
type: qa
---
## Q
`Order` holds `Customer`, and `Customer` holds `List<Order>`. What goes wrong with this bidirectional association, and what are the two disciplined options?

## A
Nothing keeps the two ends consistent: `order.setCustomer(c)` without `c.getOrders().add(order)` leaves a half-link, and every future mutation path must remember both. It also creates a **reference cycle** that breaks naive `equals`/`hashCode`/`toString` with infinite recursion.

- **Option A — one owning side**: only `Customer.addOrder(order)` exists; it sets the back-pointer itself and is the *only* mutator. `Order.setCustomer` is package-private or gone.
- **Option B — drop the back-pointer**: keep the single reference `Order → Customer` and answer "orders of a customer" from an index in the repository.

Default to B in a machine-coding round: a navigable link you can derive is cheaper than one you must maintain.

## Q zh
Bidirectional association（两个对象相互引用）是什么陷阱？

## A zh
**陷阱**：

1. **一致性地狱**：`order.addItem(item)` 必须也做 `item.setOrder(order)`。忘记一半导致**ghost 引用**和 bug。

2. **内存泄漏**：如果一个引用是强的且是循环的，垃圾收集无法清理。例：`Order` → `LineItem` → `Order`。

3. **序列化复杂性**：循环导致无限递归。需要 transient 字段或自定义序列化。

4. **测试和隔离**：模拟一个对象意味着也模拟另一个。测试变得耦合。

**何时不可避免**：父-子关系（`Form` ↔ `Field`），其中子需要返回到父。

**缓解**：
- 一个方向强（如 Order → LineItem）；另一个是弱引用或懒惰计算。
- 使用事件或观察者而不是反向引用。
