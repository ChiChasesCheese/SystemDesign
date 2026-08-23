---
id: data-universe-survivorship-bias-magnitude
node: data.point-in-time.universe
type: qa
---
## Q
You backtest a long-only equity strategy on "all US stocks currently in existence" pulled from today's price database, going back 20 years. Roughly how much does this inflate annualized return relative to a properly point-in-time universe, and what mechanism causes it?

## A
**Survivorship bias from this construction has been estimated at roughly 1-4 percentage points of annualized return, depending on the universe and period** — small-cap and single-country universes with heavier delisting activity sit at the high end, large-cap developed-market universes at the low end. Academic estimates for US mutual funds put the figure near 1.4%/year (Malkiel 1995); equity-index reconstructions with heavy delisting churn have shown gaps several points wider.

The mechanism is simple and brutal: "stocks currently in existence" is a filter applied *today*, so it deletes every company that went bankrupt, got acquired at a loss, or was delisted for failing exchange listing standards — precisely the left tail of the return distribution — while keeping every winner by construction. The backtest never sees a single one of those losses, so its average return is computed only over the survivors, and the effect compounds: the bias grows with the backtest's length and with how much churn the universe actually had, which is why it is far worse for small/micro-cap and emerging-market universes than for the S&P 500.

## Q zh
你用今天的价格数据库里"目前存在的所有美国股票"回测一个多头策略，往前追溯 20 年。相比一个真正做到点时（point-in-time）的股票池，这样构建大约会把年化收益虚高多少？造成这个偏差的机制是什么？

## A zh
**用这种方式构建带来的存活者偏差（survivorship bias），据估计大约会虚高年化收益 1-4 个百分点**，具体取决于股票池和区间——退市活动更频繁的小盘股/单一国家股票池处在高端，大盘发达市场股票池处在低端。关于美国共同基金的学术估计将这一数字定在约每年 1.4%（Malkiel 1995）；退市换手更剧烈的股指重构研究则显示差距还要宽出好几个百分点。

机制既简单又残酷："目前存在的股票"是一个**今天**才施加的过滤条件，所以它删除了每一家破产、被折价收购或因未达交易所上市标准而退市的公司——恰恰是收益分布的左尾——同时因为构造方式而保留了每一个赢家。回测从头到尾看不到这些损失中的任何一笔，所以其平均收益只是在幸存者身上计算出来的，而且这个效应会复合：偏差随回测长度和股票池实际换手程度增长，这也是为什么它对小盘/微盘和新兴市场股票池的伤害远大于对标普 500 的伤害。
