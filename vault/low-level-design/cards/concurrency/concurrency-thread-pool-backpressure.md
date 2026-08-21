---
id: concurrency-thread-pool-backpressure
node: concurrency.patterns
type: qa
---
## Q
A fixed thread pool fed by an **unbounded** task queue never rejects work. What actually fails under sustained overload, and what's the disciplined setup?

## A
Nothing rejects, so nothing pushes back: the queue grows without limit — latency climbs (tasks wait behind thousands of others) and the process eventually **OOMs**. The failure is *hidden* until it's catastrophic.

- Disciplined: **bounded queue + explicit rejection policy**. `CallerRuns` is the classic backpressure choice — the submitter executes the task itself, naturally slowing producers.
- Size CPU-bound pools ≈ number of cores; IO-bound pools larger (≈ cores × (1 + wait/compute)).

Rule: overload must surface at the boundary, not accumulate in memory.

## Q zh
线程池如何实现 backpressure？为什么有界队列很关键？

## A zh
Backpressure = 阻止生产者生产比消费者处理更快的数据。

线程池中的机制：
1. **有界队列**：容量有限，不是无限的
2. **拒绝处理程序**：当队列满时的行为
   - `CallerRunsPolicy`：调用线程自己运行任务（阻塞生产者）
   - `DiscardPolicy`：丢弃任务
   - `AbortPolicy`：抛出异常

例子：
```java
// 队列有 100 个任务
new ThreadPoolExecutor(
    10,              // 核心线程
    20,              // 最大线程
    new LinkedBlockingQueue<>(100),  // 有界！
    new ThreadPoolExecutor.CallerRunsPolicy()  // 阻塞提交者
);
```

为什么有界队列很关键：
- 无界队列导致内存不足（堆积任务）
- 生产者不知道消费者何时赶不上
- 有界队列强制背压，让生产者等待
