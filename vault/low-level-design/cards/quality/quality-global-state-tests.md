---
id: quality-global-state-tests
node: quality.testability
type: qa
---
## Q
Name the two distinct ways static/global state breaks tests, and the standard fix for nondeterministic dependencies like time.

## A
Two failure modes:

- **No substitution point**: `Payment.process()` as a static call (or `Singleton.getInstance()`) can't be replaced — every test drags the real implementation along.
- **State leaks between tests**: a mutable global survives across test methods, so tests pass alone and fail in suite (or in parallel) depending on **order** — the worst kind of flake.

Fix for time (the canonical case): never call `LocalDateTime.now()` in domain logic — inject a `Clock`; tests pass `Clock.fixed(...)` and can step time deterministically. Same recipe for randomness (`Random` seed/interface) and UUIDs (injected `IdGenerator`). Legacy escape hatch: wrap the static in an instance class you can inject — then migrate.

## Q zh
全局状态如何使测试变得困难？如何避免它？

## A zh
全局状态的问题：

**1. 测试隔离**：
```java
// 全局
static Database db = Database.connect("prod");

// 在测试中...
db 仍然指向 prod！测试数据被污染。
```

**2. 测试顺序依赖**：
- 一个测试修改全局状态
- 下一个测试依赖于那个状态
- 单独运行时测试通过，在套件中失败

**3. 并发问题**：
- 多个测试同时运行会相互干扰

避免全局状态：
```java
// 好的：依赖注入
public class Service {
    private Database db;
    public Service(Database db) { this.db = db; }
}

// 在测试中
@Test void testWithMock() {
    Service service = new Service(new MockDatabase());
}
```

修复现有的全局状态：
- 实例化而不是静态
- 使用依赖注入
- 在测试中使用 setUp/tearDown 重置
