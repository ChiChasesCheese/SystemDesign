---
id: carry-rates-fx-uip-forward-premium-puzzle
node: carry.rates-fx
type: qa
---
## Q
Uncovered interest rate parity (UIP) predicts that a currency with a higher
interest rate should, on average, depreciate by roughly that interest rate
differential. What does Fama's (1984) regression evidence actually find
instead, and why is this exactly what makes FX carry a profitable trade
rather than something arbitraged to zero?

## A
**UIP predicts the forward premium should be an unbiased predictor of the
future change in the spot rate** — regress the future spot change on the
interest differential (or equivalently the forward premium) and you should
get a slope coefficient of +1: high-rate currencies depreciate one-for-one
with their rate advantage, and hedged returns from borrowing low and lending
high should average to zero.

**Fama found the opposite sign.** Regressions of this type typically produce
a *negative* slope coefficient — high-interest-rate currencies tend to
depreciate less than their rate differential implies, or even appreciate on
average, rather than giving back the interest advantage. This is the
"forward premium puzzle," and it is the direct empirical reason FX carry
works: if UIP held exactly, borrowing the low-rate currency and lending the
high-rate one would earn zero expected excess return after accounting for
the expected depreciation. Because high-yielders don't reliably depreciate
enough to offset the rate gap, the interest differential survives as a real,
average positive excess return — not an arbitrage, since it's compensated
by exactly the tail/crash risk (a sudden, sharp depreciation of the
high-yield currency) that carry.concept describes as the price of the short-
vol payoff.

## Q zh
抛补利率平价(UIP)预测,利率较高的货币平均应该会贬值,贬值幅度大致等于这
个利率差。Fama(1984)的回归实证结果实际上发现了什么?这为什么恰恰是 FX
carry 能赚钱、而不是被套利到零的原因?

## A zh
**UIP 预测远期升贴水应该是未来即期汇率变动的无偏预测**——把未来即期汇率的
变动对利率差(或者等价地,对远期升贴水)做回归,理论上应该得到斜率系数
+1:高利率货币应该按其利率优势 1:1 贬值,借低息、贷高息的对冲后收益平均应
该为零。

**Fama 发现的是相反的符号。** 这类回归通常得到的是一个**负**的斜率系数——
高利率货币的贬值幅度往往小于利率差所暗示的程度,甚至平均而言还会升值,而
不是把利率优势吐回去。这就是"远期溢价之谜(forward premium puzzle)",
也是 FX carry 之所以能赚钱的直接实证原因:如果 UIP 完全成立,借低息货币、
贷高息货币在计入预期贬值之后应该赚到零预期超额收益。正因为高息货币不会可
靠地贬值到足以抵消利率差的程度,这个利率差就作为一份真实的、平均为正的超
额收益存活了下来——这不是套利,因为它恰恰是被 carry.concept 所说的
"short-vol payoff 的代价"——也就是高息货币突然、剧烈贬值的尾部/崩溃风
险——所补偿的。
