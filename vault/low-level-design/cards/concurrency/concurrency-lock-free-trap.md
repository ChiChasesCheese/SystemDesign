---
id: concurrency-lock-free-trap
node: concurrency.hazards
type: qa
---
## Q
A candidate says "I'll make it lock-free, so no deadlock." Why is this usually the wrong move in an LLD round?

## A
Lock-free removes deadlock but not the hazards that actually bite:

- **CAS covers one word.** Any invariant spanning two fields (`balance` *and* `ledger`) can't be maintained by a CAS loop — you get torn, individually-atomic updates.
- **Livelock/starvation remain**: under contention, CAS retry loops burn CPU and a slow thread can retry forever (lock-*free* guarantees system progress, not per-thread progress; that's wait-free).
- Plus ABA and memory reclamation, and code no reviewer can verify in an hour.

Right answer: use lock-free **components** others wrote — `AtomicLong` counters, `ConcurrentHashMap`, `LongAdder` — and a plain lock for your own multi-field invariants. If contention is the concern, shrink the critical section or shard the lock before going lock-free.

## Q zh
为什么无锁代码陷阱会导致竞态条件？

## A zh
无锁代码的常见错误：

```java
// 错误：两个原子操作不是原子的
if (queue.isEmpty()) {      // CAS 或原子检查
    queue.add(item);        // 单独的 CAS —— 在两者之间窗口！
}
```

竞态条件：
- 线程 1 检查 isEmpty() = true
- 线程 2 添加一个项目
- 线程 1 仍然添加 —— 队列现在有 2 个项目

修复：
- 使用原子的组合操作：`putIfAbsent`、`offer`
- 或在循环中进行 CAS 重试
- 或使用适当的同步

无锁代码看起来更快，但需要深入理解内存顺序。通常不值得。
