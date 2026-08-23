---
id: execution-algos-almgren-chriss-tradeoff
node: execution.algos
type: qa
---
## Q
An Almgren-Chriss execution schedule for a risk-neutral trader reduces to trading evenly across the horizon (TWAP-like). A highly risk-averse trader given the exact same order, same horizon, same market gets a front-loaded schedule instead. What single parameter changes between them, and what trade-off does it actually control?

## A
**The risk-aversion parameter (often written λ or γ) controls how much the trader is willing to pay in extra impact cost to reduce the variance of their execution outcome — and that single dial is what moves the optimal schedule from flat to front-loaded.**

Almgren-Chriss frames execution as minimizing a combination of **expected cost** (impact, which is lower the slower and more evenly you trade) and **variance of cost** (timing risk — the price can move against the still-unexecuted remainder while you wait, and the longer that remainder sits open, the more variance it's exposed to). A **risk-neutral trader** (λ = 0) only cares about expected cost, so the optimal solution just minimizes impact — which, since impact rises with the square of trading rate under linear temporary-impact assumptions, means trading at a constant, even rate: TWAP-like. A **risk-averse trader** cares about variance too, and since variance accumulates the longer a position sits unexecuted, the optimum shifts toward **front-loading**: trade more, faster, early — accepting a higher expected impact cost now — specifically to shrink the size of the exposed remainder sooner and cut the total variance the position is exposed to over the horizon.

The consequence for anyone configuring an execution algo: risk aversion isn't a cosmetic knob, it's the parameter that trades a *known, certain* cost (impact) against an *uncertain* one (timing risk) — cranking it up buys predictability of outcome at a real, quantifiable price, and the "right" setting depends on how much the trader (or the fund's risk tolerance) actually cares about variance versus expected cost for that specific order.

## Q zh
一个风险中性交易者对应的 Almgren-Chriss 最优执行计划，会退化成在整个执行期内均匀交易（类似 TWAP）。同一笔订单、同样的期限、同样的市场条件，交给一个高度厌恶风险的交易者，得到的却是一个前置（front-loaded）的执行计划。两者之间变化的是哪一个参数？这个参数实际控制的是什么权衡？

## A zh
**风险厌恶参数（常写作 λ 或 γ）控制的是交易者愿意多付多少额外的冲击成本，来换取执行结果方差的降低——正是这一个旋钮，把最优执行计划从"平坦"变成了"前置"。**

Almgren-Chriss 把执行问题表述为最小化**预期成本**（冲击成本，交易越慢、越均匀，冲击越低）和**成本方差**（时机风险——在你等待的过程中，价格可能朝不利于剩余未成交仓位的方向变动，这部分仓位敞开的时间越长，暴露的方差越大）二者的组合。**风险中性交易者**（λ = 0）只在乎预期成本，所以最优解就是单纯最小化冲击——在线性暂时冲击假设下，由于冲击随交易速率的平方上升，这意味着以恒定、均匀的速率交易：类似 TWAP。**风险厌恶交易者**同时在乎方差，而由于方差会随着仓位敞开时间越长不断累积，最优解就会朝**前置**方向偏移：早一点、快一点多交易——现在就接受更高的预期冲击成本——具体目的是尽早缩小暴露在外的剩余仓位规模，从而削减整个执行期内仓位所暴露的总方差。

对任何配置执行算法的人的后果是：风险厌恶不是一个装饰性旋钮，而是一个把*确定已知*的成本（冲击）拿去和*不确定*的成本（时机风险）做权衡的参数——把它调高，能用一个真实的、可量化的价格，换来结果的可预测性；至于"正确"的设置该是多少，取决于交易者（或基金的风险偏好）对这笔具体订单而言，究竟有多在意方差、相对预期成本又有多在意。
