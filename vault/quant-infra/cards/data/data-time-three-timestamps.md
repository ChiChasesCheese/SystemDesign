---
id: data-time-three-timestamps
node: data.market-data.time
type: qa
---
## Q
A single trade record in your archive can carry at least three different timestamps: the exchange timestamp, the capture timestamp, and the ingest timestamp. Define each, and explain which one a backtest should use as the "decision could have happened here" boundary — and why using either of the other two is wrong in a different direction.

## A
**Three distinct clocks, three distinct meanings:**
- **Exchange timestamp**: when the venue's matching engine actually executed or generated the event — the ground truth of when the trade or quote happened in the real world.
- **Capture timestamp**: when your feed handler's network interface or process actually received the message — later than the exchange timestamp by wire and processing latency (fractions of a millisecond on a colocated direct feed, up to tens of milliseconds or more for a retail-grade or SIP-routed connection).
- **Ingest timestamp**: when the event lands in your database or research warehouse after whatever queuing, batching, or ETL delay your pipeline adds — later still, sometimes by seconds to hours if data is only "ingested" at end of day.

**The backtest's decision boundary should be the capture timestamp, not the exchange timestamp.** Using the exchange timestamp as the moment your strategy "knew" about an event assumes zero transmission latency — a form of lookahead bias, since no real system receives information at the instant it occurs. Using the ingest timestamp, conversely, is overly conservative for a live-latency-sensitive strategy if ingest lag is an artifact of your research pipeline's batching rather than something a live system would actually incur — it would make the backtest reject opportunities a well-engineered live system could actually capture. The capture timestamp is the only one of the three that represents "when *this specific pipeline*, running with realistic network and processing latency, actually had the information" — which is exactly the boundary a decision-timing simulation needs.

## Q zh
归档里的一条成交记录可能携带至少三种不同的时间戳：交易所时间戳、捕获时间戳、入库时间戳。请分别定义它们，并说明回测应当用哪一个作为"决策本可以在此刻发生"的边界——用另外两个分别会在什么方向上出错？

## A zh
**三个不同的时钟，三种不同的含义：**
- **交易所时间戳（exchange timestamp）**：场所撮合引擎真正执行或生成该事件的时刻——真实世界中这笔成交或报价发生的地面真相。
- **捕获时间戳（capture timestamp）**：你的行情处理程序的网卡或进程真正收到该报文的时刻——由于线路和处理延迟，会晚于交易所时间戳（对同机房直连行情而言是零点几毫秒量级，对零售级或经 SIP 路由的连接而言可能达几十毫秒甚至更多）。
- **入库时间戳（ingest timestamp）**：该事件经过流水线的排队、批处理或 ETL 延迟之后，真正落入你的数据库或研究数据仓库的时刻——更晚，如果数据只在每日收盘后才"入库"，有时会晚上数秒到数小时。

**回测的决策边界应当使用捕获时间戳，而不是交易所时间戳。** 把交易所时间戳当作策略"得知"某事件的时刻，等于假设传输延迟为零——这是一种前视偏差（lookahead bias），因为没有任何真实系统能在事件发生的瞬间就收到信息。反过来，如果入库延迟只是研究流水线批处理造成的产物，而不是实盘系统真正会承受的延迟，那么用入库时间戳又对一个对实盘延迟敏感的策略过于保守——它会让回测拒绝一些一个工程良好的实盘系统本可以真正捕捉到的机会。三者之中，只有捕获时间戳代表的是"*这套具体的流水线*，在真实的网络和处理延迟下，实际拥有该信息的时刻"——这恰恰是决策时序仿真所需要的那条边界。
