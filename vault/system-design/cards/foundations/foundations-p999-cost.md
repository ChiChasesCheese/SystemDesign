---
id: foundations-p999-cost
node: foundations.numbers
type: qa
---
## Q
Why does each further latency nine (p99 → p999) cost disproportionately more to fix — and when is p999 still worth paying for?

## A
The extreme tail is dominated by effectively **random events** — GC pauses, page faults, TCP retransmits, context switches, background compactions — not your code path, so code optimization stops helping; you're buying overprovisioning, hedging, and isolation instead. Queueing compounds it: one slow request delays everything behind it on that worker.

Worth it when the tail hits the most valuable traffic (Amazon tracks p999 because the slowest requests correlate with the heaviest-data, highest-spend customers) or when fan-out amplifies the tail into the median — [[foundations-tail-latency-amplification]].


## Q zh
为什么工程师关心 p999 延迟虽然少于 0.1% 的请求会那样慢？

## A zh
在高吞吐量下，"少于 0.1%"意味着大数字。在 1M QPS，p999 = 1 秒意味着每秒 1k 个用户等待 1 秒 — 不能接受的。

此外，p999 经常暴露架构缺陷：一个后台任务每小时 stop-the-world 了一次，会在 p999 显示，不在 p50。

因此：报告尾部。它告诉你实际用户体验。
