---
id: data-pit-asof-vendor-backfill-bias
node: data.point-in-time.as-of
type: qa
---
## Q
A fundamentals vendor advertises "20 years of history, always up to date." What does that phrase imply about how they built the historical file, and why does a bitemporal loader need to distrust it by default?

## A
**"Always up to date" almost always means the vendor keeps only the latest known value per period and backfills it across the whole history — not that they preserved each vintage as it was originally known.** When they onboard a new data field, restate a methodology, or fix a data error, the fix is applied retroactively to every historical row rather than inserted as a new, later-dated vintage. The file you download today therefore encodes today's knowledge as if it had always been available — this is **vendor backfill bias**, a special case of look-ahead bias that survives even a diligent `knowledge_date <= t` filter, because the vendor never captured a real knowledge date in the first place; every row silently carries `knowledge_date = today`.

The practical defenses: prefer vendors who sell true point-in-time / "as originally reported" datasets (they cost more and are slower to update); when only a backfilled file is available, treat its whole history as suspect for any field whose definition or methodology could plausibly have changed, and cross-check strategy performance against a period *before* the vendor started covering the instrument or field — a live/uncorrected out-of-sample window is the only way to catch this bias after the fact, since the historical file itself no longer contains the evidence.

## Q zh
某家基本面数据供应商宣传"20 年历史数据，始终保持最新"。这句话对他们如何构建历史文件意味着什么？为什么双时态加载器默认就应该不信任它？

## A zh
**"始终保持最新"几乎总是意味着供应商只保留每个期间目前已知的最新值，并把它回填到整段历史上——而不是保留了每个数值在当时被知晓时的原始版本。** 当他们上线一个新字段、重述某种方法论，或修复一个数据错误时，修正会被追溯应用到所有历史行，而不是作为一条更晚知晓日期的新版本插入。你今天下载到的文件因此把"今天已知的信息"编码得仿佛一直可得——这就是**供应商回填偏差（vendor backfill bias）**，是前视偏差（look-ahead bias）的一种特殊形式，即便认真按 `knowledge_date <= t` 过滤也躲不掉，因为供应商压根没有记录过真实的知晓日期；每一行都默默带着 `knowledge_date = 今天`。

实践中的防御手段：优先选择真正提供 point-in-time／"as originally reported"数据集的供应商（更贵、更新更慢）；当只能拿到回填过的文件时，对任何方法论或定义可能变过的字段，把它的整段历史都视为可疑；并在供应商开始覆盖该标的或字段**之前**的时间段里交叉验证策略表现——一个真正的、未经修正的样本外窗口，是事后捕捉这种偏差的唯一办法，因为历史文件本身已经不再保留证据。
