---
id: carry-rates-fx-curve-carry-rolldown
node: carry.rates-fx
type: qa
---
## Q
The Treasury curve is upward-sloping: the 10-year yields 4.5% and the
9-year (where today's 10-year bond will sit in a year, if the curve's shape
is unchanged) yields 4.2%. You buy the 10-year and hold it for one year.
Beyond the coupon, what additional source of return does "rolling down" the
curve give you, and what happens to this source of return if the curve is
flat or inverted instead?

## A
**Holding the bond for a year moves it from a 10-year maturity to a 9-year
maturity, and if the curve's shape stays the same, the yield appropriate to
that shorter maturity is lower — 4.2% instead of 4.5%.** A bond's price
moves inversely with its yield, so a bond whose yield falls (holding the
curve shape fixed) appreciates in price: the roughly 30bp yield decline,
applied through the bond's duration, produces price appreciation on top of
the coupon income the bond already pays. That price appreciation from
"sliding down" the curve as time passes — with no change in interest rates
themselves — is the roll (or rolldown) component of the bond's carry, and it
adds to the coupon/yield component to give total carry.

**On a flat curve, there is no rolldown** — the 9-year and 10-year yields
are the same, so moving from one maturity to the other produces no price
effect, and carry collapses to just the coupon/yield income. **On an
inverted curve, rolldown turns negative** — the 9-year yields more than the
10-year, so as the bond "rolls" to the shorter maturity its appropriate
yield rises, which means its price falls, subtracting from the coupon
income rather than adding to it. This is why a high current yield alone
(on an inverted curve) can be a misleading carry signal: the coupon looks
attractive, but the curve's shape is working against total carry, not with
it.

## Q zh
国债收益率曲线向上倾斜:10 年期收益率 4.5%,9 年期(即今天的 10 年期债券
一年后所处的位置,假设曲线形状不变)收益率 4.2%。你买入这只 10 年期债券并
持有一年。除了票息之外,"沿曲线下滑(roll down)"还给你带来了什么额外的
收益来源?如果曲线是平的或者倒挂的,这部分收益会发生什么变化?

## A zh
**持有这只债券一年,会让它从 10 年期变成 9 年期,如果曲线形状保持不变,与
这个更短期限相匹配的收益率会更低——从 4.5% 变成 4.2%。** 债券价格与收益率
反向变动,所以一只收益率下降(假定曲线形状不变)的债券,价格会上涨:这大约
30 个基点的收益率下降,通过债券的久期传导,会在债券本已支付的票息收入之外
再带来一部分价格上涨。这种随时间流逝、"沿曲线下滑"产生的价格上涨——利率
本身完全没有变动——就是债券 carry 中的 roll(或 rolldown)部分,它和票息/
收益率部分相加,构成总 carry。

**在一条平坦的曲线上,没有 rolldown**——9 年期和 10 年期收益率相同,从一个
期限滑向另一个期限不会产生任何价格效应,carry 就只剩下票息/收益率收入。
**在一条倒挂的曲线上,rolldown 会变成负的**——9 年期收益率高于 10 年期,所
以当债券"滚动"到更短期限时,与之匹配的收益率反而上升,这意味着价格会下
跌,从票息收入里扣掉一块而不是加上一块。这就是为什么单看当前收益率高(在
一条倒挂曲线上)可能是一个误导性的 carry 信号:票息看起来很吸引人,但曲线
的形状正在对总 carry 起反作用,而不是助力。
