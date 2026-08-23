---
id: execution-spread-realized-spread-decomposition
node: execution.spread
type: qa
---
## Q
A market maker's effective spread on a buy order is 4 bps, but five minutes after the fill, the price has moved up 3 bps in the buyer's favor and stayed there. How much of that 4 bps did the market maker actually keep as profit, and what does the rest represent?

## A
**The market maker kept only about 1 bp; the other 3 bps was never profit at all — it was the market repricing to reflect information the buyer had and the maker didn't.** This is the **realized spread decomposition**: effective spread splits into **realized spread** (what the liquidity provider actually earns) and **price impact / markout** (the price move after the trade, in the direction that hurts the liquidity provider).

`realized spread ≈ effective spread − price impact`

Here, price impact is measured as the signed price move from execution to some horizon later (commonly a few minutes) — the buyer paid at the ask, and if the midpoint has since risen 3 bps and stayed there, that portion of what the maker "earned" on paper at the moment of the trade has already evaporated: the maker is now short a security that's worth 3 bps more, an unrealized loss on the inventory they're still holding or a loss crystallized once they cover. Only the remaining 1 bp survives as durable compensation.

Why this decomposition matters: **effective spread alone conflates a genuinely profitable trade with one that was picked off by informed flow.** A market maker (or anyone analyzing maker economics) needs the split to tell the two apart — a name where realized spread is consistently close to effective spread is one where the maker's flow is relatively uninformed and the maker prices tightly and profitably; a name where realized spread shrinks toward zero or goes negative is one where adverse selection is eating the entire quoted compensation, and the maker should widen quotes or stop making markets in that name altogether. The permanent component (price impact) is exactly the piece that also shows up on the impact leaf as the cost a *taker* pays that persists rather than decays.

## Q zh
一位做市商在一笔买单上的有效价差是 4 个基点，但成交 5 分钟后，价格朝买方有利的方向上涨了 3 个基点，并且没有回落。这 4 个基点里，做市商实际留下了多少作为利润？剩下的部分代表什么？

## A zh
**做市商实际上只留下了大约 1 个基点；另外 3 个基点根本不是利润——那是市场在重新定价，以反映买方掌握而做市商不掌握的信息。** 这就是**已实现价差分解（realized spread decomposition）**：有效价差可以拆分成**已实现价差（realized spread）**（流动性提供者实际赚到的部分）和**价格冲击/成交后走势（price impact / markout）**（成交之后价格朝着不利于流动性提供者方向移动的部分）。

`已实现价差 ≈ 有效价差 − 价格冲击`

这里，价格冲击是从成交那一刻到之后某个时间点（通常几分钟后）的带符号价格变动——买方是按卖一价成交的，如果中点价此后上涨了 3 个基点并保持在那里，那么做市商在成交那一刻账面上"赚到"的那部分收益中，有这么多其实已经蒸发了：做市商现在空头一笔已经值钱 3 个基点的证券，这要么是他们仍持有这笔库存产生的未实现损失，要么是等他们平仓时兑现的实际损失。只有剩下的 1 个基点，才作为持久的补偿真正留存下来。

这个分解为什么重要：**单看有效价差，会把一笔真正赚钱的成交，和一笔被知情资金流打中的成交混为一谈。** 做市商（或任何分析做市经济性的人）需要这个拆分来区分二者——一只已实现价差持续接近有效价差的股票，说明做市商面对的资金流相对不知情，报价既紧又能盈利；一只已实现价差趋近于零甚至变负的股票，说明逆向选择正在吃掉全部报价补偿，做市商应该把报价拉宽，或者干脆不再为这只股票做市。这个永久性分量（价格冲击）恰好也是在 impact 那一支里会出现的那个部分——即吃单方（taker）付出的、不会衰减而是会持续存在的成本。
