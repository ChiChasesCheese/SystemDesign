---
id: data-bars-consolidated-vs-direct-feed
node: data.market-data.bars
type: qa
---
## Q
A backtest uses consolidated-tape (SIP) timestamps to decide when a signal "could have" acted on a print. The strategy is later deployed on direct exchange feeds. Why does this backtest systematically overstate how early the strategy sees information, and what is the actual mechanism for the gap?

## A
**The consolidated feed (the SIP — Securities Information Processor, e.g. the US CTA/UTP tape) aggregates trade and quote messages from every venue, and that aggregation itself takes time** — each venue reports to the SIP over its own connection, the SIP timestamps and re-disseminates, and by construction this adds latency on top of each venue's own matching-engine time. That gap has historically run from roughly the tens of microseconds up to single-digit milliseconds depending on venue and period, small in absolute terms but often larger than the reaction-time budget of a fast strategy, and it is *not* the delay a firm that subscribes to a venue's **direct feed** experiences — a direct feed is that single venue's proprietary output, received with only the network/wire latency between that venue and the subscriber, none of the SIP's aggregation and re-broadcast overhead.

A backtest built on SIP timestamps therefore systematically **understates** how stale a SIP-based live system's information really is relative to what a direct-feed participant already knows and has acted on — the price the SIP shows "now" may already be several venues and microseconds-to-milliseconds behind the true current best price on the fastest direct feed. Two consequences follow: (1) a backtest that assumes it can react to a SIP quote instantly is implicitly assuming better information than a SIP-based live system will ever have, and (2) if the live system trades against direct-feed participants (which most high-frequency counterparties are), it is systematically the slower, more-informed-against party — the backtest never models this adverse-selection gap at all.

## Q zh
一个回测使用合并行情（SIP）时间戳来判断某个信号"本可以"对哪笔成交做出反应。该策略之后被部署在直连交易所行情（direct feed）上。为什么这个回测会系统性地高估策略能多早看到信息？造成这个差距的实际机制是什么？

## A zh
**合并行情（SIP，即 Securities Information Processor，例如美国的 CTA/UTP 行情）会汇总来自每个交易场所的成交和报价报文，而这个汇总过程本身就需要时间**——每个场所通过自己的连接向 SIP 上报，SIP 打上时间戳并重新分发，这在每个场所自身撮合引擎时间之上，天然又叠加了一层延迟。这个差距历史上大致在几十微秒到个位数毫秒之间，具体取决于场所和时期，绝对数值不大，但往往超过一个快速策略的反应时间预算，而且它*不是*订阅某个场所**直连行情（direct feed）**的机构所经历的延迟——直连行情是该场所专有的输出，接收方只承受该场所与订阅方之间的网络/线路延迟，没有 SIP 那层汇总与再广播的开销。

因此一个基于 SIP 时间戳构建的回测，会系统性地**低估**一个基于 SIP 的实盘系统的信息究竟有多陈旧——相对于最快直连行情上的参与者已经知道并已经据此行动的真实当前最优价，SIP 此刻显示的价格可能已经落后好几个场所、慢了几微秒到几毫秒。由此有两个后果：（1）一个假设自己能对 SIP 报价瞬时做出反应的回测，隐含地假设了一个基于 SIP 的实盘系统永远不可能拥有的更好信息；（2）如果实盘系统是在和直连行情的参与者对手方交易（大多数高频对手方确实如此），它就系统性地处于更慢、被对方更充分了解的一方——而回测从头到尾都没有对这个逆向选择（adverse selection）差距建模。
