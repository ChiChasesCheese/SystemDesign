---
id: data-pit-asof-naive-where-leak
node: data.point-in-time.as-of
type: qa
---
## Q
Your fundamentals table is properly bitemporal — it has both `report_date` (effective date) and `knowledge_date` (when the row was filed or corrected). A colleague writes the backtest query as `WHERE report_date <= t` because "that's the date the report is for." Why does this still leak the future, even though the table itself is correct?

## A
**Having the right schema does not save you from the wrong query.** `report_date <= t` only asks whether the *period a fact describes* has passed by `t` — it says nothing about whether the fact had been *published* by `t`. A company's Q1 (ending March 31) report is filed in April and often revised in a later 10-K/A in July; both the original and the revised row carry `report_date = 2024-03-31`. Filtering on `report_date` alone returns *every* row with that date — including the July restatement — at a simulated date in June, handing the strategy numbers that would not exist for another month.

The correct filter is on the **knowledge date**: `WHERE knowledge_date <= t`, then take the most recent row per `report_date` under that constraint. This is the single most common point-in-time bug in practice — the schema is bitemporal, the query only uses one of the two axes — and it is dangerous precisely because the backtest still runs, still produces a plausible-looking equity curve, and only fails once the strategy is live and no longer has access to the restated numbers early.

## Q zh
你的基本面数据表已经是正确的双时态表——同时有 `report_date`（生效日期）和 `knowledge_date`（该行被填报或更正的时间）。一位同事把回测查询写成 `WHERE report_date <= t`，理由是"这是报告对应的日期"。既然表结构本身是对的，为什么这条查询依然会泄露未来信息？

## A zh
**表结构正确并不能挽救错误的查询。** `report_date <= t` 只问某个事实所描述的期间是否已经在 `t` 之前结束——它完全没有回答这个事实是否在 `t` 之前已被**公布**。一家公司 Q1（3 月 31 日结束）的报告在 4 月才提交，往往还会在之后的 10-K/A 中修订；无论是原始行还是修订行，`report_date` 都等于 2024-03-31。只按 `report_date` 过滤会返回**所有**带该日期的行——包括 7 月的重述——即便模拟日期设在 6 月，也会把一个月后才会存在的数字喂给策略。

正确的过滤条件应作用于**知晓日期**：`WHERE knowledge_date <= t`，然后在该约束下对每个 `report_date` 取最新的一行。这是实践中最常见的点时（point-in-time）bug——表结构是双时态的，查询却只用了其中一条轴——之所以危险，正是因为回测依然能跑通，依然产出一条看似合理的净值曲线，只有到策略实盘、不再能提前拿到重述数字时才会暴露。
