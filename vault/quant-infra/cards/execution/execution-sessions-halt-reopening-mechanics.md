---
id: execution-sessions-halt-reopening-mechanics
node: execution.microstructure.sessions
type: qa
---
## Q
A single-stock volatility halt triggers mid-session: the exchange stops all trading in the name for five minutes. When trading resumes, why doesn't it just pick back up where continuous trading left off, matching the next buy and sell orders that show up?

## A
**Reopening after a halt is treated as its own miniature opening auction, precisely to avoid letting one arriving order — or the first order to show up after a five-minute information vacuum — set a price for everyone.** During the halt, orders are allowed to accumulate but nothing executes, exactly like the pre-open collection window. If trading simply resumed as continuous matching, the very first order to arrive after the halt would trade against whatever was resting (or against a market order desperate to trade), and a single mistimed or manipulative order could print a price far from fair value in a market that has had zero price discovery for the halt's duration — a real risk given that halts are usually *triggered by* a sudden, possibly disorderly price move in the first place.

Instead, exchanges run a **reopening auction**: orders accumulate for a short window (often a minute or so), an indicative reopening price and imbalance are published and updated just like a normal open, and the uncrossing algorithm computes a single clearing price from the full set of accumulated interest before continuous trading resumes. This gives the market a chance to collectively re-discover a price after new information (the reason for the halt) has had time to be absorbed, rather than letting the first order in the door set it unilaterally. The consequence for any strategy: an order queued during a halt has no execution and no price information until the reopening auction actually clears — a resting limit order does not simply "wait its turn" the way it would in continuous trading.

## Q zh
盘中触发了单只股票的波动性熔断（volatility halt）：交易所暂停这只股票的交易 5 分钟。为什么恢复交易时，不是直接从连续交易断开的地方接着撮合下一笔买卖委托？

## A zh
**熔断后的重新开盘（reopening）被当作一次独立的迷你开盘拍卖来处理，目的正是为了避免让某一笔到达的委托——或者说 5 分钟信息真空之后第一笔出现的委托——单方面替所有人定出价格。** 熔断期间，委托可以继续累积，但不会成交，这跟盘前的收集窗口完全一样。如果交易恢复就是简单地继续连续撮合，那么熔断后第一笔到达的委托，就会和当时挂着的（或者一笔急于成交的市价单）直接对手成交，而一笔时机不当或带操纵性质的委托，就可能在一个熔断期间完全没有价格发现的市场里，打出一个严重偏离公允价值的成交价——考虑到熔断本身往往就是**由**突然的、可能失序的价格波动**触发**的，这个风险是真实存在的。

交易所的做法是运行一场**重新开盘拍卖（reopening auction）**：委托在一个较短的窗口内累积（通常一分钟左右），像正常开盘一样发布并更新指示性的重新开盘价格和失衡量，撮合算法基于全部累积的委托计算出单一的出清价格，之后连续交易才恢复。这给了市场一个机会，让新信息（也就是触发熔断的原因）有时间被消化后，集体重新完成价格发现，而不是让第一个进来的委托单方面定价。对任何策略的后果是：熔断期间排队的委托既不会成交，也拿不到价格信息，要等重新开盘拍卖真正出清——一笔挂着的限价单，并不会像在连续交易里那样"排队等着轮到自己"。
