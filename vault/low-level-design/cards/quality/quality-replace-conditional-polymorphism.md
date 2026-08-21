---
id: quality-replace-conditional-polymorphism
node: quality.refactoring
type: qa
---
## Q
"Replace conditional with polymorphism" — what's the trigger, and when is the switch actually the better design?

## A
Trigger: the **same** `switch`/`if`-on-type appears in **multiple places** — each new type means shotgun surgery across all of them. Move each branch's body into a subclass/strategy override; dispatch replaces the conditionals.

```java
switch (emp.type) { ENGINEER -> base*1.1; MANAGER -> base+bonus; }  // in pay(), inBonus(), inReport()...
// becomes: emp.pay() — one class per type owns all its branches
```

Keep the switch when:

- It occurs **once** — polymorphism trades one readable block for classes scattered across files.
- New **operations** are more frequent than new **types** — polymorphism optimizes for adding types; a switch (or visitor) optimizes for adding operations. That's the expression problem: pick the axis that actually varies.

## Q zh
如何用多态性替换大的 switch 语句？

## A zh
模式：

**使用 switch 的代码**：
```java
switch (shapeType) {
    case CIRCLE:
        return Math.PI * r * r;
    case SQUARE:
        return s * s;
    case TRIANGLE:
        return b * h / 2;
}
```

**使用多态性**：
```java
interface Shape {
    double area();
}
class Circle implements Shape {
    public double area() { return Math.PI * r * r; }
}
class Square implements Shape {
    public double area() { return s * s; }
}
// 使用
shape.area();  // 多态调用
```

优势：
- 添加新形状不需要修改现有代码
- 每个类都知道自己如何计算（高内聚）
- 遵循开-闭原则

何时应用：
- switch 语句按类型分派
- 不同类型有不同的行为
- 经常添加新类型
