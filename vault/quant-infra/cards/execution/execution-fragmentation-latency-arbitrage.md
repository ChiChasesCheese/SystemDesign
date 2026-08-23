---
id: execution-fragmentation-latency-arbitrage
node: execution.microstructure.fragmentation
type: qa
---
## Q
A stock trades on 12 different lit venues simultaneously. A large trade prints on venue A that moves the true price. A latency-arbitrage trader immediately buys against still-unchanged, now-stale quotes on venues B through L before those venues' market makers can react. State the mechanism in one sentence, and then explain who actually pays for it.

## A
**Latency arbitrage is trading against quotes on slower venues before their market makers can update them to reflect information a faster participant already has from a venue (or a direct feed) they saw first.** The mechanism requires only two ingredients: fragmentation (the same economic security quoted independently on many venues, so a price move on one doesn't mechanically update the others) and a latency gap (some participants observe the price-moving event microseconds to low-milliseconds before others, whether because of physical distance to the matching engine, direct-feed versus SIP access, or raw processing speed).

**The market makers whose stale quotes get hit pay directly** — they are picked off at a price that is already wrong by the time the trade executes against them, a pure loss with no offsetting information advantage. This cost does not disappear; it gets **passed through to everyone who trades against those market makers' quotes in normal conditions**, because a market maker who expects to be picked off by faster participants a known fraction of the time must widen their quoted spread to all other flow to stay profitable on average. So the practical consequence for a strategy that isn't itself doing latency arbitrage: the spreads you cross every day are wider than they would be in a single, unfragmented, uniform-latency market, because market makers are pricing in the latency-arb tax as a cost of doing business across a fragmented set of venues.

## Q zh
一只股票同时在 12 家不同的明面交易所交易。在 A 交易所有一笔大单成交，推动了真实价格。一位做延迟套利的交易者，赶在 B 到 L 这些交易所的做市商能反应过来之前，立刻对这些交易所里那些还没变、已经过时的报价下单买入。用一句话说明这个机制，然后说明这个成本最终由谁承担。

## A zh
**延迟套利就是在更慢的交易所的做市商还来不及把报价更新到反映信息之前，用更快的参与者已经从他们先看到的某个交易所（或直连行情）获得的信息，去打这些过时的报价。** 这个机制只需要两个要素：分割化（同一个证券在许多交易所各自独立报价，一个地方的价格变动不会机械地同步到其他地方）和延迟差（某些参与者比其他人早若干微秒到低毫秒观察到价格变动事件，无论原因是离撮合引擎的物理距离、直连行情 vs SIP 的访问权限，还是纯粹的处理速度）。

**报价被打中的那些做市商直接承担成本**——他们被以一个成交时已经错误的价格"打中"，这是纯粹的损失，没有任何信息优势作为补偿。这个成本不会凭空消失；它会**转嫁给所有在正常情况下与这些做市商报价交易的人**，因为一个预期会有一定比例的时间被更快的参与者打中的做市商，必须把对所有其他资金流报出的价差拉宽，才能维持平均意义上的盈利。所以对一个自己并不做延迟套利的策略来说，实际后果是：你每天穿过的价差，比在一个单一、未分割、延迟统一的市场里本应有的价差要宽——因为做市商把延迟套利这项税，作为在分割化的众多交易所之间做生意的成本，定价进了报价里。
