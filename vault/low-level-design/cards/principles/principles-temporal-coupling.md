---
id: principles-temporal-coupling
node: principles.coupling
type: qa
---
## Q
```java
var svc = new ReportService();
svc.setStore(store);
svc.init();
svc.run();          // NPE / IllegalStateException if you skip a step
```
Name this coupling, list its two detection signals, and give the fix.

## A
**Temporal coupling** — correctness depends on an ordering the type doesn't express. Signals:

- Methods that begin with `if (!initialized) throw new IllegalStateException(...)`.
- Setters for things the object cannot function without (`setStore`), i.e. a constructor that leaves the object invalid.

Fix: **make the invalid state unconstructable** — take every required collaborator in the constructor (or a builder that validates and returns a ready object), and drop `init()` into it. When phases are genuinely distinct, encode them in *types*: `Connection.open()` returns an `OpenConnection` that is the only thing with `query()`.

Same smell, larger scale: two calls that must happen in order across classes — merge them into one method that owns the sequence.

## Q zh
什么是时间耦合，为什么它是个问题？

## A zh
时间耦合发生在方法必须以特定顺序调用时，但代码没有强制这个顺序。

例子：
```
user.setEmail(new_email);  // 必须在 validate 之前
user.validate();
user.save();
```

问题：
- 顺序对调用者来说不是显而易见的
- 没有编译时检查；错误直到运行时才显现
- 难以重构或并行化

解决方案：
- 创建一个方法强制顺序：`user.updateAndValidateAndSave(new_email)`
- 使用生成器（Builder）分阶段进行
- 使用返回"下一步"对象的 API 指导调用者
