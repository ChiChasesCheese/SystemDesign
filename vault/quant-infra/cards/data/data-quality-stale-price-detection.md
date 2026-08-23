---
id: data-quality-stale-price-detection
node: data.quality
type: qa
---
## Q
A thinly traded stock shows the exact same closing price for 6 consecutive trading days. This could mean the feed is broken (repeating the last good value) or it could mean the stock genuinely didn't trade at a different price. Name a check that distinguishes these two cases, and explain why price alone can't.

## A
**Price alone cannot distinguish "the feed is stuck" from "the market genuinely didn't move," because both produce an identical price series — the discriminator has to come from a second, independent signal.** The standard check cross-references **volume**: a price frozen at the identical value while volume is zero (or near-zero) across those days is consistent with genuine illiquidity — nobody traded, so there's no new print to move the price. A price frozen at the identical value while volume is *nonzero and roughly normal* is a strong signal of a broken feed — real trades occurred, so a genuinely unchanged last-sale price for six straight days at real volume is a much lower-probability event and should trigger investigation (a feed handler stuck replaying a cached value, a vendor snapshotting the wrong field, or an actual halt not correctly reflected).

A second, complementary check compares the flagged instrument against **correlated peers**: if a sector or the broader market moved 3% over those six days and this one name shows exactly zero movement despite normal volume, that divergence is itself evidence of a stale feed independent of the volume check. Neither check alone is airtight — an illiquid stock can occasionally show nonzero volume with no price change by genuine coincidence, and a whole sector can occasionally move together with one laggard — which is why production stale-price detectors combine the flat-price run length, the volume pattern, and peer-correlation divergence into one confidence score rather than triggering on any single condition alone, and route ambiguous cases to quarantine rather than silently trusting or silently dropping them.

## Q zh
一只流动性很差的股票，连续 6 个交易日显示完全相同的收盘价。这既可能是行情源坏了（一直重复上一个正常值），也可能是这只股票确实没有以别的价格成交过。请说出一种能区分这两种情况的检查方法，并解释为什么单看价格做不到这一点。

## A zh
**单看价格无法区分"行情源卡住了"和"市场确实没动"，因为这两种情况产出的价格序列是完全一样的——区分度必须来自第二个独立信号。** 标准做法是交叉核对**成交量**：如果价格冻结在同一个值、而这几天的成交量为零（或接近零），这与真正的流动性不足是吻合的——没人交易，自然没有新的成交打印能推动价格。如果价格冻结在同一个值、而成交量**非零且大致正常**，这就是行情源损坏的强烈信号——确实发生了真实成交，那么在真实成交量下连续六天收盘价一字不动，是一个概率低得多的事件，应当触发调查（可能是行情处理程序卡住重放了一个缓存值，供应商快照错了字段，或者一次真实的停牌没有被正确反映出来）。

第二个互补的检查是把被标记的标的与**相关同类标的**做比较：如果某个板块或大盘在这六天里涨了 3%，而这只股票在成交量正常的情况下涨跌幅恰好为零，这种背离本身就是独立于成交量检查之外、行情源过期的证据。这两个检查单独看都不是万无一失的——一只流动性差的股票偶尔可能巧合地出现非零成交量却价格不变，一整个板块也偶尔会真的齐涨齐跌、只剩一个滞后者——这正是为什么生产环境的过期价格检测器会把价格持平的持续长度、成交量模式、以及同类相关性背离综合成一个置信度分数，而不是单凭任何一个条件就触发，并把模棱两可的情况路由到隔离区，而不是悄悄信任或悄悄丢弃。
