---
id: execution-sessions-continuous-assumption-breaks
node: execution.microstructure.sessions
type: qa
---
## Q
A POV (percentage-of-volume) algo is slicing a large order, targeting 10% of continuously-traded volume, when the stock gets halted for five minutes and later closes with 15% of the day's volume printing in the closing auction. Name two distinct ways this breaks the algo's core assumption, and what each one costs.

## A
**The algo assumes volume is a continuous stream it can always take a fixed slice of; both events replace continuous matching with a single-price batch clear that the algo isn't built to participate in the same way.**

- **The halt:** for five minutes, there is zero continuous volume to be 10% of — the algo doesn't get "10% of nothing," it simply stalls, accumulating unfilled shares while its schedule silently falls behind. If the algo then tries to catch up immediately after reopening — a period when the reopening auction has just cleared and the book is often at its thinnest and most uncertain, before normal two-sided liquidity has rebuilt — pushing the remaining shares in fast means paying much higher impact than the same shares would have cost against a normal, replenished book. The cost is either **schedule slippage** (silently falling behind, extending completion and opportunity cost) or **a burst of bad-price impact** if the algo compensates by trading aggressively into thin post-reopen liquidity.
- **The close:** 15% of the day's volume clearing in one auction print means the algo's "percentage of continuous volume" target was computed against a shrinking base — it was never designed to bid into a call auction, so unless it has explicit auction logic, it either sits out the single richest liquidity event of the day (forgoing the cheapest fills available) or has to be manually routed into an MOC/LOC (market/limit-on-close) order type that behaves nothing like its continuous child-order logic.

Both failures share a root cause: **continuous participation-rate algos are built on the assumption that liquidity is a steady flow they can sample proportionally, and a call auction or a halt is, by construction, not a flow — it's a single discrete event with no intermediate fills**, so an algo that only knows how to slice a stream has nothing to slice during either one.

## Q zh
一个 POV（percentage-of-volume）算法正在拆分一笔大单，目标是吃到连续成交量的 10%，这时股票突然被熔断暂停 5 分钟，随后收盘时又有 15% 的全天成交量在收盘拍卖中一次性成交。指出这如何以两种不同的方式打破了该算法的核心假设，并说明各自的代价。

## A zh
**这个算法假设成交量是一条可以随时按固定比例切一片的连续流；而这两个事件都是把连续撮合换成了一次性的单价批量出清，算法根本没有为参与这种机制而设计。**

- **熔断：** 5 分钟内根本没有连续成交量可供它取 10%——算法不会"吃到 0 的 10%"，它只会停滞，未成交的量不断堆积，交易进度在悄悄落后于计划。如果算法在重新开盘后立刻想追回进度——这段时间恰恰是重新开盘拍卖刚出清、盘口往往最薄、最不确定，正常的双边流动性还没重新建立起来的时候——把剩余的量快速推出去，付出的冲击成本会远高于在正常、已补充好的盘口上成交同样的量。代价要么是**进度滑移**（悄悄落后，拖长完成时间、产生机会成本），要么是**一波糟糕价位的冲击成本**（如果算法通过在重新开盘后的薄流动性中激进交易来补进度）。
- **收盘：** 全天 15% 的成交量在一次拍卖成交中出清，意味着算法"占连续成交量百分比"这个目标的计算基数本身在缩水——它从来就不是为向一场集合竞价报价而设计的，所以除非算法内置了专门的拍卖逻辑，否则要么坐视全天流动性最丰厚的这一次事件白白错过（放弃本可获得的最便宜成交），要么必须手动改路由到 MOC/LOC（市价/限价收盘单）这种和它连续子单逻辑完全不同的订单类型。

这两种失败有一个共同的根源：**连续参与率算法建立在"流动性是一条可以按比例持续采样的稳定流"这个假设上，而集合竞价或熔断，从设计上就不是一条流——它们是没有中间成交的单一离散事件**，所以一个只会切分连续流的算法，在这两种情况下都没有东西可切。
