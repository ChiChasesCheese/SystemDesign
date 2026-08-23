---
id: data-secmaster-adjusted-price-breaks-volume-limits
node: data.security-master
type: qa
---
## Q
A pipeline stores split-adjusted prices but leaves the `volume` and `limit_up`/`limit_down` columns from the raw feed untouched. Two features are computed downstream: dollar volume (`price * volume`) and a "would this order have been limit-blocked" check comparing the strategy's intended price to `limit_up`/`limit_down`. What breaks in each, and why?

## A
**Both break because adjusted price and raw share/limit fields stop being the same unit system once a split happens, and the two errors point in opposite directions.**

- **Dollar volume**: a split-adjusted price is scaled by the inverse of the split ratio (a 2-for-1 split multiplies historical prices by 0.5), but volume must be scaled by the *opposite* factor to stay consistent — historical share counts should be multiplied by 2, since a holder who had 100 shares pre-split has 200 post-split-equivalent shares. If the pipeline adjusts price but leaves volume as raw historical share counts, `price * volume` (dollar volume) for pre-split dates is silently cut in half relative to its true value — a dollar-volume-based liquidity filter or participation cap will misjudge how liquid the stock actually was.
- **Limit bands**: `limit_up`/`limit_down` (or, on venues with them, price collars/circuit-breaker bands) are set by the exchange in real, as-traded price terms on the day in question — they were never adjusted for a split that hadn't happened yet. Comparing an adjusted historical price series to these raw limit values compares two different price scales; for any date before a subsequent split, the adjusted price is a fraction of the actual traded price, so a check like "was the fill price within the limit band" will almost always spuriously pass or fail depending on the split direction, making halts and limit-hit logic silently wrong for the entire pre-split history.

The fix is to never mix adjusted and unadjusted fields in the same comparison: either keep both a raw and an adjusted series for every field that has units in price/shares (so features pick the correct one per calculation), or restrict adjusted prices strictly to return/performance calculations and always evaluate market-mechanics logic (limits, volume caps, actual fills) against the raw, as-traded numbers.

## Q zh
一个流水线存储了拆分复权后的价格，但没有对原始行情里的 `volume`（成交量）和 `limit_up`/`limit_down`（涨跌停价）字段做任何处理。下游计算了两个特征：美元成交量（`price * volume`），以及一个"这笔委托当时是否会被涨跌停挡住"的检查，把策略意图价格与 `limit_up`/`limit_down` 比较。这两处分别会出什么问题？为什么？

## A zh
**两处都会出问题，因为一旦发生拆分，复权价格和原始股数/涨跌停字段就不再处于同一套单位体系了，而且这两个错误的方向恰好相反。**

- **美元成交量**：拆分复权价格按拆分比例的倒数缩放（2 股拆 1 股会把历史价格乘以 0.5），但成交量必须按**相反的**因子缩放才能保持一致——历史股数应当乘以 2，因为拆分前持有 100 股的人在拆分后等价于持有 200 股。如果流水线对价格做了复权、却把成交量留成原始历史股数，那么拆分前那些日期的 `price * volume`（美元成交量）相对真实值会被悄悄砍掉一半——基于美元成交量的流动性过滤器或参与率上限会误判该股票当时的真实流动性。
- **涨跌停带**：`limit_up`/`limit_down`（在有此机制的市场，也包括价格限幅带/熔断带）是交易所按当天真实的、实际成交的价格口径设定的——它们从未为一次尚未发生的拆分做过复权。把一条复权后的历史价格序列拿去和这些原始限价值比较，等于在比较两套不同的价格量纲；对任何一次后续拆分之前的日期，复权价格只是实际成交价格的一个零头，所以类似"成交价是否在涨跌停带内"这样的检查，几乎总会因为拆分方向而出现虚假的通过或虚假的触发，让拆分前的整段历史里，停牌和涨跌停触发逻辑都悄悄地错了。

修正方法是永远不要在同一个比较里混用复权和未复权字段：要么对每一个带有价格/股数量纲的字段都同时保留原始和复权两个序列（让每个计算各自挑选正确的那一个），要么把复权价格严格限定在收益率/绩效计算里使用，而所有涉及市场机制的逻辑（涨跌停、成交量上限、实际成交）一律用原始的、实际成交口径的数字来评估。
