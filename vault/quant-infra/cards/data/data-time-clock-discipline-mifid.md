---
id: data-time-clock-discipline-mifid
node: data.market-data.time
type: qa
---
## Q
Two servers in your trading stack — the feed handler and the strategy engine — each timestamp events using their own local system clock, synced by ordinary NTP. Why is this a live-correctness risk even if both clocks are "accurate to a second or so," and what regulatory number sets the bar in practice for high-frequency activity?

## A
**Any latency measurement or event-ordering decision that spans two machines is only as trustworthy as the *drift between* their clocks, not the absolute accuracy of either one.** If the feed handler's clock reads 3ms ahead of the strategy engine's clock, every tick-to-decision latency you compute across the two machines is wrong by 3ms in a fixed direction — and worse, if two events from different machines are close in real time, comparing their timestamps to determine which happened first can give the wrong answer entirely. Ordinary **NTP** typically synchronizes clocks to within single-digit milliseconds over a LAN, which sounds tight but is often larger than the actual round-trip latency budget a fast strategy cares about — meaning the clock error can exceed the signal you're trying to measure.

The regulatory benchmark: **MiFID II RTS 25** requires firms engaged in high-frequency algorithmic trading to synchronize their business clocks to UTC with a maximum divergence of **100 microseconds**, traceable to a recognized time source (typically enforced via **PTP** — Precision Time Protocol, which achieves sub-microsecond to low-microsecond synchronization on well-engineered hardware, versus NTP's millisecond-class accuracy); other, less latency-sensitive trading activity gets a looser 1-millisecond requirement under the same rule. The practical takeaway for research infrastructure: NTP is adequate for wall-clock logging and coarse sequencing, but any system computing sub-millisecond latencies or ordering events across machines for a latency-sensitive strategy needs PTP-grade discipline, not NTP.

## Q zh
你的交易系统里有两台服务器——行情处理程序和策略引擎——各自用普通 NTP 同步的本地系统时钟给事件打时间戳。即便两个时钟都"精确到大约一秒左右"，为什么这依然是一个实盘正确性风险？实践中给高频活动设下门槛的监管数字是多少？

## A zh
**任何跨越两台机器的延迟测量或事件先后判断，可信度只取决于两台时钟之间的**漂移**，而不是任何一台时钟本身的绝对精度。** 如果行情处理程序的时钟比策略引擎的时钟快 3 毫秒，那么你在这两台机器之间计算出的每一个从行情到决策的延迟，都会朝固定方向错 3 毫秒——更糟的是，如果来自不同机器的两个事件在真实时间上很接近，仅凭比较它们的时间戳来判断谁先发生，可能会得到完全错误的答案。普通 **NTP** 在局域网内通常能把时钟同步到个位数毫秒以内，听起来已经很紧了，但往往仍大于一个快速策略真正关心的往返延迟预算——意味着时钟误差可能超过你想测量的信号本身。

监管基准是：**MiFID II RTS 25** 要求从事高频算法交易的机构，将其业务时钟与 UTC 同步，最大偏差不超过 **100 微秒**，且可追溯到一个公认的时间源（通常通过 **PTP**——精确时间协议实现，在工程良好的硬件上能达到亚微秒到个位数微秒级同步，相比之下 NTP 是毫秒级精度）；同一规则下，对延迟敏感度较低的其他交易活动，要求放宽到 1 毫秒。对研究基础设施而言实际的结论是：NTP 对墙钟日志和粗粒度事件排序是够用的，但任何要为一个延迟敏感策略计算亚毫秒级延迟或跨机器排序事件的系统，都需要 PTP 级别的纪律，而不是 NTP。
