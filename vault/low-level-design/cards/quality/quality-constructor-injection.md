---
id: quality-constructor-injection
node: quality.testability
type: qa
---
## Q
Why is constructor injection preferred over setter/field injection — three concrete properties?

## A
- **No invalid intermediate state**: the object is fully usable the moment it exists; setter injection allows a constructed-but-unwired object, adding "was it initialized?" as a bug class.
- **Dependencies are honest and final**: `final` fields, visible in one signature — and a constructor demanding six collaborators is a *feature*: it makes the SRP violation impossible to ignore (field injection hides it).
- **Framework-free tests**: `new Service(fakeRepo, fixedClock)` — no DI container, no reflection in unit tests.

Setter injection's remaining niche: genuinely **optional** or cyclic dependencies — both rare, and a cycle is usually a design smell to break instead.

## Q zh
为什么构造函数注入比 setter 注入或服务定位器更好？

## A zh
**构造函数注入**：
```java
public Service(Logger log, Database db) {
    this.log = log;
    this.db = db;
}
```
优势：
- 依赖在构造时清晰可见
- 不变性（字段可以是 final）
- 编译时检查（所有依赖都必须满足）
- 无法创建部分初始化的对象

**Setter 注入**：
- 依赖可以在任何时间设置
- 对象可以在没有所有依赖的情况下创建
- 易于选择性地覆盖（用于测试）

**服务定位器**：
- 隐藏的依赖
- 紧耦合到服务定位器

一般来说：优先使用构造函数注入（显式、强制、可测试）。
