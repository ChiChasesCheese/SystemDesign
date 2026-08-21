---
id: oop-immutability-payoff
node: oop.values
type: qa
---
## Q
Name three concrete bug classes that making a type immutable eliminates.

## A
- **Aliasing bugs**: instances can be shared and returned freely — no defensive copies.
- **Corrupted collections**: safe as `HashMap`/`HashSet` keys, since `hashCode` cannot drift after insertion.
- **Data races**: read-only sharing across threads needs no synchronization.

"Mutation" becomes `money.plus(x)` returning a new instance — every invariant is checked once, in the constructor.

## Q zh
不可变对象（不能改变）的好处是什么，何时它们的成本超过好处？

## A zh
**好处**：
- **线程安全**：无同步。多个线程可以共享一个不可变对象。
- **缓存**：相同的值可以安全地重复使用。HashMaps 和 sets 中没有别名问题。
- **推理**：一旦创建，状态不变。更少的精神模型。
- **防守**：没有人可以通过改变来伤害你。

**成本**：
- **创建的成本**：每次改变都需要新对象。例：`String` 连接，列表追加。
- **复制开销**：克隆对于大对象来说很昂贵。

**何时值得**：
- **频繁共享**（配置、常数、值对象如 `Money`）。
- **多线程**（`Date` 对象不是线程安全的；`LocalDate` 是且不可变）。
- **缓存键**。

**何时成本过高**：
- **频繁改变**（正在构造的大对象）。改用 Builder（构造时不可变）。
- **内存约束**（许多小对象）。

**黄金法则**：默认不可变；只在需要改变时制作可变。
