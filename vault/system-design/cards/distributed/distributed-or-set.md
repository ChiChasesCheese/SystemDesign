---
id: distributed-or-set
node: distributed.crdt
type: qa
---
## Q
Replicated set: replica A removes element x while replica B concurrently re-adds x. Why do naive sets and 2P-Sets get this wrong, and how does an OR-Set resolve it?

## A
- **Naive set**: add/remove don't commute, so replicas that see them in different orders diverge — no well-defined answer.
- **2P-Set**: removals go to a tombstone set that wins forever — once removed, x can **never be re-added**.
- **OR-Set (observed-remove)**: every add attaches a **unique tag**; remove deletes only the tags the remover had *observed*. B's concurrent re-add carries a fresh tag A never saw, so it survives the merge — **add wins over concurrent remove**, and re-adding after removal works.

Cost: tag/tombstone metadata grows with operations and needs eventual compaction. LWW-element-sets avoid the metadata but inherit timestamp data loss ([[distributed-lww-danger]]).

## Q zh
什么是 OR-Set（观察-移除集）？它如何处理并发的加和移除？

## A zh
一种 CRDT 表现为集合，其中：
- 每次加入都分配唯一 ID（如 (元素, 副本ID, 计数)）。
- 移除跟踪看到过哪些加入 ID，而不是存储元素本身。
- 并发加入和移除不会冲突：即使一个副本移除，在另一个副本上并发看不见的加入也会在同步后出现。

好处：不需要全局协调；所有副本最终保证相同的集合。缺点：内存开销（跟踪历史 ID）。
