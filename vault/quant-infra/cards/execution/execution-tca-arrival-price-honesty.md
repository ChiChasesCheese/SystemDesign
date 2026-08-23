---
id: execution-tca-arrival-price-honesty
node: execution.tca
type: qa
---
## Q
A quant on your team argues that VWAP is actually a fine TCA benchmark because "it's just the average price everyone traded at that day, so it's an objective fact about the market, not something we control." Where does this argument break down for an order that's a large fraction of the day's volume?

## A
**VWAP stops being an external, objective fact the moment the order being measured is a large enough share of the day's volume to move VWAP itself — at that point the benchmark is partly made of the very trades it's supposed to be judging.** If a fund's order is, say, 20% of the day's volume, then 20% of the trades that go into computing that day's VWAP *are the fund's own fills*. An algo that trades in a way correlated with the direction VWAP will be pulled — for instance, buying more heavily exactly when the stock is already being bought heavily by others, since that's when volume (and hence VWAP-tracking opportunity) is highest — will mechanically look like it's "tracking VWAP well," because it's helping compose the very number it's compared against. This is an endogeneity problem, not a measurement quirk: you cannot cleanly separate "the algo matched the benchmark" from "the algo's own trading is part of what the benchmark is."

**Arrival price has no such problem, because it's fixed at the moment of the decision, before the algo starts trading at all** — nothing the algo subsequently does can change what the price was when the PM decided to trade. Whatever the algo does next — trade slowly, trade fast, follow the crowd, front-load, whatever — none of it can retroactively move the number it's being scored against. That's the precise sense in which arrival price is exogenous and VWAP, for a large order, is not: one benchmark is set once and can't be gamed by the very strategy being measured against it; the other is co-created, in part, by that strategy. The practical consequence is that "beating VWAP" is a weaker claim the larger the order is relative to the day's volume — exactly when good execution measurement matters most.

## Q zh
你团队里的一位 quant 认为 VWAP 其实是个不错的 TCA 基准，理由是"它就是当天所有人交易的平均价格，是关于市场的一个客观事实，不是我们能控制的东西。"当这笔订单占当天成交量的很大比例时，这个论点会在哪里站不住脚？

## A zh
**一旦被衡量的订单占当天成交量的比例大到足以自己拉动 VWAP，VWAP 就不再是一个外部的、客观的事实了——此时这个基准的一部分，正是由它本该评判的那些成交构成的。** 假设一只基金的订单占当天成交量的 20%，那么用来计算当天 VWAP 的成交中，就有 20% *是这只基金自己的成交*。一个交易方式与 VWAP 会被拉向哪个方向相关的算法——比如恰好在这只股票已经被别人大量买入的时候更用力地买入，因为那正是成交量（也就是跟踪 VWAP 的机会）最高的时候——会在机械意义上显得"很好地跟踪了 VWAP"，因为它本身就在参与构成那个被拿来比较的数字。这是一个内生性问题，不是测量上的小瑕疵：你没法干净地把"算法匹配了基准"和"算法自己的交易就是这个基准的一部分"这两件事分开。

**到达价没有这个问题，因为它在决策那一刻就已经固定下来，早于算法开始交易之前** ——算法之后做的任何事情，都无法改变基金经理决定交易那一刻的价格是多少。无论算法接下来怎么做——慢慢交易、快速交易、跟风、前置执行，随便什么——都无法追溯性地移动它被拿来打分的那个数字。这正是"到达价是外生的，而对一笔大单来说 VWAP 不是"这句话的精确含义：一个基准一旦设定就固定不变，无法被拿来评判它的那个策略本身反向操纵；另一个基准则部分是由那个策略共同创造出来的。实际后果是：订单相对当天成交量越大，"跑赢 VWAP"这个说法就越站不住脚——而这恰恰是良好执行度量最重要的时候。
