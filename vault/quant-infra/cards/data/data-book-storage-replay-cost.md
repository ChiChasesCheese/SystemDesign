---
id: data-book-storage-replay-cost
node: data.market-data.book
type: qa
---
## Q
Your team stores full-depth L3 book data for every US-listed stock going back several years, planning to backtest a microstructure strategy against it. Why is this dramatically more expensive to store and replay than the equivalent history of trades or even L2 snapshots, and what do most shops actually do instead?

## A
**L3 message volume is a multiple of trade volume, not a fraction of it — every resting order generates an add, and typically several modify/cancel messages, for every trade that eventually (or never) results from it.** A single marketable order that walks five price levels generates one trade print but potentially dozens of L3 messages as resting orders at each level are partially filled, modified, or cancelled around it, and the vast majority of order-book activity — quotes placed and cancelled without ever trading — never produces a trade at all (cancel rates for liquid names commonly run well above 90% of order messages). Multiplying this across every listed instrument, every trading day, over years produces a message volume that is easily one to two orders of magnitude larger than the trade tape for the same universe and period — full L3 for the whole US equity market can run into the terabytes per day.

Because of this, most shops do not keep full L3 depth for the whole market: they either (1) restrict full-depth capture to a small, deliberately chosen set of symbols relevant to their strategy, (2) keep L3 for a short rolling retention window (days to weeks) and downsample or discard older history, or (3) store L2 (aggregated by price) rather than L3 for the bulk of history, accepting the loss of queue-position information in exchange for an order-of-magnitude storage reduction. Replay compounds the cost: correctly replaying book state requires processing every message in exact sequence — as established in the reconstruction card — so a backtest against full L3 history is not just storage-expensive but compute-expensive, since there is no way to "skip ahead" without periodically re-snapshotting, and getting that snapshot cadence wrong reintroduces exactly the staleness and gap-recovery problems live consumption has to solve.

## Q zh
你的团队保存了美国所有上市股票近几年的全深度 L3 盘口数据，打算用它回测一个微观结构策略。为什么这比保存等长的成交数据、甚至 L2 快照数据要昂贵得多？多数机构实际上是怎么做的？

## A zh
**L3 的报文量是成交量的若干倍，而不是它的一部分——每一笔挂单都会产生一条新增报文，通常还会伴随若干条修改/取消报文，而最终（或永远）由它产生的成交可能只有一笔。** 一笔穿越五档价位的主动成交单只会产生一笔成交打印，但围绕它，各价位上的挂单被部分成交、修改或取消，可能产生多达几十条 L3 报文；而且绝大多数盘口活动——被挂出又被撤销、从未成交过的报价——根本不会产生任何成交（流动性好的标的，报文里的取消比例常常远超 90%）。把这个比例乘以每一个上市标的、每一个交易日、再乘以若干年，产出的报文量很容易比同一股票池同一时期的成交行情大出一到两个数量级——整个美国股票市场的全深度 L3 数据每天可以达到 TB 级别。

正因如此，多数机构并不会为整个市场保存全深度 L3：他们要么（1）只对与自身策略相关的一小批精心挑选的标的做全深度采集，要么（2）只保留一段较短的滚动留存窗口（几天到几周）的 L3，对更早的历史做降采样或直接丢弃，要么（3）对历史的大部分只存 L2（按价格聚合）而不是 L3，用损失队列位置信息换取一个数量级的存储压缩。回放进一步放大了这个成本：正确回放盘口状态需要严格按序列顺序处理每一条报文——正如重建那张卡片所说——所以基于全量 L3 历史的回测不仅存储昂贵，计算也昂贵，因为除非周期性地重新做快照，否则无法"跳着走"，而快照周期设错，又会重新引入实盘消费必须解决的那种过期和缺口恢复问题。
