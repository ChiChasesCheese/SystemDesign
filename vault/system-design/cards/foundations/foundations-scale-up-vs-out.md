---
id: foundations-scale-up-vs-out
node: foundations.tradeoffs
type: qa
---
## Q
When do you keep scaling *up* (bigger machine) instead of *out* (more machines), and what eventually forces the switch?

## A
Scale up while you can: no partitioning, no rebalancing, no distributed failure modes — and a single 2026 box goes further than people assume (TBs of RAM, millions of IOPS). Costs: price grows superlinearly with size, and there's a hard ceiling.

Forced out by: load beyond the biggest box, **availability** (one machine is one failure domain), or geographic latency requiring presence in multiple regions.

DDIA's point: distribution adds irreducible complexity — go distributed when a number forces you, never by default.


## Q zh
Scale-up（更大的机器）vs scale-out（更多的机器）：各自何时是正确的选择？

## A zh
- **Scale-up**（更大的机器）：简单，没有分布式复杂性；但受单机物理限制（RAM、CPU 核心数）。在无状态计算中使用，直到单机成为瓶颈。
- **Scale-out**（更多的机器）：打破单机限制；但引入分布式的复杂性：分片、故障恢复、网络分区。为**有状态**存储和无法在单机上工作的工作负载保留。

规则：首先 scale-up（简单）；只有当你用完了单机资源或有状态复杂性强制时才 scale-out。
