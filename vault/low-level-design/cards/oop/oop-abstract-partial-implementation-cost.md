---
id: oop-abstract-partial-implementation-cost
node: oop.interfaces
type: qa
---
## Q
You put shared logic in an abstract base class with `protected` hooks (template method). What are you paying for that reuse, and what's the alternative shape?

## A
Costs:

- **You spend the single inheritance slot** — the subclass can never extend anything else.
- **`protected` members are public API to subclasses**: you can't rename or reorder them later without breaking every child, and the base's call order becomes a contract.
- The base is **hard to test alone** (needs a fake subclass), and subclasses can't be tested without dragging the base's behavior in.

Alternative: **interface + a composed helper** — the algorithm lives in a collaborator that takes the varying step as a strategy object. Java's compromise is the *skeletal implementation* pattern: publish the interface, offer `AbstractFoo` as an optional convenience so implementers who need their own hierarchy can forward to it instead.

## Q zh
abstract class 可以有实现。它何时比接口更好的选择是「工作的一半已经完成」？

## A zh
**答案**：当子类*实际上重用*共同的实现时。

例如：一个 repository 有通用的 CRUD、分页、缓存逻辑。每个具体 repository（UserRepo、ProductRepo）覆盖只有 `query()` 和 `rowMapper()`。具体逻辑住在基类中；子类专注于特定域。

```java
abstract class Repository<T> {
    List<T> findAll() { /* 通用分页和缓存 */ }
    protected abstract String query();
}
```

**成本**：
- 子类继承所有数据成员；不能多继承或轻易更改基类。
- 过度设计：如果只有**一个**子类，base 中的共享代码只是噪声。

**只有在以下情况下回报**：≥2个子类，*实际上*每个子类节省 20+ 行代码。
