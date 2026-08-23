---
id: momentum-cross-sectional-vol-scaling-crowding
node: momentum.cross-sectional
type: qa
---
## Q
Momentum crashes are large but not literally unforecastable — Barroso and
Santa-Clara showed that scaling a momentum portfolio's exposure down when
recent realized volatility spikes materially reduces crash risk and improves
its Sharpe ratio. Given that this fix is well known and momentum is one of
the most widely traded factors in the world, what should you actually expect
the trade-off to be for someone running it today?

## A
**Volatility scaling doesn't eliminate the crash risk, it partially prices
it in ahead of time.** Momentum crashes cluster with spikes in market
volatility (the loser leg's high beta is exactly what makes volatility a
leading indicator of crash risk), so shrinking position size when realized
volatility jumps cuts exposure into the worst months before the worst of the
loss lands. The cost is giving up some of the strategy's average return in
calm periods, since the position is smaller than an unscaled version would
be — you are trading away some carry-forward return for a smoother, less
left-skewed distribution.

Because this fix, and momentum itself, are both extremely well known,
capacity and crowding are the second-order constraint: in the most liquid,
most researched names, the net-of-cost edge left after transaction costs and
crowding is thin, and a volatility-scaled version does not restore the
crowded-out edge — it only reshapes the tail. The practical expectation is
that momentum, even well-managed, behaves less like a strategy that stopped
having a bad year and more like one whose bad years were made shorter and
smaller rather than removed.

## Q zh
动量崩溃很大,但并非完全不可预测——Barroso 和 Santa-Clara 证明,当近期实际
波动率飙升时把动量组合的仓位相应缩小,能显著降低崩溃风险并提升其夏普比率。
既然这个修正方法广为人知,而动量又是全世界交易最拥挤的因子之一,今天运行
这个策略的人实际上应该预期什么样的取舍?

## A zh
**波动率缩放并不能消除崩溃风险,它只是提前把这部分风险定价进仓位里。** 动
量崩溃和市场波动率飙升往往同时出现(输家腿的高 beta 本身就是波动率成为崩
溃风险领先指标的原因),所以当实际波动率跳升时缩小仓位,能在最惨的损失落
地之前就先减少在最坏那几个月里的暴露。代价是在平静时期放弃一部分平均收
益,因为仓位比不做缩放的版本更小——你是在用一部分本可以累积的收益,换取一
个更平滑、负偏更小的分布。

因为这个修正方法和动量本身都已经广为人知,拥挤和容量就成了第二层约束:在
最流动、被研究得最透的股票里,扣除交易成本和拥挤效应之后剩下的净 edge 已
经很薄,而做波动率缩放并不能把已经被套利掉的 edge 找回来——它只是重塑了
尾部形状。实际应该预期的是,即便管理得当,动量表现得不像"不再有糟糕的年
份",而更像是"糟糕的年份被缩短、缩小了,而不是被消除了"。
