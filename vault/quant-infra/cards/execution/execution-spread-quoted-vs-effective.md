---
id: execution-spread-quoted-vs-effective
node: execution.spread
type: qa
---
## Q
A stock quotes bid $50.00 / ask $50.10, a 10-cent quoted spread. Your market buy order fills at $50.04. You want to measure your actual transaction cost — should you use the 10-cent quoted spread, and if not, what should you compute instead?

## A
**Use the effective spread, not the quoted spread — the quoted spread tells you the worst-case cost available at that moment, not the cost you actually paid.** The **quoted spread** is simply ask − bid ($0.10 here); it's a property of the displayed book, observable before anyone trades, and it's what you'd pay only if you crossed the full distance from the midpoint to the far touch. The **effective spread** is defined from what actually happened: `2 × |execution price − midpoint at order time|`. Here the midpoint was ($50.00+$50.10)/2 = $50.05, you filled at $50.04, so effective spread = 2 × |50.04 − 50.05| = $0.02 — a fifth of the quoted spread.

The gap between the two is **price improvement**: your order executed *inside* the quoted spread rather than at the far touch, which happens routinely when a marketable order interacts with hidden liquidity, receives a midpoint-pegged fill in a dark venue, or is matched against another order at a better price than the displayed quote implied. This is why quoted spread is a poor proxy for realized transaction cost in any market with meaningful non-displayed liquidity: it measures what was *offered*, not what you *paid*. Any serious cost analysis — and every card downstream on realized spread and TCA — starts from effective spread, computed trade by trade against the prevailing midpoint at the moment of execution, not from the static quoted number.

## Q zh
某只股票报价买一 50.00 美元 / 卖一 50.10 美元，报价价差（quoted spread）是 10 美分。你的市价买单以 50.04 美元成交。你想衡量自己实际付出的交易成本——应该用这 10 美分的报价价差吗？如果不是，应该计算什么？

## A zh
**应该用有效价差（effective spread），而不是报价价差——报价价差告诉你的是那一刻可获得的最坏情况成本，而不是你实际付出的成本。** **报价价差**就是卖一减买一（这里是 0.10 美元）；它是显示盘口的一个属性，在任何人成交之前就能观察到，只有当你从中点一路穿越到最远端的对手价时，才会付出这么多。**有效价差**则是按实际发生的情况定义的：`2 × |成交价 − 下单时的中点价|`。这里中点是 (50.00+50.10)/2 = 50.05 美元，你以 50.04 美元成交，所以有效价差 = 2 × |50.04 − 50.05| = 0.02 美元——只有报价价差的五分之一。

两者之间的差距就是**价格改善（price improvement）**：你的委托是在报价价差**内部**成交的，而不是在最远端的对手价成交——这在委托与隐藏流动性互动、在暗池里拿到中点撮合的成交、或者被匹配到一笔价格比显示报价更优的对手单时，是常态。这正是为什么在任何存在可观非显示流动性的市场里，报价价差都不是实现交易成本的好代理指标：它衡量的是当时"被提供了什么"，而不是你"实际付出了什么"。任何认真的成本分析——包括后续关于已实现价差和 TCA 的每一张卡片——都是从有效价差出发，逐笔按成交那一刻的当期中点价计算，而不是从静态的报价数字出发。
