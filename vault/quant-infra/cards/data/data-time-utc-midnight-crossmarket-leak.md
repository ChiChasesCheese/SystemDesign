---
id: data-time-utc-midnight-crossmarket-leak
node: data.market-data.time
type: qa
---
## Q
Your daily-bars table stores every instrument's daily bar with the same UTC-midnight timestamp — a storage convention for "this row is for calendar date D." A cross-sectional model joins a Tokyo-listed stock's daily bar and a New York-listed stock's daily bar on that shared date and computes same-day features from both. Why can this let the model see information it shouldn't have?

## A
**A shared UTC-midnight timestamp says two rows describe the same calendar date; it says nothing about whether their trading sessions actually overlapped or which one closed first.** Tokyo's regular session (roughly 09:00-15:00 JST) closes in the middle of the New York trading day, hours before New York's own session even opens (NYSE regular hours are roughly 09:30-16:00 ET, and Tokyo's afternoon is New York's very early morning). So "Tokyo's bar for date D" is fully determined and closed before "New York's bar for date D" has traded a single share — the two rows sharing a date label are separated by roughly half a trading day of real elapsed time, with Tokyo strictly earlier.

If a same-day cross-sectional join treats both as simultaneously "known as of date D close," a feature computed from the New York bar and used to explain or predict the Tokyo bar dated the same day is leaking information from later in the day — real time — into a signal timestamped as if it were available beforehand. The label "date D" hides this because it looks like a single point in time when it is really two different, non-overlapping intervals collapsed onto one calendar stamp. The fix is to key cross-market joins on **session close instants in a common timezone (or UTC)**, not on the shared calendar-date label — so a query can correctly ask "which of these two closes actually happened first" instead of assuming same-labeled dates are simultaneous.

## Q zh
你的日线表把每个标的的日线 bar 都存成同一个 UTC 零点时间戳——这是一个表示"这一行是日历日期 D 的数据"的存储惯例。一个截面模型把一只东京上市股票的日线 bar 和一只纽约上市股票的日线 bar 按这个共同日期做连接，并用两者计算同一天的特征。为什么这可能让模型看到它本不该看到的信息？

## A zh
**共同的 UTC 零点时间戳只表示两行描述的是同一个日历日期；它完全没有说明这两个交易时段是否真的有重叠，或者哪一个先收盘。** 东京的常规交易时段（大致 09:00-15:00 日本时间）在纽约交易日进行到一半时就已经收盘，比纽约自己的时段开盘还要早好几个小时（纽交所常规交易时间大致是美东 09:30-16:00，而东京的下午对应的是纽约的凌晨很早）。所以"日期 D 的东京 bar"在"日期 D 的纽约 bar"还没成交一股之前，就已经完全确定并收盘了——两行共享同一个日期标签，实际经过的真实时间却相差大约半个交易日，而且东京严格地更早。

如果一次同日截面连接把两者都当作"截至日期 D 收盘时同时已知"，那么一个用纽约 bar 计算出来、用来解释或预测同一天东京 bar 的特征，就是在把当天更晚（真实时间上）的信息，泄露进一个本应标记为"事前已可得"的信号里。"日期 D"这个标签把这一点藏了起来，因为它看起来像单一的一个时点，实际上是两个不重叠的区间被压缩到同一个日历戳上。修正方法是把跨市场连接的键设为**统一时区（或 UTC）下的收盘时刻**，而不是共享的日历日期标签——这样查询才能正确地问"这两个收盘事件里到底哪一个真正先发生"，而不是假设标签相同的日期就是同时发生的。
