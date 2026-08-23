---
id: execution-impact-nonlinear-in-urgency
node: execution.impact
type: qa
---
## Q
You need to trade a fixed quantity Q. Compressing the execution window from 4 hours to 2 hours roughly doubles your participation rate. Under the square-root law, does your total impact cost for the order double as well? Walk through why urgency is expensive in a way that compounds rather than adds.

## A
**No — total cost rises by roughly √2 (≈1.4×), not 2×, for that one compression, but each further compression buys proportionally less time-risk reduction for a steeper cost increase, which is what makes urgency expensive in a compounding rather than linear way.**

Per the square-root law, impact per unit traded scales with √(participation rate). Halving the execution window roughly doubles the participation rate (same Q, half the time), so per-unit cost rises by √2, and since total cost is (cost per unit) × Q with Q fixed, **total cost for the order also rises by √2** for that step. That in isolation sounds mild — but the relationship compounds as you keep compressing: going from 4 hours → 2 hours → 1 hour → 30 minutes multiplies participation rate by 2 each time, and cost keeps rising by √2 at each halving, so cost as a function of *inverse* time is itself convex — each successive compression buys a smaller reduction in the time you're exposed to the market, for a bigger jump in execution cost, because you're moving further up a concave-in-size, but ever-steeper-in-rate, cost curve as the window shrinks toward zero.

This is exactly the tension **Almgren-Chriss formalizes as a trade-off, not a free choice**: compressing the window reduces **timing risk** (the variance of the price while your remaining position sits unexecuted — less time exposed means less variance) but only in exchange for impact cost that rises faster than the time saved, once you're already trading reasonably fast. Near the risk-neutral end (long, unhurried schedules), adding urgency is cheap because you're on the flat part of the curve; near maximum urgency, the same absolute increase in speed costs far more in impact than it saves in timing-risk reduction. That's the mechanism behind "impact is non-linear in urgency" — it isn't that urgency has some fixed extra fee, it's that the cost curve gets steeper exactly where you're pushing it.

## Q zh
你需要交易一个固定数量 Q。把执行窗口从 4 小时压缩到 2 小时，大致会让你的参与率翻倍。在平方根冲击律下，这笔订单的总冲击成本也会翻倍吗？请说明为什么"紧迫"带来的是一种复合式而非线性叠加式的昂贵。

## A zh
**不会——就这一次压缩而言，总成本大致上升 √2（约 1.4 倍），而不是 2 倍，但每一次进一步压缩，换来的时机风险下降会越来越少，而成本上升却越来越陡，这正是"紧迫"以复合而非线性方式变昂贵的原因。**

按照平方根冲击律，单位交易量的冲击按 √(参与率) 缩放。把执行窗口砍半，大致会让参与率翻倍（同样的 Q，一半的时间），所以单位成本上升 √2；由于总成本等于单位成本乘以 Q，而 Q 固定不变，**这笔订单的总成本这一步也上升 √2**。单独看这一步，听起来还算温和——但这层关系会随着你不断压缩而复合累加：从 4 小时 → 2 小时 → 1 小时 → 30 分钟，每一次都让参与率翻倍，而每一次砍半成本都再上升 √2，所以成本作为*时间倒数*的函数本身是凸的——随着窗口不断收窄趋近于零，每一次进一步压缩，换来的暴露时间缩短越来越小，而执行成本的跳跃却越来越大，因为你正在一条"对规模是凹的，但对速率越来越陡"的成本曲线上，越走越靠上。

这恰恰是 **Almgren-Chriss 把它形式化为一种权衡、而非免费选择**的那层张力：压缩窗口能降低**时机风险（timing risk）**（剩余未成交仓位暴露期间价格的方差——暴露时间越短，方差越小），但只有当你本就交易得相当快的时候，才需要用上升更快的冲击成本来换取这个好处。在接近风险中性的一端（长而不慌不忙的执行计划），增加一点紧迫性很便宜，因为你正处在成本曲线平缓的那一段；而在接近最大紧迫性的一端，同样绝对幅度的加速，在冲击成本上的付出，会远超它在时机风险上省下的收益。这就是"冲击对紧迫性是非线性的"背后的机制——不是紧迫性本身有某个固定的额外收费，而是成本曲线恰恰在你不断加压的地方变得越来越陡。
