---
id: foundations-load-parameters
node: foundations.method
type: qa
---
## Q
"Scalable" is meaningless until you describe load. What are load parameters, and how do you pick the right one — e.g. for Twitter's home timeline?

## A
Load parameters are the numbers that describe demand on *your* architecture: QPS per operation, read/write ratio, concurrent connections, cache hit rate, working-set size — and crucially their **distribution**, not just averages.

Pick the parameter the bottleneck actually depends on: Twitter's is not tweet-write QPS (a few k/s) but **followers per user**, because each tweet fans out into ~75 timeline writes and the distribution is extremely skewed (celebrities). Naming the wrong parameter means designing for the wrong problem. See [[foundations-fanout-estimation]].


## Q zh
给定一个产品，哪三个参数形成"一切的起点"？

## A zh
- **DAU**（日活用户）：驱动规模估算；例如 1M DAU，每天产生多少数据？
- **QPS**（每秒查询数）：驱动容量规划；从 DAU 和使用模式估算。
- **数据规模**：驱动存储和索引选择；例如 1TB vs 1PB 改变一切。

这些是参数 — 面试官会给你们或你要求它们。有了数字，设计就变成"对于这个规模什么有效"。
