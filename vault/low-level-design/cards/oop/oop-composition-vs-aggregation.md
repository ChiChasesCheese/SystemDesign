---
id: oop-composition-vs-aggregation
node: oop.relationships
type: qa
---
## Q
`ParkingLot`–`Floor` vs `Course`–`Student`: which is composition, which aggregation — and what single question decides?

## A
Question: **does the part's lifetime end with the whole, under exclusive ownership?**

- `Floor` exists in exactly one lot and dies with it → **composition** (filled diamond).
- `Student` outlives the course and belongs to many → **aggregation** (hollow diamond).

Both are has-a; ownership + lifetime is the discriminator, and composition is the one your destructor/cascade-delete logic must respect.

## Q zh
Composition vs aggregation——两者都是「有关系」。区别是什么？

## A zh
- **Composition**（强）：部分**由整体拥有和管理**；部分**无法独立存在**。整体被销毁，部分也被销毁。例：`Car` 和 `Engine`；没有 car 就没有 engine。
- **Aggregation**（弱）：整体只**持有对**部分的引用；部分**可以独立存在**。删除整体，部分仍然存在。例：`Team` 和 `Player`；player 可以加入另一个 team。

在 UML 中：
- Composition = 填充的菱形。
- Aggregation = 空的菱形。

在 Java 代码中，区别**语义上**（只能通过设计意图看出）；语言中没有执行。

**实际区别**：lifecycle 和所有权。
