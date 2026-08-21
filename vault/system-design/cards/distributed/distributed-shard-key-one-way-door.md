---
id: distributed-shard-key-one-way-door
node: distributed.partitioning.schemes
type: qa
---
## Q
Why is the shard key the highest-stakes decision in a sharded design, and what four properties do you check before committing to one?

## A
Because it is a **one-way door**: the key determines physical placement of every row, so changing it means rewriting the entire dataset. DynamoDB partition keys are immutable — you create a new table and backfill; MongoDB and Vitess have online resharding, but it's a multi-week migration with dual writes and a cutover, not a config change.

Check:

1. **High cardinality** — enough distinct values to exceed your eventual partition count.
2. **Even access distribution**, not just even data distribution (the two differ; a celebrity key is uniform in storage, hot in traffic).
3. **Query alignment** — the key appears in the predicate of your dominant read, or every read becomes scatter-gather.
4. **Transaction/locality alignment** — rows that must be mutated together (order + order_items) hash to the same partition, so you never need a distributed transaction.

Interview move: state the dominant query and the atomicity unit *first*, then derive the key from them.

## Q zh
为什么选择分片键是一个单向门？

## A zh
分片键决定数据如何分布。一旦部署后：
- 改变它需要**重新分片** — 移动所有数据到新分片（停机或复杂的在线迁移）。
- 坏选择会导致**热点**（某些分片承载大部分负载）。
- 不能后来"添加"分片键（已经存储的数据没有新维度）。

单向性：决定后很难更改而不显著中断服务。关键选择点 — 系统设计时必须仔细考虑访问模式和增长。
