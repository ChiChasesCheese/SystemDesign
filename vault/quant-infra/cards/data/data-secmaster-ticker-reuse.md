---
id: data-secmaster-ticker-reuse
node: data.security-master
type: qa
---
## Q
You join two price files by ticker symbol: `AAIT` in 2013-2015 and `AAIT` in 2020-2024. Both ranges exist in your vendor's data under the same ticker. Why might this be silently splicing together two unrelated companies, and what identifier avoids the problem?

## A
**Ticker symbols are reused.** An exchange retires a symbol when a company delists (acquired, bankrupt, or moved exchanges) and, after a period, is free to assign that same short, memorable symbol to a completely unrelated new listing — it is a scarce, exchange-managed resource, not a permanent identifier. A naive time-series join keyed on ticker alone will happily concatenate company A's history with company B's history the moment their date ranges don't overlap, producing a single "instrument" whose price series has a nonsensical jump at the handover point and whose fundamentals mix two businesses — and because the join succeeds without error, this class of bug is invisible until someone notices an impossible return or an accounting ratio that makes no sense.

The fix is to key everything internally on a **permanent, non-reused identifier** — an internal surrogate key in the security master, or an industry identifier explicitly designed not to be recycled (see FIGI) — and treat the ticker as a *time-varying attribute* of that identifier (`instrument_id, ticker, valid_from, valid_to`), resolved through the security master rather than used as a join key directly. The same caution applies to company name and, to a lesser extent, CUSIP, both of which can also change or be reassigned around corporate actions.

## Q zh
你按股票代码（ticker）把两份价格文件拼接起来：2013-2015 年的 `AAIT` 和 2020-2024 年的 `AAIT`。供应商的数据里，这两段区间用的是同一个代码。为什么这可能悄悄把两家毫不相干的公司接到了一起？用什么标识符能避免这个问题？

## A zh
**股票代码是会被复用的。** 当一家公司退市（被收购、破产，或转板）时，交易所会把这个代码收回，过一段时间后就可以自由地把这个短小好记的代码分配给一家完全不相关的新上市公司——它是一种由交易所管理的稀缺资源，而不是永久性标识符。一个仅按代码做键的朴素时间序列拼接，一旦两段日期区间不重叠，就会心安理得地把 A 公司的历史和 B 公司的历史接在一起，产出一条"单一标的"，其价格序列在交接点会出现莫名其妙的跳变，基本面数据也混杂了两家公司——而且由于这次拼接不会报错，这类 bug 在有人注意到一个不可能的收益率或一个说不通的财务比率之前是完全隐形的。

修正方法是内部统一以**永久、不复用的标识符**为键——证券主数据（security master）里的内部代理键，或专门设计为不会被回收的行业标识符（见 FIGI）——并把股票代码当成该标识符的一个**随时间变化的属性**（`instrument_id, ticker, valid_from, valid_to`），通过证券主数据解析，而不是直接拿来当连接键。同样的谨慎也适用于公司名称，以及在较小程度上适用于 CUSIP——它们也都可能在公司行为前后发生变更或被重新分配。
