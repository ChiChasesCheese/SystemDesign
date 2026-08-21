---
id: patterns-singleton-costs
node: patterns.creational
type: qa
---
## Q
Why is Singleton the most criticized GoF pattern, and what's the modern alternative when you genuinely need one instance?

## A
Singleton couples two decisions that should be separate: *one instance exists* and *everyone accesses it globally*.

- The global access point makes dependencies **invisible** (nothing in a signature says the class uses it) and makes tests share **hidden mutable state** you can't swap or reset.
- It hard-codes the concrete class — no substituting a test double.

Modern alternative: keep the class ordinary, create **one instance at the composition root** and inject it (DI container or hand-wired `main`). Reserve true singletons for stateless, cross-cutting facts (e.g. a process-wide logger), and if forced, use an `enum` singleton / static holder for safe lazy init.

## Q zh
Singleton 的隐藏成本是什么，什么时候会backfire？

## A zh
**表面**优点：全局访问、一个实例、初始化一次。

**隐藏成本**：

1. **线程安全**：初始化序列变得脆弱（双重检查锁定 bug、初始化顺序）。
2. **测试**：无法轻易模拟。Singleton 持有真实状态；每个测试污染下一个。需要 reset 方法（哈克）或 thread-local 版本（复杂）。
3. **隐藏耦合**：调用者通过 `Singleton.getInstance()` 获得全局依赖，难以跟踪。
4. **并发**：即使线程安全，多个线程访问同一实例可能导致竞态条件。
5. **延迟初始化陷阱**：首次访问 Singleton 时初始化可能失败，而调用代码没有准备好处理。

**何时 backfire**：
- 多线程中的状态共享。
- 数据库连接池（应该有多个实例进行负载均衡）。
- 需要测试隔离时。

**替代**：依赖注入，让容器管理实例生命周期。
