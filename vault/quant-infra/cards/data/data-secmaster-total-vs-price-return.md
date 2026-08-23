---
id: data-secmaster-total-vs-price-return
node: data.security-master
type: qa
---
## Q
A dividend-focused strategy's backtest uses "adjusted close" prices from a vendor and separately adds a cash credit to the simulated portfolio on each ex-dividend date, sourced from a corporate-actions feed. The backtest looks great; live trading underperforms it by roughly the dividend yield of the portfolio. What is the bug?

## A
**"Adjusted close" from most vendors is already a total-return series — dividends are baked into the price adjustment — so crediting the cash dividend separately double-counts it.** There are two legitimate, mutually exclusive series for any dividend-paying stock:
- **Price-return series**: the price path an investor who received but did not reinvest dividends would see — the price itself only reflects splits and other capital changes, not dividend reinvestment. Cash dividends must be added to the account separately (as this backtest did), which is correct *only if the price series is price-return*.
- **Total-return series**: dividends are treated as if immediately reinvested into more shares of the same stock, so the series' cumulative growth already includes the dividend income compounding — this is what most vendors ship by default under the label "adjusted close," because it is the standard series used for performance comparison against a total-return benchmark index.

Feeding a total-return-adjusted price series into a backtest *and* crediting the raw cash dividend on top counts the dividend twice: once implicitly, through the price series' embedded reinvestment, and once explicitly, through the cash credit. The backtest's simulated NAV grows too fast by roughly the dividend yield compounding every ex-date, which is exactly the gap this desk saw disappear once it hit live trading, where no such double-counting exists. The fix is to pick one series and one accounting treatment: total-return prices with **no** separate cash credit, or price-return prices **with** the cash credit — never both.

## Q zh
一个专注股息的策略回测使用供应商提供的"复权收盘价"（adjusted close），同时又根据公司行为数据在每个除息日给模拟组合额外记一笔现金入账。回测表现很亮眼；实盘交易的表现却大约比回测低了整个组合的股息收益率那么多。这个 bug 是什么？

## A zh
**多数供应商的"复权收盘价"本身就已经是全收益（total-return）序列——股息已经被烘焙进了价格复权里——所以再单独记一笔现金股息就重复计算了。** 对任何一只派息股票，存在两种合法但互斥的价格序列：
- **价格收益（price-return）序列**：一个收到了股息但没有再投资的投资者会看到的价格路径——价格本身只反映拆分等资本变动，不反映股息再投资。这种情况下现金股息必须单独记入账户（正如这个回测所做的那样），但**只有当价格序列是 price-return 时**这样做才是对的。
- **全收益（total-return）序列**：股息被视为立即再投资买入同一只股票的更多份额，所以该序列的累计增长里已经包含了股息收入的复利效果——这是大多数供应商在"复权收盘价"这个标签下默认提供的，因为这是用于对标全收益基准指数做业绩比较的标准序列。

把一条全收益复权价格序列喂进回测，**同时**又在其上额外记一笔原始现金股息，等于把股息计算了两遍：一遍隐含在价格序列内嵌的再投资里，一遍显式地体现在现金入账里。回测模拟的净值会因每个除息日复利叠加大约股息收益率那么多而虚高增长——这恰好就是这张交易台在进入实盘、不存在这种重复计算之后所看到的那部分差距。修正方法是只选一种序列、配一种记账方式：要么用全收益价格、**不**额外记现金，要么用价格收益价格、**配上**现金入账——两者不能同时用。
