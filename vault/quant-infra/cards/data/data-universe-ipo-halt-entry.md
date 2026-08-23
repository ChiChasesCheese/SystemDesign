---
id: data-universe-ipo-halt-entry
node: data.point-in-time.universe
type: qa
---
## Q
A momentum strategy adds a stock to its tradable universe the moment it starts appearing in the price database — which for a newly public company is its IPO day. What goes wrong with backtested fills on that day, and what is the standard fix?

## A
**IPO first-day prices are not representative, tradable prices for a typical strategy.** The trade prints are dominated by allocation dynamics rather than the same open-market price discovery the rest of the backtest assumes: a first-day "pop" (historically averaging well into double-digit percentages, sometimes 20-40%+ for hot IPOs) reflects the gap between the underwriter's offer price and where public demand actually clears, most shares are locked up with early holders (a typical 90-180 day lockup) rather than freely floating, and volume/liquidity in the first sessions is thin and unstable relative to the stock's eventual steady state — none of which resembles the liquidity a backtest's cost model assumes it can trade into.

The standard fix is a **seasoning window**: exclude a newly listed stock from the tradable universe for a fixed period after its offer date — commonly the first **1-6 months (≈20-126 trading days)** depending on the strategy's holding period — and enter the universe only once volume and price have stabilized past the initial pop and any early-days effect. The same discipline applies to a **halted stock**: a halt (news pending, LULD limit-up/limit-down, or a circuit breaker) means the last traded price is not a price you could actually transact at, so a backtest must either mark the position through the halt using the pre-halt price without allowing a fill, or wait for the reopen auction print — never treat a halt as a tradable moment.

## Q zh
某动量策略在一只股票开始出现在价格数据库中的那一刻起就把它加入可交易股票池——对新上市公司而言，这一刻就是 IPO 当天。当天的回测成交会出什么问题？标准的修正方法是什么？

## A zh
**IPO 首日价格对一般策略而言并不是有代表性、可交易的价格。** 成交价主要受配售动态支配，而不是回测其余部分所假设的那种公开市场价格发现：首日"暴涨"（historically 平均能达到两位数百分比，热门 IPO 有时高达 20-40%+）反映的是承销商发行价与公众真实需求出清价之间的差距，大部分股份被早期持有人锁定（典型锁定期 90-180 天）而非自由流通，最初几个交易日的成交量/流动性相对该股票最终的稳态而言既稀薄又不稳定——这些都不符合回测成本模型所假设的可交易流动性。

标准修正方法是设置一个**成熟窗口（seasoning window）**：在发行日之后的一段固定时间内——常见做法是最初 **1-6 个月（约 20-126 个交易日）**，具体取决于策略的持有周期——把新上市股票排除在可交易股票池之外，等到成交量和价格越过初期暴涨和早期效应、趋于稳定之后再纳入股票池。同样的纪律也适用于**停牌股票**：停牌（消息待发布、LULD 涨跌停机制、或熔断）意味着最后一笔成交价并不是你实际能够成交的价格，所以回测要么在停牌期间用停牌前价格标记持仓但不允许成交，要么等待复牌集合竞价的成交价——永远不要把停牌当作一个可交易的时点。
