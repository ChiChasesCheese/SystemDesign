---
id: oop-cascade-delete-decision
node: oop.relationships
type: qa
---
## Q
`removeFloor(floor)` is called. How does the relationship type decide what happens to the objects the floor referenced, and what must you clean up regardless?

## A
- **Composition (owned parts)** — `Spot`s exist only inside that floor → **cascade**: delete them with the floor; nothing else may hold a reference.
- **Aggregation (shared parts)** — a `Vehicle` parked there outlives the floor → **never cascade**: either detach (`spot.release()`) or **refuse the delete** while a live reference exists, which is usually the right answer for occupied floors.

Regardless of type, delete must also remove the object from every **secondary index / back-pointer** you built (`spotById`, `ticketsByPlate`). In-memory designs don't have foreign keys, so a missed index entry becomes a stale object that stays reachable and reads as "deleted but still bookable."

## Q zh
什么时候应该在对象模型中（而不是数据库中）实现 cascade delete？

## A zh
**应该在对象模型中**：
- 当删除是**语言级别语义**的一部分时。例：删除 `Document` 必须删除它的 `Page` 对象（不是可选的）。
- 生命周期**紧密耦合**（子无法独立存在）。
- **删除逻辑本身很复杂**（不仅仅是 delete 语句；有触发器、验证）。

**应该在数据库中**（或两者）：
- 外键约束为**数据完整性**担保。
- 多个应用程序访问数据库（ORM 无法控制所有删除）。

**最佳实践**：
```java
class Document {
    List<Page> pages;
    void delete() {
        pages.forEach(Page::delete);  // 对象级别 cascade
        // ... 清理，然后
        repo.delete(this);
    }
}
```

在数据库中也定义外键 `ON DELETE CASCADE`。两个防线。
