---
id: execution-sessions-why-close-concentrates-size
node: execution.microstructure.sessions
type: qa
---
## Q
On many US large-cap names, a meaningful double-digit percentage of the entire day's volume prints in the closing auction alone, in a matter of seconds. Continuous trading is open for six and a half hours — why does so much size choose to wait for the last few minutes instead?

## A
**The close is the one moment in the day where the officially-marked price and the price you can actually trade at are guaranteed to be the same number, and a large class of institutional flow is contractually or structurally forced to transact at exactly that number.** Three forces compound:

- **Benchmark-forced flow.** Index funds and ETFs are marked-to-market and judged on tracking error against the index's *official closing level*, which itself is computed from closing auction prints. A passive fund that trades during continuous hours instead of the close accepts tracking-error risk for no benefit — so index rebalances, fund flows, and creation/redemption baskets are executed in the close by design.
- **Single price, no execution-price uncertainty.** Every share in the closing auction fills at the identical clearing price, so a large order has zero risk of "walking the book" or paying a worse average price than smaller orders in the same auction — a cost that is unavoidable in continuous trading, where size against a partially-refilling book pushes the price against you as you go.
- **Liquidity aggregation.** Because so many participants deliberately schedule size into the close (the two effects above are self-reinforcing), the close is genuinely the single deepest liquidity event of the day — which then attracts even more size, since executing against genuinely large size is cheaper per share than trading the same quantity against thinner continuous-session depth.

The consequence for anyone executing a large order: benchmarking to VWAP or arrival price during continuous hours is fighting a liquidity pool that structurally prefers to show up at 3:59:xx, not at 11am.

## Q zh
在很多美股大盘股上，全天成交量中有相当可观的两位数百分比，会在短短几秒钟内集中在收盘拍卖（closing auction）里成交。连续交易时段长达六个半小时，为什么这么多的量偏偏要等到最后几分钟才交易？

## A zh
**收盘是一天当中唯一能保证"官方标记价格"和"你实际能成交的价格"是同一个数字的时刻，而有一大类机构资金流在合同上或结构上被强制要求恰好在这个数字上成交。** 三股力量叠加：

- **被基准强制的资金流。** 指数基金和 ETF 是按市值计价的，考核标准是相对指数**官方收盘水平**的跟踪误差，而这个官方收盘水平本身就是由收盘拍卖的成交价计算出来的。一只被动基金如果在连续交易时段而不是收盘时交易，就是在毫无收益的情况下承担跟踪误差风险——所以指数再平衡、基金申赎、一揽子创设/赎回，设计上就是安排在收盘时执行。
- **单一价格，没有成交价不确定性。** 收盘拍卖里每一股都按同一个出清价成交，所以大单没有"扫穿盘口"或者比同一场拍卖里的小单拿到更差平均价的风险——而这在连续交易里是无法避免的：大量委托打向一个只能部分补充的盘口，会随着成交推进不断把价格推向对你不利的方向。
- **流动性聚集效应。** 正因为这么多参与者都刻意把大单安排到收盘（上面两个效应互相强化），收盘确实是全天流动性最深的一次事件——这又进一步吸引更多的量涌入，因为跟真正的大量对手盘成交，单位股的成本比跟较薄的连续交易盘口成交更低。

这对任何要执行大单的人的后果是：在连续交易时段以 VWAP 或到达价（arrival price）为基准执行，等于是在跟一个结构性地更愿意在 3:59 分几十秒出现、而不是在上午 11 点出现的流动性池对着干。
