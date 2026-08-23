---
id: momentum-trend-xsmom-crash-resilience
node: momentum.trend
type: qa
---
## Q
Cross-sectional equity momentum crashed violently in the sharp V-shaped
rebound off the March 2009 low. Time-series momentum (TSMOM) also lost money
around sudden trend reversals, but did not exhibit the same severe,
concentrated crash. What is different about the loss mechanism in each case?

## A
**Cross-sectional momentum's crash requires a relative-spread structure that
TSMOM doesn't have.** The 2009 crash happened because the short leg (past
losers, disproportionately high-beta) rebounded harder than the long leg
(past winners, lower-beta) as the whole market snapped back — the loss comes
from the *spread between two legs*, amplified by the leverage difference
built into which names ended up long versus short. That amplification
mechanism is specific to a long-short, relative-ranking construction.

TSMOM has no such spread to blow up: each market's position is judged only
against its own trend, independent of every other market. A sharp V-shaped
reversal does cause TSMOM to whipsaw — it gets caught holding a short
position into the rebound and takes a loss on that market — but the loss is
bounded to that one market's position size (scaled by its own volatility),
not amplified through a long-short spread built from a systematically
higher-beta short book. TSMOM's bad moments come from many markets
whipsawing around sudden, simultaneous trend reversals — a diffuse cost — not
from a single violent short-squeeze concentrated in one structurally
leveraged leg, which is why its loss profile is smaller and less
catastrophically concentrated than a momentum crash.

## Q zh
横截面股票动量在 2009 年 3 月低点后的 V 型剧烈反弹中崩溃得很惨。时序动量
(TSMOM)在突然的趋势反转附近也会亏钱,但没有表现出同样严重、集中的崩溃。
两种情况下的亏损机制有什么不同?

## A zh
**横截面动量的崩溃需要一种 TSMOM 并不具备的相对价差结构。** 2009 年的崩溃
之所以发生,是因为当整个市场猛烈反弹时,空头腿(过去的输家,不成比例地集
中在高 beta 股票)反弹幅度超过了多头腿(过去的赢家,beta 较低)——亏损来自
**两条腿之间的价差**,并被"哪些股票最终被做多、哪些被做空"这个结构中内
嵌的杠杆差异放大。这种放大机制是长短仓、相对排序构造所特有的。

TSMOM 没有这样一个会被引爆的价差:每个市场的仓位只根据其自身的趋势来判
断,和其他任何市场无关。一次剧烈的 V 型反转确实会让 TSMOM 遭遇 whipsaw——
它会在反弹到来时仍持有空头仓位,在那个市场上产生亏损——但这个亏损被限定在
那一个市场的仓位规模内(按其自身波动率缩放),而不会通过一个由系统性更高
beta 的空头组合构成的长短价差被放大。TSMOM 糟糕时刻的来源,是许多市场围绕
突然、同时发生的趋势反转各自 whipsaw——一种分散的成本——而不是集中在某一条
结构性加杠杆的腿上的单次剧烈逼空,这就是为什么它的亏损轮廓比动量崩溃更
小、集中度也更低。
