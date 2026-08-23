---
id: execution-book-queue-position-asset
node: execution.microstructure.book
type: qa
---
## Q
Two traders each post a limit buy order at the same price, one at 9:30:00 and the other at 9:30:05. The price never moves and, an hour later, a large sell order arrives that only has enough size to fill the first order in the queue at that price. In price-time priority, why does this make queue position something you "earn" and "hold," rather than just a side effect of order routing?

## A
**Queue position is a claim on future fills that you accumulate purely by waiting, and it can be worth real money even though it costs nothing to acquire beyond patience.** In price-time priority, the 9:30:00 order sits strictly ahead of the 9:30:05 order for as long as both remain unchanged — every share that arrives to trade at that price fills the front order first. An hour later, when the large sell order shows up, the trader who posted five seconds earlier gets nothing; the trader who posted first gets filled at a price they wanted, with no spread paid and possibly a maker rebate earned. Nothing about size, cleverness, or later information mattered — only how long the order had already been resting.

This makes queue position an **asset with a value that grows the longer you hold it and resets to zero the instant you touch the order** (see the companion card on what a cancel-replace costs). It's why market makers who value queue position highly will sometimes decline to improve their own price or size even when conditions shift slightly — moving the order forfeits an accumulated position that may take minutes to rebuild, and in a fast market minutes of lost priority can mean the difference between capturing a fill during the good part of the queue and never being reached before the price moves away entirely.

## Q zh
两位交易者在同一价位挂了限价买单，一位在 9:30:00 挂单，另一位在 9:30:05 挂单。价格此后一直没变，一小时后来了一笔大卖单，数量只够成交这个价位排在队首的那一笔委托。在 price-time priority 下，为什么这会让"队列位置"成为一种需要"赚取"和"持有"的东西，而不只是订单路由的副产品？

## A zh
**队列位置是你单纯靠"等待"积累出来的、对未来成交的一种索取权，尽管获取它除了耐心不需要付出任何成本，它却能实实在在值钱。** 在 price-time priority 下，只要两笔委托都保持不动，9:30:00 那笔委托就一直严格排在 9:30:05 那笔前面——每一股来到这个价位成交的量，都先给排在队首的委托。一小时后大卖单出现时，晚挂 5 秒的那位交易者什么也拿不到；先挂单的那位则以自己想要的价格成交，没付价差，甚至可能还赚到做市返佣。数量大小、策略巧妙与否、后来获得的信息，统统不重要——重要的只是这笔委托已经挂了多久。

这使得队列位置成为一种**持有时间越长价值越高、而一旦你动它就瞬间归零的资产**（参见关于撤单重挂代价的配套卡片）。这也是为什么很看重队列位置的做市商，有时哪怕行情稍有变化，也宁可不去改善自己的价格或数量——挪动这笔委托意味着放弃一个可能要花几分钟才能重新积累起来的位置，而在快市场里，几分钟的优先权损失，往往就是"能在队列好位置吃到成交"和"价格跑掉前始终排不到自己"之间的区别。
