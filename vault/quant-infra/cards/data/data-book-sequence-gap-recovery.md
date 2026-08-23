---
id: data-book-sequence-gap-recovery
node: data.market-data.book
type: qa
---
## Q
Your feed handler is applying book deltas by sequence number and detects it just processed sequence 104,882 followed immediately by 104,885 — three messages are missing, probably lost on the wire. What must the system do before it lets any downstream strategy or feature read the book again, and what happens if it just keeps applying messages as they arrive?

## A
**It must stop treating the book as trustworthy, resynchronize from a fresh source of truth, and only then resume — never silently continue applying later messages on top of a known-incomplete state.** The standard recovery path: mark the book **stale/invalid** the instant a sequence gap is detected; either request the missing messages from a **retransmission/gap-fill channel** many venues provide specifically for this (a side channel that replays a bounded range of past sequence numbers) or, if that's unavailable or the gap is large, discard the current book entirely and rebuild from the **next full snapshot** the venue publishes. Only once the book is known to be complete and in-sequence again should downstream consumers be allowed to read it.

If the system instead just keeps applying messages 104,885 onward without resolving the gap, every field derived from the book is now silently wrong in an unbounded way: three deletes it never processed leave phantom orders in the book that no longer exist, size at a price level is off by however much those three messages would have changed it, and every downstream feature computed from book state — order-book imbalance, queue-position estimates, a quoted-spread feature, a passive-fill probability model — inherits the corruption without any error being raised, because applying a delta is a well-formed operation regardless of whether the base state under it is correct. This is the core reason book data is treated as expensive and fragile relative to trade data: a single dropped packet propagates silently into every feature built on the book until an explicit gap check catches it, and the check has to run continuously, not as a periodic audit.

## Q zh
你的行情处理程序正在按序列号应用盘口增量，检测到刚处理完序列号 104,882，紧接着收到的是 104,885——中间有三条报文缺失，很可能是在传输中丢失了。在允许任何下游策略或特征再次读取这份盘口之前，系统必须做什么？如果它只是继续应用后续到达的报文会发生什么？

## A zh
**它必须停止把这份盘口当作可信的，从一个新的可信来源重新同步，然后才能恢复——绝不能悄悄地在一个已知不完整的状态之上继续应用后续报文。** 标准的恢复路径是：一旦检测到序列缺口，立刻把盘口标记为**过期/无效**；接着要么向许多交易场所专门为此提供的**重传/补漏通道**（一个可以重放一段有界历史序列号范围的旁路通道）请求缺失的报文，要么在该通道不可用或缺口过大时，彻底丢弃当前盘口，从该场所发布的**下一份完整快照**重建。只有当盘口再次确认完整且序列连续之后，才应该允许下游消费方读取它。

如果系统不解决这个缺口、而是直接继续应用从 104,885 开始的后续报文，那么每一个由盘口衍生出的字段现在都以一种无界的方式悄悄出错了：三条从未处理过的删除报文，会在盘口里留下本已不存在的幽灵挂单；某个价位上的数量，会因为这三条报文原本会造成的变化而出现偏差；每一个基于盘口状态计算的下游特征——订单簿失衡（order-book imbalance）、队列位置估计、报价点差特征、被动成交概率模型——都会在不触发任何报错的情况下继承这种损坏，因为应用一条增量本身是一个格式良好的操作，与它所叠加的基础状态是否正确无关。这正是盘口数据相对于成交数据被视为昂贵且脆弱的核心原因：一个被丢弃的数据包会悄悄传播进所有基于盘口构建的特征里，直到一次明确的缺口检测把它抓出来为止，而且这项检测必须持续运行，而不能是周期性的审计。
