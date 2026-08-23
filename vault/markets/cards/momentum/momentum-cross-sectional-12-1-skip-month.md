---
id: momentum-cross-sectional-12-1-skip-month
node: momentum.cross-sectional
type: qa
---
## Q
The textbook cross-sectional momentum signal ranks stocks on their trailing
12-month return but explicitly skips the most recent month — sorting on
months t-12 through t-2, not t-12 through t-1. Why does dropping that one
month matter, and what would happen to the strategy if you left it in?

## A
**The most recent month behaves oppositely to the other eleven.** Over
horizons of a few weeks to a month, stock returns show *short-term reversal*
— last month's biggest gainers tend to give some of it back, and last
month's biggest losers tend to bounce, an effect driven by bid-ask bounce and
temporary liquidity/order-flow imbalances rather than genuine information.
That is the opposite sign from the 2-to-12-month drift momentum is trying to
capture.

Including month t-1 in the ranking would mix a reversal signal into a
momentum signal: it would tilt the "winner" bucket away from stocks that
happen to have just had a bad month (even if their 11-month trend is strong)
and contaminate the loser bucket the same way, diluting the momentum spread
and adding noise correlated with short-term liquidity effects rather than
underreaction. Skipping t-1 isolates the intermediate-horizon drift from the
short-horizon reversal that lives right next to it.

## Q zh
教科书式的横截面动量信号用过去 12 个月的收益排序,但明确跳过最近一个月——用
t-12 到 t-2 排序,而不是 t-12 到 t-1。跳过这一个月为什么重要?如果把它留在
里面,策略会发生什么?

## A zh
**最近一个月的表现方向和另外 11 个月是相反的。** 在几周到一个月这个尺度上,
股票收益表现出**短期反转(short-term reversal)**——上个月涨最多的股票往往会
回吐一部分涨幅,上个月跌最多的股票往往会反弹,这个效应主要由买卖价差跳动
(bid-ask bounce)和暂时性的流动性/订单流失衡驱动,而不是真实信息。这和动
量想捕捉的 2-到-12 个月漂移方向正好相反。

如果把 t-1 月也纳入排序,就会把一个反转信号混进动量信号里:它会把"赢家"
一档里那些恰好上个月表现不佳(哪怕前 11 个月趋势很强)的股票挤出去,同样也
会污染"输家"一档,稀释动量价差,并引入和短期流动性效应相关的噪音,而不是
反应不足本身。跳过 t-1 就是把中期漂移和紧挨着它的短期反转分开。
