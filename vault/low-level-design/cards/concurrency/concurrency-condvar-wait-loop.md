---
id: concurrency-condvar-wait-loop
node: concurrency.primitives
type: qa
---
## Q
Why must a condition-variable wait always be
```java
while (queue.isEmpty()) { notEmpty.await(); }
```
and never `if (queue.isEmpty()) notEmpty.await();`? Two reasons.

## A
- **Spurious wakeups**: the platform may wake a waiter with no signal at all — permitted by POSIX and the JVM.
- **The predicate can be false again by the time you run**: between the signal and reacquiring the lock, another woken (or barging) thread may have consumed the item. `signalAll` deliberately wakes many threads that must re-check.

The loop re-tests the predicate *while holding the lock*, so you only proceed when the condition truly holds. Rule: wait is always inside a loop guarding the predicate.

## Q zh
为什么条件变量 wait 必须在循环中？虚假唤醒是什么？

## A zh
条件变量 wait 必须在循环中（Spurious Wakeups）：

```java
while (!condition) {
    condVar.wait();  // 不要 if (condition)
}
```

原因：
1. **虚假唤醒**：OS 有时在没有相应的 notify 时唤醒线程
2. **竞态条件**：另一个线程可能在 notify 和 wait 方法返回之间改变条件
3. **多个消费者**：一个 notify 可能唤醒多个等待线程，但只有一个应该继续

例子：
```
消费者 1 等待
消费者 2 等待
生产者发送一个项目，notify 一个
消费者 1 唤醒，但... 队列仍然是空的！（消费者 2 已经取走了它）
```

所以总是检查条件后唤醒。
