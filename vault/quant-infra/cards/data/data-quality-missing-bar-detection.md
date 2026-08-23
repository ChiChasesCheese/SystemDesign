---
id: data-quality-missing-bar-detection
node: data.quality
type: qa
---
## Q
Your daily-bars table has no row for stock XYZ on 2024-03-14. This could mean the ingestion pipeline failed to load that day's data, or it could mean the stock genuinely didn't trade (a rare but real occurrence for illiquid micro-caps). What reference does a missing-bar detector need in order to tell these apart, and why is "no row = missing" not itself a sufficient check?

## A
**"No row" is ambiguous on its own — you need an independent source of truth for which dates a given instrument was even eligible to trade, and check the absence against that, not against a generic date range.** The reference is a **trading/holiday calendar** for the instrument's listing venue, combined with the instrument's own listing/delisting window from the security master: a missing row on a date the exchange was open and the instrument was actively listed is a genuine gap worth investigating; a missing row on an exchange holiday, on a date before the instrument's IPO, or after its delisting is not a gap at all — it's the correct absence of data, and flagging it would just generate noise the team learns to ignore.

Within the set of "should have traded" dates, the detector still can't fully resolve genuine-no-trade from pipeline failure by itself for a single instrument — a sufficiently illiquid micro-cap can legitimately go a session without a single print. The practical discriminators: (1) check whether *other* instruments loaded successfully for that same date — if XYZ is the only gap among thousands of names that all loaded fine, the fault is almost certainly XYZ-specific data (consistent with genuine no-trade), but if a whole batch of names is missing for that date, the fault is almost certainly a pipeline failure (a vendor outage, a job that didn't run); (2) cross-check against a second vendor for the same instrument and date — if vendor B has a print and vendor A doesn't, vendor A's pipeline is the gap, not the market. As with stale-price detection, no single signal is conclusive, so production detectors combine "should this date have data," "did peers load," and "does another source have it" before deciding a gap is real versus a false alarm.

## Q zh
你的日线表在 2024-03-14 这一天没有股票 XYZ 的记录。这既可能是入库流水线那天没能加载数据，也可能是这只股票确实没有成交（对流动性极差的微盘股来说是罕见但真实存在的情况）。缺失 bar 检测器需要参照什么才能区分这两种情况？为什么"没有行 = 缺失"本身不是一个充分的检查？

## A zh
**"没有行"本身是模糊的——你需要一个独立的可信来源，说明某个标的在哪些日期是本应可交易的，把缺失情况拿去和它比对，而不是和一个泛泛的日期区间比对。** 这个参照是该标的上市场所的**交易/假日日历**，再结合证券主数据里该标的自身的上市/退市窗口：如果交易所当天开市、该标的当天在正常挂牌交易，却缺了一行，这是一个真实值得调查的缺口；如果缺失发生在交易所假日、在该标的 IPO 之前，或在其退市之后，那根本不是缺口——这是数据理应缺失的正确状态，把它标记出来只会产生团队最终学会无视的噪音。

在"本应有成交"的日期集合内，检测器仍然无法仅凭单一标的自己，完全区分"真的没成交"和"流水线失败"——一只流动性足够差的微盘股确实可能在某个交易日一笔成交都没有，这是合法的。实践中的判别方法是：（1）检查*其他*标的当天是否成功加载——如果在成千上万只当天都正常加载的标的中，只有 XYZ 出现缺口，故障几乎肯定是 XYZ 特有的数据问题（与真实无成交的情况吻合）；但如果整批标的当天都缺失，故障几乎肯定是流水线本身的问题（供应商中断、任务没跑）；（2）针对同一标的、同一日期，与第二家供应商做交叉核对——如果供应商 B 有这笔成交而供应商 A 没有，那么出问题的是供应商 A 的流水线，而不是市场本身。和过期价格检测一样，没有任何单一信号是决定性的，所以生产环境的检测器会综合"这一天本该有数据吗"、"同类标的是否加载成功"、"是否有其他来源有这条数据"三者，再判断一个缺口是真实的还是虚警。
