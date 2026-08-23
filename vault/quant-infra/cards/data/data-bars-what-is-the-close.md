---
id: data-bars-what-is-the-close
node: data.market-data.bars
type: qa
---
## Q
Vendor A reports AAPL's "close" for a given day as $190.12. Vendor B reports $190.34 for the same day. Both claim to be correct. Name at least two genuinely different prices this "close" could refer to, and why they legitimately disagree.

## A
**"Close" is not one number — it depends on which trade or process you treat as authoritative, and reasonable choices disagree by design.** At minimum:
- **The official closing-auction price** on the stock's primary listing exchange (e.g. Nasdaq or NYSE's closing auction) — a single-price call auction that crosses all closing-eligible orders at one clearing price, published with an explicit "official close" tag. This is the number most index providers and the exchange itself treat as canonical.
- **The last regular-session trade price on the consolidated tape**, which can differ from the closing auction print because a large fraction of a stock's volume — sometimes on the order of 5-15%+ for liquid names — trades off-exchange (dark pools, wholesalers internalizing retail flow) and away from the primary listing exchange's auction mechanism, so "the last trade the SIP saw before 4:00pm" is not guaranteed to be the auction print itself, and their microsecond ordering near the close can differ.
- **A composite/consolidated last-sale price** some vendors compute as the last trade across all reporting venues up to a cutoff, which can include or exclude late-reported or corrected prints depending on when the vendor's snapshot was taken.

The practical consequence: a feature or a fill assumption built on "the close" must pin down *which* close, because they diverge most exactly when it matters most — thin names, high-volatility closes, and days with heavy off-exchange or after-hours activity — and silently mixing sources (using vendor A's close as an entry price and vendor B's close for a benchmark return) manufactures a phantom return equal to the gap between the two.

## Q zh
供应商 A 报告 AAPL 某一天的"收盘价"是 190.12 美元。供应商 B 报告同一天是 190.34 美元。两者都声称自己是对的。请说出这个"收盘价"至少两种真正不同的含义，以及为什么它们会合理地不一致。

## A zh
**"收盘价"并不是唯一一个数字——它取决于你把哪一笔成交或哪个流程当作权威口径，而合理的选择本来就会互不相同。** 至少包括：
- **该股票主上市交易所的官方集合竞价收盘价**（例如纳斯达克或纽交所的收盘集合竞价）——一个单一价格的集合竞价，把所有符合收盘条件的委托以一个出清价撮合，并附带明确的"官方收盘"标记。这是大多数指数提供商以及交易所自身视为权威的数字。
- **合并行情上常规交易时段的最后一笔成交价**，它可能与收盘集合竞价的成交价不同，因为一只股票相当一部分成交量——对于流动性好的标的，有时可达 5-15%+甚至更多——是在场外成交的（暗池、内部化零售订单流的批发商），并不经过主上市交易所的集合竞价机制，所以"SIP 在下午 4 点前看到的最后一笔成交"并不保证就是集合竞价的成交本身，两者在收盘附近微秒级的先后顺序也可能不同。
- 一些供应商计算的**综合/合并最新成交价**，取截止到某个时点、跨所有上报场所的最后一笔成交，根据供应商截取快照的时点不同，可能包含或不包含迟报或被更正的成交。

实际后果是：任何建立在"收盘价"之上的特征或成交假设，都必须明确到底是**哪一个**收盘价，因为它们恰恰在最要紧的时候分歧最大——流动性差的标的、波动剧烈的收盘、以及场外或盘后活动频繁的交易日；而悄悄混用不同来源（用供应商 A 的收盘价作为入场价、用供应商 B 的收盘价计算基准收益）会凭空制造出一个恰好等于两者差值的虚假收益。
