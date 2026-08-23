---
id: data-pit-asof-bitemporal-schema
node: data.point-in-time.as-of
type: qa
---
## Q
A fundamentals table has one `date` column and one `value` column per company. Every night the vendor overwrites old rows when a company restates. Six months from now, can you still reconstruct exactly what the table would have shown a researcher on any past date? What schema actually guarantees it?

## A
**No — a single-date table is destructive.** Each nightly overwrite replaces what was knowable in the past with what is known now, so once a restatement lands there is no way to recover the pre-restatement value from the table itself; the history you "have" is really a mix of vintages, most-recent-value-wins.

A **bitemporal table** fixes this by carrying two independent date axes instead of one:
- **Effective date** (a.k.a. valid time) — the real-world period the fact describes, e.g. "Q1 revenue."
- **Knowledge date** (a.k.a. transaction time) — when your system learned that fact, i.e. when the row was inserted or the correction landed.

Every restatement becomes a **new row** with the same effective date but a later knowledge date; nothing is ever overwritten or deleted. A point-in-time query then filters `knowledge_date <= t` and takes the latest row per effective date under that filter — reproducing exactly what was on file as of `t`, restatement history included. This is also why "point-in-time" data is strictly more expensive to store than a single current view: you are keeping every vintage, not just the latest one.

## Q zh
一张基本面数据表只有一个 `date` 列和一个 `value` 列。每天晚上，只要公司发生财报重述（restatement），供应商就会覆盖旧的那一行。六个月后，你还能精确还原出研究员在过去任意一天看到的表内容吗？真正能保证这一点的表结构是什么？

## A zh
**不能——单日期字段的表是破坏性的。** 每次夜间覆盖都会用"现在已知的"替换"过去可知的"，所以一旦重述落地，表本身就无法还原重述前的数值；你"拥有"的历史其实是各个版本混杂、只保留最新值的结果。

**双时态表（bitemporal table）**通过两条独立的时间轴而不是一条来解决这个问题：
- **生效日期（effective date，即 valid time）**——事实描述的真实世界期间，例如"Q1 营收"。
- **知晓日期（knowledge date，即 transaction time）**——你的系统何时得知这一事实，即该行被插入或更正落地的时间。

每次重述都会产生**新的一行**，生效日期不变、知晓日期更晚；不会有任何覆盖或删除。点时（point-in-time）查询随后过滤 `knowledge_date <= t`，并在该过滤条件下取每个生效日期最新的一行——精确还原出截至 `t` 时点档案上的内容，重述历史一并保留。这也是为什么"point-in-time"数据的存储成本天然高于单一当前视图：你保留的是每一个版本，而不只是最新版本。
