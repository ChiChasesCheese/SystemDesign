---
id: concurrency-visibility-stale-flag
node: concurrency.model
type: qa
---
## Q
Thread A sets `running = false`, but the worker looping on `while (running) {}` never stops — no crash, no exception. Why can this happen, and what are two fixes?

## A
There is **no happens-before edge** between the write and the reads: the write can sit in a store buffer, and the JIT may hoist the read out of the loop entirely (it "proves" `running` never changes on this thread).

- Fix 1: declare the flag `volatile` / atomic — every read sees the latest write.
- Fix 2: read and write it under the **same lock** (lock release → lock acquire creates the ordering).

Key point: this is a **visibility** bug, not an atomicity bug — the write happened, it just isn't guaranteed to be seen.

## Q zh
为什么一个普通布尔标志在无锁代码中是陈旧的？

## A zh
普通变量没有 happened-before 保证：

```java
boolean done = false;

// 线程 1：
done = true;

// 线程 2（其他核上）：
while (!done) { }  // 可能永远不会看到 true！
```

为什么：
- 写入可能留在线程 1 的 L1 缓存中
- 线程 2 从其自己的 L1 缓存中读取
- 没有缓存一致性消息或内存屏障
- Java 内存模型对普通变量没有保证

修复：
```java
volatile boolean done = false;  // 强制缓存一致性
```

`volatile` 添加了内存屏障，强制每次读都查看最新值。

其他修复：
- 使用锁：`synchronized`
- 使用 `AtomicBoolean`
