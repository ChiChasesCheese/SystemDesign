---
id: execution-fragmentation-lit-vs-dark
node: execution.microstructure.fragmentation
type: qa
---
## Q
US equities trade across more than a dozen lit exchanges plus dozens of dark pools operated by banks and market makers. You need to sell 200,000 shares of a name that trades 2 million shares a day without moving the price against yourself before you're done. Why would you route part of that order to a dark pool instead of just posting it on a lit exchange, and what do you give up by doing so?

## A
**A dark pool lets you express trading interest without publishing it, which is exactly what a size order needs to avoid signaling its own presence — the trade-off is giving up the certainty and priority mechanics that a displayed order gets.**

- **Lit venues** publish every resting order's price and size as part of the public quote stream that feeds the NBBO. Posting 200,000 shares there — or even a visible slice of it — tells every participant, including predatory ones, that a large seller is present, inviting them to trade ahead of your remaining size (front-running the signal) or to widen their own quotes against you. In exchange, you get full price-time priority and certainty about exactly where you stand in the queue.
- **Dark pools** accept orders with no pre-trade transparency — nothing about your order's existence, size, or price is published. Most execute at the **midpoint** of the current NBBO (so neither side pays the spread), letting an institution work a large order without revealing intent or moving the displayed market. What you give up: no displayed queue means no guaranteed priority mechanics to reason about, execution is uncertain (you only fill if a natural contra order happens to be resting there too), and dark pools are not immune to information leakage — some attract "pinging" flow from participants who send small orders specifically to detect the presence of large resting interest, and pool operators vary widely in how well they police predatory subscribers.

The practical answer for the 200,000-share order: split it — work a portion passively in one or more dark pools to capture midpoint fills against natural contra-flow with zero footprint, while the lit-venue portion still needs a schedule (see the algos leaf) because dark pools alone rarely have enough resting natural liquidity to complete a size order on their own.

## Q zh
美股在十几家挂牌交易所之外，还有几十家由银行和做市商运营的暗池（dark pool）在交易。你需要卖出 20 万股某只日成交量 200 万股的股票，并且要在卖完之前尽量不把价格砸向自己不利的方向。为什么你会把这笔单的一部分路由到暗池，而不是直接挂在明面交易所上？这样做又放弃了什么？

## A zh
**暗池让你能够表达交易意愿而不公开它，这正是一笔大单要避免暴露自身存在所需要的；代价是放弃了显示委托才有的确定性和优先权机制。**

- **明面交易所（lit venues）** 会把每一笔挂单的价格和数量作为公开报价流的一部分发布出去，这些报价流构成了 NBBO。把 20 万股——哪怕只是可见的一小片——挂在那里，等于告诉所有参与者（包括掠夺性的那些）有一个大卖家在场，招来别人抢在你剩余的量之前交易（利用这个信号抢跑），或者让他们把自己的报价往对你不利的方向拉开。作为交换，你得到完整的 price-time priority，能确切知道自己在队列里排第几。
- **暗池** 接受委托但没有任何盘前透明度——你的委托是否存在、数量、价格，统统不公开。大多数暗池按当前 NBBO 的**中点**成交（这样双方都不用付价差），让机构可以在不暴露意图、不影响显示行情的情况下处理一笔大单。你放弃的是：没有可见队列就意味着没有可推理的确定性优先权机制，成交本身是不确定的（只有恰好有天然对手盘挂在那里你才会成交），而且暗池也并非对信息泄露免疫——有些暗池会吸引"试探式（pinging）"资金流，这些参与者专门发小单来探测是否有大额挂单存在，不同暗池运营商对掠夺性用户的监管力度也参差不齐。

对这笔 20 万股订单的实际做法是：拆分——把一部分放在一个或多个暗池里被动执行，靠天然对手盘拿中点成交、零足迹，而明面交易所那部分仍然需要一个执行计划（见 algos 那一支），因为暗池单靠自己的天然挂单量，很少能独自吃完一笔大单。
