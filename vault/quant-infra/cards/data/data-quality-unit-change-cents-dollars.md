---
id: data-quality-unit-change-cents-dollars
node: data.quality
type: qa
---
## Q
A price series shows a stock jumping from $1.20 to $120.00 overnight with no corresponding corporate action (no reverse split, no news). Two very different explanations produce the exact same-looking jump in the raw numbers. What are they, and what check separates "real move" from "unit bug" before a strategy trades on it?

## A
**The two explanations are a genuine 100x price move (essentially never happens without a discrete cause) and a silent unit change in the feed — historically the single most common cause is a vendor or exchange switching between reporting prices in cents and dollars** (some legacy feeds, and some low-priced or foreign instruments, are natively quoted in cents; a vendor migration, a schema change, or a new data source being spliced into the same field without conversion produces exactly a 100x jump). The same class of bug shows up in other unit mismatches too: a currency redenomination not applied consistently, a per-share vs. per-100-shares quoting convention switch, or a vendor changing a field's scale factor without changing its name.

The check that separates them is a **bounded percent-change sanity filter combined with cross-source confirmation**: flag any single-bar return outside a wide but finite band (something like ±50% intraday for a normal equity, well beyond any plausible single-session move absent a known corporate action) for review rather than accepting it silently, then check it against (a) the corporate-actions feed — is there a documented split/reorg that would explain the jump, and (b) a second independent vendor for the same instrument and date — if vendor B shows $1.22, not $120.00, the discrepancy is a unit or parsing bug in vendor A, not a real move. Crucially, this check must run *before* the value reaches any return calculation or model input, because a 100x price jump silently becomes a 9,900% one-day return that will dominate any signal, risk model, or backtest statistic it touches — the discipline here is the same as elsewhere in data quality: reject and quarantine on an implausible value rather than let it flow downstream and hope a later stage catches it.

## Q zh
某只股票的价格序列一夜之间从 1.20 美元跳到 120.00 美元，且没有任何对应的公司行为（没有反向拆股，没有相关新闻）。有两种截然不同的解释会在原始数字上产生一模一样的跳变。这两种解释分别是什么？在策略据此交易之前，用什么检查能把"真实波动"和"单位错误"区分开？

## A zh
**这两种解释分别是一次真实的 100 倍价格变动（在没有离散原因的情况下基本不会发生），以及行情源里一次悄无声息的单位变更——历史上最常见的单一原因是供应商或交易所在以美分和以美元报价之间切换**（一些老旧行情源，以及一些低价或海外标的，原生就是以美分报价的；一次供应商迁移、一次表结构变更，或把一个新数据源拼接进同一个字段而未做换算，都会恰好产生 100 倍的跳变）。同一类 bug 也会出现在其他单位不匹配的场景中：货币重新计值没有被一致地应用、按每股 vs 按每百股的报价惯例切换，或供应商改变了某个字段的比例因子却没有改字段名。

区分两者的检查是一个**有界的百分比变化合理性过滤器，配合跨来源确认**：把任何超出一个宽但有限区间（对一只普通股票而言大致是日内 ±50%，远超在没有已知公司行为的情况下任何合理的单日波动）的单 bar 收益率标记出来待复核，而不是悄悄接受，然后对照（a）公司行为数据源——是否有一份记录在案的拆分/重组能解释这次跳变，以及（b）针对同一标的、同一日期的第二家独立供应商——如果供应商 B 显示的是 1.22 美元而不是 120.00 美元，那么这个差异是供应商 A 的单位或解析 bug，而不是一次真实波动。关键是，这项检查必须在这个数值进入任何收益率计算或模型输入**之前**运行，因为一次 100 倍的价格跳变会悄悄变成一个 9,900% 的单日收益率，主导它所触及的任何信号、风险模型或回测统计量——这里的纪律和数据质量的其他地方一样：对不合理的数值应当拒绝并隔离，而不是让它流向下游、寄希望于后面某个环节把它抓住。
