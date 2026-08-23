---
id: data-universe-delisting-return
node: data.point-in-time.universe
type: qa
---
## Q
A stock in your backtest gets delisted for bankruptcy. Your loader simply stops emitting rows for it from the delisting date onward — no more prices, no more positions. What does this do to the strategy's measured return, and what should happen instead?

## A
**Silently dropping the row is worse than including a bad number — it deletes the loss entirely.** If the backtest engine has no price after the delisting date, a position that was marked at, say, $8 the day before either freezes at $8 forever (overstating terminal wealth by the whole remaining value) or simply vanishes from the P&L computation as if the capital were never invested — both understate the loss from a bankruptcy that in reality usually wipes out most or all of the equity value.

The fix is to feed the engine an explicit **delisting return**: a synthetic final observation that closes the position out at the best available estimate of recovery value on the delisting date. CRSP, the standard academic source, assigns a fixed delisting return (famously **-30% for NYSE/AMEX delistings and -55% for Nasdaq delistings** when the true recovery value is unknown, per Shumway (1997), who showed the vendor's own default of simply omitting these observations was itself a source of survivorship bias in early studies). A production PIT dataset needs the same discipline: every delisting event carries a terminal return (from tender price, final trade, or a bankruptcy-recovery estimate), applied on the delisting date, so the position is closed with a realistic loss rather than silently disappearing.

## Q zh
回测中的一只股票因破产被摘牌。你的加载器从摘牌日起干脆不再输出该股票的行情——不再有价格，不再有持仓。这会对策略的测算收益造成什么影响？正确的做法应该是什么？

## A zh
**悄悄丢掉这一行比直接给一个糟糕的数字还要糟——它把这笔损失彻底抹去了。** 如果回测引擎在摘牌日之后拿不到任何价格，一个前一天还标价 8 美元的持仓要么永远冻结在 8 美元（把剩余全部价值都算进最终财富，虚高终值），要么直接从盈亏计算中消失，仿佛这笔资金从未投入过——两者都低估了一次破产事件通常会抹去大部分甚至全部股权价值这一现实。

正确做法是给引擎喂一个明确的**摘牌收益（delisting return）**：一条合成的最终观测值，在摘牌日按照能获得的最佳回收价值估计把持仓平掉。学术界的标准数据源 CRSP 在真实回收价值未知时会赋予一个固定的摘牌收益——著名的规则是**纽交所/美国证交所摘牌为 -30%，纳斯达克摘牌为 -55%**（出自 Shumway (1997)，他指出供应商默认直接省略这些观测值本身就是早期研究中存活者偏差的一个来源）。生产环境的 PIT 数据集需要同样的纪律：每一次摘牌事件都携带一个终止收益（来自要约收购价、最后一笔成交价，或破产回收估计），在摘牌日应用，让持仓以真实的亏损平仓，而不是悄悄消失。
