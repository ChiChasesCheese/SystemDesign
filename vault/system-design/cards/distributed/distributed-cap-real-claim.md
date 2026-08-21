---
id: distributed-cap-real-claim
node: distributed.cap
type: qa
---
## Q
What does the CAP theorem actually constrain — and why is calling a system "CA" a red flag in an interview?

## A
It constrains behavior **only during a network partition**: a replicated system must then either refuse some requests (choose **C**, staying linearizable) or answer with possibly-stale/divergent data (choose **A**). It says nothing about normal operation.

"CA" is a red flag because partitions are not optional in a distributed system — you can't choose to forfeit P; you can only choose what to sacrifice *when* one happens. Also note "C" here means linearizability and "A" means every non-failed node answers — much narrower than everyday "consistency" and "high availability".

## Q zh
CAP 定理的真实含义是什么？（不是不能选三个，而是...）

## A zh
**真实含义**：在网络分区下，必须在**一致性**和**可用性**之间做权衡。没有分区的情况下，可以同时满足所有三个。更准确的说法：系统设计者需要考虑分区发生时的行为。要么等待分区愈合（优先一致性），要么继续操作接受不一致（优先可用性）。分区是否经常发生决定了应该优先哪个。容易被误解成："一个系统不能选 CA+P+C"，实际上是 "在分区时只能选 AP 或 CP"。
