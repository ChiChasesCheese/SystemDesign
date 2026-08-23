---
id: execution-spread-compensation-for-risk
node: execution.spread
type: qa
---
## Q
A liquid mega-cap stock trades with a half-spread of roughly 1-5 bps; an illiquid small-cap can run 20-100+ bps. A market maker quoting either name is providing the same service — continuous two-sided liquidity — so why does one cost so much more than the other to trade against?

## A
**The spread is not a fee for a service rendered; it's compensation the market maker demands for two risks that scale with how illiquid and how informationally opaque a name is.**

- **Inventory risk.** A market maker who just bought from a seller now holds unwanted inventory and is exposed to the price moving against that position before they can offload it. The less liquid the name, the longer it takes to lay off that inventory (fewer natural counterparties arrive per unit time), so the maker is exposed for longer and demands a wider spread to be compensated for holding risk they didn't choose to take. A mega-cap's deep, constant two-sided flow lets a maker turn inventory over almost immediately; a thin small-cap can leave them holding a position for minutes or hours.
- **Adverse selection.** Some of the flow that trades against the maker's quote is informed — someone who knows something the maker doesn't and is trading precisely because the quoted price is about to be wrong. The maker cannot tell an informed order from a liquidity-driven one before filling it, so they price in the *average* cost of being picked off. A name with more concentrated informed trading relative to total volume (common in smaller, less-covered stocks where information asymmetry between insiders/informed traders and the market is larger) means a bigger fraction of every fill is adverse selection, and the spread widens to cover it.

The consequence: spread is not primarily set by exchange fees, share price, or convention — it's set by how expensive it is, on average, to be a market maker in that specific name, which is why spread tracks liquidity and information opacity so closely across the cross-section of stocks.

## Q zh
一只流动性很好的大盘股，半价差大约是 1-5 个基点；一只流动性差的小盘股，半价差可能高达 20-100+ 个基点。给这两只股票报价的做市商提供的是同一种服务——持续的双边流动性——为什么与其中一只做交易的成本要高出这么多？

## A zh
**价差不是为某项服务支付的手续费；它是做市商为两类风险索要的补偿，而这两类风险的大小取决于这只股票的流动性有多差、信息有多不透明。**

- **库存风险（inventory risk）。** 一位刚从卖方那里买入的做市商，此刻手里持有一笔不想要的库存，在能够脱手之前一直暴露在价格朝不利方向变动的风险中。这只股票流动性越差，脱手这笔库存所需的时间就越长（单位时间内出现的天然对手盘越少），做市商暴露的时间也就越长，因此要索要更宽的价差来补偿他们本不想承担的这份持仓风险。大盘股深厚、持续的双边资金流，让做市商几乎能立刻周转掉库存；而流动性薄的小盘股，可能让他们持仓好几分钟甚至好几小时。
- **逆向选择（adverse selection）。** 与做市商报价成交的部分资金流是知情的——某个知道做市商不知道的信息、正是因为报价即将变得错误才来交易的人。做市商在成交之前无法分辨一笔委托是知情单还是纯粹的流动性需求单，所以他们把"被打中的*平均*成本"定价进报价里。一只知情交易相对于总成交量更集中的股票（在覆盖度低、内部人/知情交易者与市场之间信息不对称更大的小盘股中很常见），意味着每一笔成交里逆向选择所占的比例更大，价差因此被拉得更宽。

后果是：价差主要不是由交易所手续费、股价高低或行业惯例决定的——它是由"在这只具体股票上当做市商，平均成本有多高"决定的，这正是为什么价差在股票横截面上会如此紧密地跟随流动性和信息不透明度而变化。
