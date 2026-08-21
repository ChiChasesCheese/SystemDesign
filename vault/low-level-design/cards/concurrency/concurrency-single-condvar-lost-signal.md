---
id: concurrency-single-condvar-lost-signal
node: concurrency.patterns
type: qa
---
## Q
Your bounded queue uses **one** condition variable for producers and consumers and wakes with single `signal()`. Tests pass, but under load all threads eventually park forever. Why?

## A
The signal can be **delivered to the wrong class of waiter**. A consumer taking an item signals "state changed" — but the single condition may wake *another consumer*, which re-checks "queue empty", and waits again. The wakeup intended for a producer is consumed and lost; eventually every producer and consumer is parked.

- Fix 1: **two conditions** (`notFull`, `notEmpty`) so a signal targets the right waiters.
- Fix 2: keep one condition but use **`signalAll`** — correct, at the cost of thundering-herd wakeups.

## Q zh
为什么一个条件变量对多个不同的条件不够？

## A zh
问题（丢失信号）：
```java
condVar.wait();  // 消费者等待...什么？
```
- 是队列满（生产者）还是空（消费者）？
- 两个消费者等待
- 生产者添加一个项目，notify
- 第一个消费者取走项目
- 第二个消费者唤醒... 队列现在是空的！

解决方案：
- **每个条件一个 condVar**：
  ```java
  notEmpty.signal();  // 清晰：唤醒等待"不空"的线程
  notFull.signal();
  ```
- 或者在单个 condVar 上使用 `notifyAll()` 并让所有线程重新检查条件（低效）

规则：不同的条件 = 不同的 condVar。
