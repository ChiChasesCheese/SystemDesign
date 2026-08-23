---
id: execution-fragmentation-nbbo-you-cant-trade
node: execution.microstructure.fragmentation
type: qa
---
## Q
Your smart order router reads the consolidated tape's NBBO, sees a bid of $50.02 on a venue, and routes a marketable sell order there. It arrives and fills at $50.00 instead. Nothing was wrong with your router's logic — what happened, and what would have shown the true, tradable price before you sent the order?

## A
**The NBBO you read off the consolidated tape (the SIP) is not necessarily the NBBO that still exists by the time your order physically arrives at the venue — it's a report of the past, not a live order book.** The SIP (Securities Information Processor) has to collect quote and trade updates from every exchange, aggregate them, and redistribute the consolidated NBBO — a pipeline that takes real processing and network time, historically on the order of low-to-mid single-digit milliseconds slower than a venue's own **direct feed** (the proprietary market data feed each exchange sells straight from its matching engine). In that gap, the $50.02 bid can be cancelled or filled by someone else — participants paying for direct feeds see the cancellation the instant it happens, while your router, working off the slower consolidated view, is still routing against a price that no longer exists.

This is why firms competing on execution quality pay for **direct feeds** from every venue rather than relying on the SIP: a router built on direct feeds sees each venue's actual current book, not a several-millisecond-old aggregate, and can route to where liquidity genuinely still is rather than where it *was*. The consequence of not doing this isn't just an occasional bad fill — it's a structural, repeatable disadvantage: any router working off the SIP is systematically a step behind anyone with direct-feed access, and that gap is exactly what latency arbitrage exploits (see the companion card).

## Q zh
你的智能路由器读取的是综合行情带（consolidated tape）上的 NBBO，看到某个交易所有 50.02 美元的买价，于是把一笔可成交的卖单路由过去。结果到达后是以 50.00 美元成交的。你的路由逻辑本身没有任何问题——到底发生了什么？在发单之前，什么东西本可以显示出真正可交易的价格？

## A zh
**你从综合行情带（SIP）上读到的 NBBO，未必就是你的委托真正到达该交易所时依然存在的那个 NBBO——它报告的是过去，而不是一份实时的盘口。** SIP（Securities Information Processor，证券信息处理商）需要从每一家交易所收集报价和成交更新、把它们汇总起来，再分发出综合 NBBO——这条流水线需要真实的处理和网络传输时间，历史上通常比交易所自己的**直连行情（direct feed）**（每家交易所直接从撮合引擎卖出的专有行情）慢上个位数到十位数毫秒不等。在这段差距里，那个 50.02 的买价可能已经被别人撤单或吃掉——付费订阅直连行情的参与者，在事情发生的瞬间就能看到撤单，而你的路由器用的是更慢的综合视图，仍然在朝着一个已经不存在的价格发单。

这就是为什么在成交质量上竞争的机构都会付费订阅每个交易所的**直连行情**，而不是依赖 SIP：一个建立在直连行情之上的路由器看到的是每个交易所的真实当前盘口，而不是一份滞后好几毫秒的汇总数据，因此能路由到流动性真正**还在**的地方，而不是它**曾经**所在的地方。不这样做的后果不只是偶尔吃到一次糟糕的成交——而是一种结构性的、可重复出现的劣势：任何依赖 SIP 的路由器，相对任何拥有直连行情的对手，都系统性地慢了一步，而这个差距，正是延迟套利（latency arbitrage）所利用的东西（见配套卡片）。
