---
id: carry-concept-definition-unchanged-price
node: carry.concept
type: qa
---
## Q
Give the precise definition of carry — not "the yield" or "the income," but
what makes carry different from a return forecast. What information do you
need to compute it, and what do you explicitly not need?

## A
**Carry is the return a position would earn if the price stayed exactly
unchanged over the holding period.** It answers "what do I earn just for
holding this, assuming nothing happens to the price," which is a completely
different question from "what do I think will happen to the price."

Crucially, carry is computable today, directly from the market's current
curve — the forward rate, the futures curve, or the yield curve — without
forming any view about the future. For a currency forward, carry is pinned
down by today's spot and forward rates (which in turn reflect the interest
rate differential); for a bond, by today's yield curve; for a commodity
future, by today's futures curve relative to spot. None of these require a
forecast of where the exchange rate, yield curve, or commodity price is
headed — that's the point: carry is the part of expected return you can read
off the current market structure, leaving "price appreciation/depreciation"
as the separate, forecast-dependent piece of total return.

## Q zh
请给出 carry 的精确定义——不是"收益率"或"票息",而是 carry 和一个价格预测
到底有什么不同。要算出 carry 需要什么信息,又明确不需要什么信息?

## A zh
**Carry 是假设持有期内价格完全不变,这个头寸能赚到的收益。** 它回答的问题
是"假设价格什么都不发生,我光是持有这个头寸能赚多少",这和"我认为价格会
怎么走"是完全不同的问题。

关键在于,carry 是今天就能算出来的,直接从市场当前的曲线读出来——远期汇
率、期货曲线、或者收益率曲线——而不需要对未来形成任何判断。对一笔货币远期
交易来说,carry 由今天的即期汇率和远期汇率钉定(而这又反映了利率差);对
一只债券来说,由今天的收益率曲线钉定;对一份商品期货来说,由今天的期货曲
线相对于现货的位置钉定。这些都不需要预测汇率、收益率曲线或商品价格未来会
往哪走——这正是重点所在:carry 是预期收益中可以直接从当前市场结构读出来的
那一部分,剩下"价格上涨/下跌"则是总收益中另一块、依赖预测的部分。
