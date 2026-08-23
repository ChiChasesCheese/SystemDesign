---
id: execution-impact-square-root-law
node: execution.impact
type: qa
---
## Q
Fund A trades $10M in a mega-cap stock with $2B daily volume — a 0.5% participation rate — and pays roughly 0.5 bps of impact. Fund B trades $100M in the same stock, a 5% participation rate — ten times the order size, but not ten times the cost. Using the square-root law, roughly what multiple of impact should Fund B expect, and what does that ratio tell you about how liquidity actually works?

## A
**Fund B's impact should scale with the square root of the participation-rate ratio — √10 ≈ 3.2× — not with the 10× size ratio, so Fund B pays about 1.6 bps rather than the naive 5 bps a linear model would predict.** The square-root law states:

`impact (bps) ≈ k · σ · √(order size / ADV)`

where σ is daily volatility and k is an empirically calibrated constant (roughly 0.1 in standard calibrations). The participation rate — order size divided by average daily volume — is the input that matters, and it enters under a square root rather than linearly.

The **participation-rate intuition** behind the square root: liquidity isn't a fixed pool you draw down proportionally — it's continuously replenished by natural order flow arriving throughout the trading window, and a bigger order interacts with proportionally more of that replenishment simply because it takes longer (or is worked more broadly) to complete. Doubling an order doesn't require doubling the price concession, because the market has more time and more natural counter-flow to absorb the larger quantity against. This is also *why* the relationship is concave rather than linear or convex: the marginal cost of the next dollar traded falls as order size grows relative to the fixed daily volume base, but it never falls to zero — cost keeps rising, just more slowly than size. That combination — rising, but sub-linear — is exactly what sets up the capacity ceiling discussed on the companion card: returns to scale are real but diminishing, not free.

## Q zh
A 基金在一只日成交额 20 亿美元的大盘股上交易 1000 万美元，参与率 0.5%，支付了大约 0.5 个基点的冲击。B 基金在同一只股票上交易 1 亿美元，参与率 5%——订单规模是 A 的 10 倍，但成本不是 10 倍。用平方根冲击律估算，B 基金大致应该预期多少倍的冲击？这个比例说明了流动性到底是怎么运作的？

## A zh
**B 基金的冲击应该按参与率之比的平方根来放大——√10 ≈ 3.2 倍——而不是按 10 倍的规模比例放大，所以 B 基金付出的大约是 1.6 个基点，而不是线性模型天真预测的 5 个基点。** 平方根冲击律表述为：

`冲击（bps） ≈ k · σ · √(订单规模 / ADV)`

其中 σ 是日波动率，k 是一个经验标定出的常数（标准标定下大约是 0.1）。真正起作用的输入是**参与率**——订单规模除以日均成交量——而且它是以平方根、而不是线性的方式进入这个公式的。

平方根背后的**参与率直觉**是：流动性不是一个按比例被抽取的固定池子——它是在整个交易窗口内被持续到来的天然订单流不断补充的，而一笔更大的订单恰恰因为需要更长时间（或被分散执行得更广）才能完成，从而能够按比例地吸收到更多这种补充流动性。把订单规模翻倍，并不需要把价格让步也翻倍，因为市场有更多的时间、更多的天然对手盘流量来吸收这笔更大的数量。这也正是为什么这层关系是**凹的（concave）**而不是线性或凸的：随着订单规模相对于固定的日成交量基数增大，下一美元交易的边际成本会下降，但永远不会降到零——成本始终在上升，只是上升得越来越慢。这种"持续上升、但次线性"的组合，恰恰构成了配套卡片讨论的容量上限（capacity ceiling）的基础：规模效应是真实存在的，但是递减的，不是免费的。
