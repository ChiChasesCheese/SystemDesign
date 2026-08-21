---
id: distributed-data-skew-vs-access-skew
node: distributed.partitioning.skew
type: qa
---
## Q
Distinguish data skew from access skew. Which remedies apply to each, and which remedy is useless for one of them?

## A
- **Data skew**: one partition holds disproportionate *bytes/rows* (a range partition on `country` where one country is 60% of users; a tenant with 100x the data). Symptoms: disk pressure, slow compactions/repairs on one node, uneven backup times.
- **Access skew (hot key/hot partition)**: bytes are fine, *traffic* is concentrated — a celebrity row, a "current day" bucket.

| Remedy | Data skew | Access skew |
|---|---|---|
| Split the range further | works | works only if the heat spans many keys |
| Salt the key | overkill | works (writes) |
| Cache in front | useless | works (reads) |
| Move the partition to a bigger node | works | useless — it's one key, and one node still serves it |

The useless-for-access-skew one to name out loud: **rebalancing/adding nodes**. It redistributes keys, and access skew concentrated on a *single* key is indivisible by any partitioning scheme. Managed systems blur this: DynamoDB's adaptive capacity will isolate a hot partition automatically, but still cannot exceed the per-partition-key ceiling (~3000 RCU / 1000 WCU).

## Q zh
数据倾斜和访问倾斜的区别是什么？分别怎样缓解？

## A zh
**数据倾斜**：某些 key 对应的数据量远大于平均值（e.g., 一个用户有 100GB 数据，其他用户只有 1GB）。结果是分片大小不均匀。缓解方式：子分片（micro-sharding）：将热 key 进一步分成多个小分片。按值范围分片（range-based）：细粒度划分范围。

**访问倾斜**：某些 key 被访问频率远高于平均（e.g., 明星用户、热点新闻）。结果是某个分片的请求量超载。缓解方式：多层缓存：在副本层、节点层添加缓存。热 key 专用缓存或本地副本。读取分散：指定副本处理热 key 读取。
