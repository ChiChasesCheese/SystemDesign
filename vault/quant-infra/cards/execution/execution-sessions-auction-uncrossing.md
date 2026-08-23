---
id: execution-sessions-auction-uncrossing
node: execution.microstructure.sessions
type: qa
---
## Q
During continuous trading, every trade happens at whatever price two orders cross at, one pair at a time. The opening and closing auctions work completely differently. Mechanically, what is a call auction doing during the minutes it collects orders, and why does every participant get the same single price regardless of when they submitted their order?

## A
**A call auction batches orders instead of matching them one at a time, then computes the single price that clears the most volume, and fills everyone at that one price.** During the collection window (pre-open, or roughly the last 10 minutes before the close on US equities), buy and sell orders accumulate without executing — nothing trades yet. The exchange continuously publishes an **order imbalance**: the size that would be left over (and its direction) if the auction closed at the current indicative price, updated every few seconds so participants can see how lopsided the book is and adjust.

At the auction moment, an **uncrossing algorithm** searches across all resting orders for the single price that maximizes the matched quantity between buyers and sellers (with tie-breaks, e.g., minimizing leftover imbalance or favoring the price closest to the prior reference price). Every matched order — whether submitted at the very start of the collection window or seconds before the close — executes at that same clearing price. This is the mechanical reason auctions are described as fair to all participants regardless of arrival time within the window: unlike continuous price-time priority, being early buys you nothing on price, only a better chance of being included if the auction is imbalanced and some orders at the margin don't get filled.

## Q zh
在连续交易时段，每一笔成交都是两笔委托相互撮合出的价格，一对一对地成交。开盘和收盘拍卖的机制完全不同。在收集委托的那几分钟里，集合竞价（call auction）到底在做什么？为什么无论参与者何时提交委托，最后都能拿到同一个单一价格？

## A zh
**集合竞价是把委托批量攒起来，而不是一笔一笔撮合，然后计算出能成交最多量的那个单一价格，让所有人都按这一个价格成交。** 在收集窗口期间（美股一般是开盘前，或收盘前大约最后 10 分钟），买卖委托只是不断累积，此时并不真正成交。交易所会持续发布**委托失衡（order imbalance）**：如果按当前指示价格结束竞价，会剩下多少数量、方向是哪边，每隔几秒更新一次，让参与者看到盘口有多不平衡，从而调整自己的委托。

到了拍卖时刻，**撮合算法（uncrossing algorithm）**会在所有挂单中搜索出能让买卖双方成交量最大化的那一个价格（若有并列，再用一些规则打破，比如最小化剩余失衡，或优先选更接近前一个参考价的价格）。无论一笔委托是在收集窗口最开始提交的，还是收盘前几秒才提交的，只要被撮合，都按这同一个出清价格成交。这就是为什么说拍卖机制对窗口内任何时间提交委托的参与者都是公平的机制原因：不同于连续交易的 price-time priority，在这里早提交在价格上不占任何便宜，只是在拍卖出现失衡、边际委托可能拿不到成交时，能提高被纳入的概率。
