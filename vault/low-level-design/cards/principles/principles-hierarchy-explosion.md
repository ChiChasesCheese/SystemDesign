---
id: principles-hierarchy-explosion
node: principles.composition
type: qa
---
## Q
Coffee add-ons modeled as subclasses: `CoffeeWithMilk`, `CoffeeWithMilkAndSugar`, `CoffeeWithSoyMilkAndSugar`... Why does this hierarchy rot, and what's the composition fix?

## A
- **Combinatorial explosion**: n independent add-ons ⇒ up to 2^n subclasses, because inheritance forces all variation axes into one tree.
- Every base change ripples through the tree (fragile base class).

Fix: make the varying dimension a composed object — decorators wrapping a `Beverage`, or a list of `AddOn` components. Composition lets independent axes vary independently.

## Q zh
当你在继承中添加第二维变化时会发生什么，为什么是个问题？

## A zh
你最终得到类爆炸：
```
Animal
  ├─ Dog
  │  ├─ ServiceDog (does service work)
  │  └─ PetDog (doesn't do service work)
  └─ Cat
     ├─ ServiceCat
     └─ PetCat
```

问题：
- N 维变化导致 M^N 个类
- 每个新概念都强制修改层次结构
- 违反开-闭原则：要添加新的维度，你必须修改现有的类

解决方案：使用组合或特性而不是继承的额外级别。
