---
id: carry-rates-fx-funding-currency-unwind
node: carry.rates-fx
type: qa
---
## Q
FX carry's characteristic crash is not a gradual reversal of the interest
differential — it's a specific, fast event. Describe the mechanics of a
funding-currency unwind (using the classic short-yen carry trade, and the
January 2015 Swiss franc de-peg, as examples) and explain why the damage
concentrates into days rather than unfolding slowly.

## A
**The crash is a synchronized rush to close the short leg, not a slow
repricing of the long leg.** In the classic trade, thousands of carry
positions are simultaneously short a low-yield funding currency (yen, or
Swiss francs while pegged) and long higher-yielding target currencies (AUD,
NZD, EM). When risk appetite drops sharply — a global growth scare, a
central bank surprise — carry traders across the market decide to unwind at
roughly the same time, which means everyone needs to *buy back* the funding
currency simultaneously to close their shorts.

That simultaneous buying is what makes the funding currency spike violently:
it isn't being bought because of new information about that currency's
fundamentals, it's being bought because leveraged positions across the
market are all closing the same short at once, and there is no natural
seller of that size on the other side at the prevailing price. In 2008, the
yen appreciated by double digits against multiple currencies within days as
the global carry trade unwound. In January 2015, the Swiss National Bank's
sudden removal of the EUR/CHF floor triggered a ~20-30% CHF move within
minutes as carry and peg-related positions were all forced to close at once
— years of accumulated carry income wiped out in a single session, on both
sides of the trade (the funding currency spikes, and the target currencies
carrying against it crater simultaneously). The damage concentrates into
days rather than unfolding slowly precisely because the trigger is a
correlated, leveraged unwind, not a change in economic fundamentals that
would take time to be priced in.

## Q zh
FX carry 特有的崩溃不是利率差的缓慢逆转——而是一次特定、快速的事件。请描
述融资货币逼空(unwind)的机制(以经典的做空日元 carry 交易、以及 2015 年
1 月瑞士法郎脱钩为例),并解释为什么损失会集中在几天之内,而不是缓慢展
开。

## A zh
**这场崩溃是对空头腿的同步、抢跑式平仓,而不是对多头腿的缓慢重新定价。**
在经典交易中,成千上万个 carry 头寸同时做空一种低息的"融资"货币(日元,
或者盯住汇率期间的瑞士法郎)、做多更高息的目标货币(澳元、纽元、新兴市场
货币)。当风险偏好骤降时——一次全球增长恐慌、一次央行意外决定——市场上的
carry 交易者会大致在同一时间决定平仓,这意味着所有人都需要**同时买回**融
资货币以平掉各自的空头。

正是这种同步买入让融资货币出现剧烈飙升:它被买入不是因为出现了关于这种货
币基本面的新信息,而是因为市场上大量加杠杆的头寸都在同一时间平掉同一个空
头,而在当时的价格上并没有一个规模相当的自然卖方接住这部分买盘。2008 年,
随着全球 carry 交易平仓,日元在几天内对多种货币升值了两位数百分比。2015
年 1 月,瑞士央行突然取消 EUR/CHF 的下限,导致 CHF 在几分钟内出现约
20%-30% 的波动,因为 carry 头寸和与盯住汇率相关的头寸被同时强制平仓——几
年积累的 carry 收益在单个交易时段内被抹去,而且交易的两端同时受损(融资货
币暴涨,而做多它去交易的目标货币同时暴跌)。损失之所以集中在几天之内而不
是缓慢展开,正是因为触发因素是一次相关性极高、加杠杆的平仓,而不是一个需
要时间才能被定价进去的经济基本面变化。
