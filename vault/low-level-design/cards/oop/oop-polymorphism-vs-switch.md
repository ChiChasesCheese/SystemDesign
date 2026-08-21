---
id: oop-polymorphism-vs-switch
node: oop.pillars
type: qa
---
## Q
When do you replace a switch-on-type with polymorphism — and when is keeping the switch the better design?

## A
- **Replace** when the same type-switch recurs in several places and new variants keep arriving: one class per variant localizes each addition to one file (this is OCP in action).
- **Keep** a single exhaustive switch over a closed enum in one place: the compiler flags missing cases, and class-per-variant there is speculative generality.

Count the switch sites and the expected variants before reaching for the hierarchy.

## Q zh
为什么 polymorphism 优于 switch/if 链来处理变体，成本是什么？

## A zh
**Polymorphism**：
```java
interface Shape { double area(); }
class Circle implements Shape { 
    public double area() { return Math.PI * r * r; }
}
class Square implements Shape { 
    public double area() { return side * side; }
}

Shape s = getShape();  // 不知道什么类型
return s.area();       // 调用正确的实现
```

**Switch/if**：
```java
if (type == CIRCLE) return Math.PI * r * r;
else if (type == SQUARE) return side * side;
// 添加新变体？添加新 case。
```

**为什么 polymorphism 优于**：
- **开放-闭合**：添加新类型而不改变现有代码。
- **分散逻辑**：每个类知道自己如何计算；没有大的 switch。
- **类型安全**：编译器强制实现；switch 容易遗漏 case。

**成本**：
- **多个文件/类**。简单的 switch 在一个地方。
- **虚拟方法调用开销**（最小；JIT 优化）。
- **学习曲线**：初级程序员可能发现 switch 更直接。

**经验法则**：一个 switch → OK。更多 → 重构为多态。
