---
id: execution-algos-pov-failure-thin-volume
node: execution.algos
type: qa
---
## Q
A POV algo is set to trade at 15% of realized volume for an order expected to take about a day in normal conditions. Volume that day comes in at a fifth of the usual level — pre-holiday, no news, a dead tape. Three days later the order is still only 40% filled. What went wrong structurally, and what should have been the trigger to intervene?

## A
**POV paces strictly off whatever volume actually shows up, with no independent notion of calendar time or urgency — so when volume collapses, the algo doesn't fail loudly, it just quietly falls further and further behind schedule while doing exactly what it was told.** At 15% of a normal day's volume, the order completes in roughly a day as expected. At 15% of a fifth of normal volume, the algo is only trading 15% of a much smaller number, so the *absolute* pace of completion drops to roughly a fifth of what was planned — a one-day order stretches toward five days or more, and the algo has no built-in mechanism to say "I'm behind, speed up" because participation-rate targeting is defined relative to volume, not relative to elapsed time or a deadline.

This produces three compounding costs: **(1) opportunity cost** — if the trade was motivated by a signal with any decay, the alpha that justified the trade in the first place is eroding every extra day the position sits unfilled, and a POV algo has no awareness of that decay. **(2) information leakage** — a resting pattern of consistent, unusually persistent buying (or selling) pressure over several days becomes detectable to other participants, who can trade ahead of the remaining size once the pattern is recognized, which is exactly the footprint cost POV was supposed to minimize by trading passively. **(3) forced late completion under worse conditions** — if a deadline eventually forces the order to finish (a rebalance date, a risk limit, a fund close), the remaining size gets dumped aggressively into whatever liquidity exists then, often at a far worse price than a controlled schedule would have achieved.

**The trigger to intervene should be a participation-rate-independent check** — a minimum completion schedule or an absolute time/quantity floor layered on top of the POV target (e.g., "trade at 15% of volume, but never fall more than X% behind a straight-line schedule") — precisely because pure POV has no mechanism of its own to notice that volume, not urgency, has become the binding constraint.

## Q zh
一个 POV 算法被设置为按已实现成交量的 15% 交易，正常情况下这笔订单预计大约一天能完成。结果那天的成交量只有平时的五分之一——节前、没有消息、行情死气沉沉。三天之后，这笔订单只完成了 40%。从结构上看，问题出在哪里？本该触发人工介入的信号又是什么？

## A zh
**POV 严格按照实际出现的成交量来控制节奏，没有任何独立于日历时间或紧迫性的概念——所以一旦成交量骤降，算法不会大声报错，它只会一声不响地在忠实执行原本指令的同时，越来越落后于计划进度。** 按正常一天成交量的 15% 交易，订单大约一天完成，符合预期。但按只有平时五分之一的成交量的 15% 交易，算法实际交易的只是一个小得多的数字的 15%，所以完成进度的*绝对*速度会降到计划的大约五分之一——原本一天的订单被拖成五天甚至更长，而算法没有任何内置机制会说"我落后了，得加速"，因为参与率目标是相对于成交量定义的，而不是相对于流逝的时间或某个截止日期。

这会带来三重叠加的代价：**（1）机会成本**——如果这笔交易的动机来自一个会衰减的信号，那么仓位多挂一天没成交，最初支撑这笔交易的 alpha 就多流失一分，而 POV 算法对这种衰减毫无感知。**（2）信息泄露**——连续好几天持续、异常持久的买入（或卖出）压力，会形成一种可被其他参与者识别的模式，一旦被识别，他们就能抢在剩余数量之前交易，而这恰恰是 POV 本该通过被动交易来最小化的那种足迹成本。**（3）被迫在更差的条件下仓促完成**——如果最终有一个截止日期强迫这笔订单完成（再平衡日、风险限额、基金关闭），剩余的量就会被激进地砸向当时存在的任何流动性，价格往往远差于一个受控计划本可以达到的水平。

**触发人工介入的信号应该是一个独立于参与率的检查**——在 POV 目标之上叠加一个最低完成进度计划，或者一个绝对的时间/数量下限（比如"按 15% 的成交量交易，但相对一条直线进度计划，落后幅度不得超过 X%"）——这正是因为纯粹的 POV 本身没有任何机制能察觉到，成交量而非紧迫性，已经变成了那个真正的约束条件。
