---
id: execution-fragmentation-router-objective
node: execution.microstructure.fragmentation
type: qa
---
## Q
A naive smart order router sends each child order to whichever venue currently displays the best price. A more sophisticated router sometimes routes to a venue with a worse displayed price instead. What is the sophisticated router actually optimizing for, and why can chasing the best displayed price alone make average execution outcomes worse?

## A
**A good router optimizes expected all-in execution quality — fill probability, realized price after accounting for adverse selection, and net economics after fees and rebates — not the single number printed as the best displayed quote.** Chasing the best display price alone breaks down for several concrete reasons:

- **Stale or fleeting quotes.** As covered in the NBBO-you-can't-trade card, the best displayed price on a given venue may not survive the round-trip to that venue — routing there repeatedly can mean repeatedly missing, at a real cost of delay and information leakage from the failed attempts (other participants can detect a router that keeps probing and pulling back).
- **Adverse selection by venue.** Not all venues' resting liquidity is equally "toxic." Fill rates at the best price on a venue that attracts a disproportionate share of informed/aggressive flow tend to come with worse post-trade markout (the price moves against you right after you fill) than the same nominal price on a venue with calmer flow — so two venues showing the identical best price are not offering the identical expected outcome.
- **Maker-taker fee/rebate structure.** Venues charge takers and pay makers (or the reverse, on "inverted" venues) different amounts per share; a venue with a marginally worse displayed price but a better net fee can still be cheaper all-in, and a router blind to fees systematically overpays.
- **Footprint and signaling cost.** Always routing to the single best-priced venue creates a detectable pattern; splitting size across venues (even ones with a nominally worse price) can reduce the probability that the router's own activity is identified and traded against.

The consequence of optimizing only for displayed price: a router that looks correct order-by-order (it always "got the best price shown") can still produce systematically worse realized execution than one that weighs fill probability, adverse selection, and fees — which is exactly why real transaction cost analysis measures realized outcomes against a benchmark like arrival price, not against whether each child order matched the quote it was routed to.

## Q zh
一个朴素的智能路由器，会把每一笔子单发送到当前显示最优价格的交易所。而一个更精细的路由器，有时反而会把单子路由到一个显示价格更差的交易所。这个更精细的路由器实际在优化什么？为什么单纯追逐最优显示价格，反而可能让平均执行结果变差？

## A zh
**一个好的路由器优化的是预期的全口径执行质量——成交概率、扣除逆向选择后的实际价格，以及扣掉手续费和返佣后的净经济性——而不是屏幕上打出的那一个"最优显示报价"数字。** 单纯追逐最优显示价格，会在好几个具体方面出问题：

- **过时或转瞬即逝的报价。** 正如"你看到的 NBBO 不是你能交易的 NBBO"那张卡片讲的，某个交易所显示的最优价格未必能撑到你的委托实际到达那里的往返时间——反复路由过去，可能意味着反复扑空，付出的是延迟的真实成本，以及失败尝试带来的信息泄露（其他参与者能识别出一个反复试探又撤回的路由器）。
- **按交易所划分的逆向选择程度不同。** 并非所有交易所的挂单流动性都同样"干净"。在一个吸引了不成比例份额的知情/激进资金流的交易所上，以最优价成交，往往伴随着比在资金流更平静的交易所上同样名义价格更差的成交后走势（markout）（你一成交价格就立刻朝对你不利的方向走）——所以两个显示同样最优价的交易所，提供的预期结果并不相同。
- **Maker-taker 手续费/返佣结构。** 不同交易所对吃单方收费、对挂单方返佣（或者在"反向"交易所则相反）的每股金额不同；一个显示价格稍差、但净费用更优的交易所，全口径算下来仍可能更便宜，而一个对手续费视而不见的路由器会系统性地多付钱。
- **足迹和信号成本。** 总是把单路由到单一最优价交易所，会形成一个可被识别的模式；把量拆分到多个交易所（哪怕其中一些名义价格更差），能降低路由器自身活动被识别并被对手交易利用的概率。

只优化显示价格的后果是：一个逐笔看起来都"正确"（每次都拿到了路由过去时显示的最优价）的路由器，实际实现的执行结果仍可能系统性地比一个权衡了成交概率、逆向选择和手续费的路由器更差——这正是为什么真正的交易成本分析（TCA）是把实现结果拿去和到达价（arrival price）这样的基准比较，而不是看每一笔子单有没有匹配上它被路由过去时的那个报价。
