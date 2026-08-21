---
id: concurrency-livelock-vs-starvation
node: concurrency.hazards
type: qa
---
## Q
Deadlock, livelock, starvation: distinguish them by what the threads are doing and name the characteristic fix for livelock.

## A
- **Deadlock**: threads blocked forever, consuming no CPU; state never changes.
- **Livelock**: threads actively running and *changing state* but making no progress — e.g. both detect conflict, both back off, both retry in lockstep (the corridor dance). Fix: **randomized backoff/jitter** so retries desynchronize.
- **Starvation**: the system progresses, but *some* thread never gets the resource — unfair locks, reader floods starving writers, priority inversion. Fix: fair queuing / bounded waiting.

Discriminator: check CPU + state changes. Blocked & frozen = deadlock; busy & frozen = livelock; others progress while one lags = starvation.

## Q zh
livelock 和 starvation 之间有什么区别？

## A zh
**Starvation**（饥饿）：
- 一个线程永远无法获得它需要的资源
- 例子：高优先级线程不断运行，低优先级线程从不获得 CPU 时间
- 线程被阻塞，等待变得可用的东西

**Livelock**（活锁）：
- 线程不断改变状态，但没有取得进展
- 例子：两个线程交替放弃资源尝试，进入无限重试循环
```
线程 1：检查资源，它忙，退出
线程 2：检查资源，它忙，退出
线程 1：重试...
```
- 线程在运行，但没有做有用的工作

相似之处：两者都导致缺乏进展。
区别：starvation 是被动等待；livelock 是活跃的无用工作。
