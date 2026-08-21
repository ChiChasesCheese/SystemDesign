---
id: foundations-when-estimates-change-design
node: foundations.estimation
type: qa
---
## Q
Give three estimate outcomes that each flip a design decision (the whole point of doing the math).

## A
- **Working set fits in RAM** (≲ a few hundred GB) → cache or serve it all from memory; no need to optimize disk paths.
- **Write QPS exceeds a single node** (~tens of thousands for a tuned DB) → partitioning is mandatory, choose a shard key now.
- **Read/write ratio is 100:1+** → invest in caching and read replicas, not write throughput.

If an estimate doesn't change any decision, say so and move on.


## Q zh
一个估算从 10 GB 变成 10 TB。这改变设计吗？为什么？

## A zh
是的。10 GB 适应一个 RAM 缓存或单个 SSD；10 TB 需要分片或对象存储。访问模式改变：

- **10 GB**：主要是全表扫描都可以；缓存热集。
- **10 TB**：必须是索引或分片的；随机访问是核心。

因此估算不是修饰的建议 — 它们直接影响哪些技术可行。规模改变一切。
