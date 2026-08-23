---
id: execution-sessions-luld-bands
node: execution.microstructure.sessions
type: qa
---
## Q
A stock's price threatens to move 6% below its recent reference price in a matter of seconds. Under the US Limit Up-Limit Down (LULD) mechanism, what actually stops that trade from happening, and what turns a band breach into a full trading pause?

## A
**LULD does not ban a large move outright — it bans the market from *quoting or trading outside a moving price band* for more than a few seconds before forcing a pause.** The band is a percentage collar (e.g., 5% for the most liquid Tier 1 names such as S&P 500 and Russell 1000 components, 10% for Tier 2, with wider bands intraday near the open/close and for lower-priced stocks) computed around a reference price that itself updates continuously — typically a trailing average of recent trade prices. So the band isn't fixed for the day; it re-centers as the price genuinely moves, but it prevents a move so fast it outruns the reference itself.

The escalation works in two steps: if the **National Best Bid or Offer is outside the band**, the exchanges must simply not display quotes outside it (and cannot trade there) — this alone can quietly resolve minor breaches as the market self-corrects within the band. If the NBBO remains outside the band, or a trade threatens to occur outside it, for **15 seconds continuously**, the security enters a **trading pause**, which then goes through the same reopening-auction mechanics as any other halt (see the reopening-auction card): orders accumulate, an indicative price is published, and a fresh auction sets the price at which trading resumes. So the mechanism's real function is to convert "the price wants to gap fast" into "the price has to clear the same auction process used for any other halt," rather than letting a fast, possibly erroneous or thin-liquidity move print and stand.

## Q zh
某只股票的价格在几秒钟内威胁要跌破最近参考价 6%。在美国的 Limit Up-Limit Down（LULD）机制下，究竟是什么阻止了这笔交易发生？触及价格带（band）又是如何升级为完全的交易暂停的？

## A zh
**LULD 并不是直接禁止大幅波动本身——它禁止的是市场在超过几秒钟的时间里，*在一个随行情移动的价格带之外报价或成交*，超过这个时限就强制暂停交易。** 这个价格带是一个百分比区间（比如流动性最好的一档股票——标普 500、罗素 1000 成分股——为 5%，二档股票为 10%，在盘中开盘/收盘附近以及低价股上带宽更宽），围绕一个本身也在持续更新的参考价计算出来——通常是最近成交价的滚动均值。所以这个价格带不是全天固定不变的；它会随着价格真实地移动而重新定心，但它能阻止的是一个快到把参考价本身都甩在后面的极端波动。

升级过程分两步：如果**全国最优买卖报价（NBBO）超出了价格带**，交易所必须不显示带外的报价（也不能在那里成交）——单这一步就可能悄悄化解掉那些市场在带内自我修正的轻微触发。如果 NBBO **连续 15 秒**仍然超出价格带，或者有成交威胁要在带外发生，这只证券就进入**交易暂停（trading pause）**，接下来走的就是和其他任何熔断一样的重新开盘拍卖流程（见重新开盘拍卖那张卡片）：委托累积、发布指示价格，由一场全新的拍卖来确定恢复交易时的成交价格。所以这套机制真正的作用，是把"价格想要快速跳空"转化为"价格必须走一遍和其他任何熔断一样的拍卖出清流程"，而不是任由一个快速的、可能是错误报价或薄流动性造成的波动直接成交并作数。
