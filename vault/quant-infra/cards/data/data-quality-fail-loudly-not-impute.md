---
id: data-quality-fail-loudly-not-impute
node: data.quality
type: qa
---
## Q
A pipeline hits a missing price for one instrument on one day and, rather than stopping, forward-fills it with the previous day's close so the downstream job doesn't crash. Three months later a strategy built on this data shows a suspicious edge around exactly that kind of gap. What's the actual failure here, and what should the pipeline have done instead?

## A
**Silently imputing a missing or suspect value doesn't just risk being wrong — it manufactures a specific, exploitable artifact and hides the evidence that anything happened at all.** A forward-filled price is, by construction, a zero-return day for that instrument regardless of what the real (unknown) price did — if the imputation happens disproportionately around a specific kind of event (a feed outage correlated with high-volatility days, say, because that's when systems are most stressed), the model can learn to associate "suspiciously flat return" with whatever else tends to co-occur with outages, discovering a pattern in *data pipeline behavior* rather than in markets. This is a subtler cousin of survivorship and lookahead bias: the strategy isn't cheating by seeing the future, it's cheating by exploiting a systematic artifact of how the data was repaired, and because the imputation was silent, nothing in the dataset flags which rows are real and which are filler — the bug is invisible to anyone auditing the strategy's inputs after the fact.

**The correct discipline is to fail the pipeline loudly and quarantine the affected data rather than auto-correct it**: when a value is missing or fails a sanity check, the job should stop (or explicitly mark that instrument/date as quarantined and excluded), emit an alert, and require either a human decision or a documented, versioned correction rule before that data is used — not silently substitute a plausible-looking number and continue. The reasoning is asymmetric: a visible gap gets investigated, understood, and either legitimately backfilled with the real value or explicitly excluded with a clear audit trail; a silent wrong fill compounds invisibly into every downstream statistic that touches it and is discovered, if ever, only by accident — as in this scenario, months later, as an inexplicable "edge" that is actually a bug wearing an alpha's clothes.

## Q zh
一个流水线在某一天遇到某个标的价格缺失，没有停下来，而是用前一天的收盘价做前向填充，好让下游任务不至于崩溃。三个月后，一个基于这份数据构建的策略在恰好类似这种缺口周围表现出可疑的"优势"。这里真正的问题出在哪？流水线本应怎么做？

## A zh
**悄悄填补一个缺失或可疑的数值，不仅仅是有可能填错——它会制造出一个具体的、可被利用的人为痕迹，并且把发生过这件事的证据一并抹去。** 一个前向填充的价格，按构造方式，就是该标的当天的零收益率，无论真实（未知）价格实际发生了什么变化——如果这种填充不成比例地集中出现在某类特定事件周围（比如行情中断恰好和高波动日相关，因为那正是系统压力最大的时候），模型就可能学会把"可疑地持平的收益率"和其他常常与行情中断同时出现的因素关联起来，发现的是**数据流水线行为**里的模式，而不是市场里的模式。这是存活者偏差和前视偏差的一个更隐蔽的表亲：策略作弊靠的不是看到了未来，而是利用了数据被修复方式所带来的系统性人为痕迹，而且由于填充是悄悄进行的，数据集里没有任何标记能区分哪些行是真实的、哪些是填补出来的——事后审计策略输入的人根本看不出这个 bug。

**正确的纪律是让流水线大声地失败，把受影响的数据隔离起来，而不是自动纠正它**：当一个数值缺失或未通过合理性检查时，任务应当停止（或明确把该标的/日期标记为隔离并排除在外）、发出告警，并要求在这份数据被使用之前，要么由人做出决策，要么套用一条有文档记录、有版本管理的修正规则——而不是悄悄替换成一个看起来合理的数字然后继续跑下去。这里的道理是不对称的：一个可见的缺口会被调查、被理解，然后要么用真实数值合法地回填，要么带着清晰的审计轨迹被明确排除；而一个悄悄填错的值，会不可见地复合进每一个触及它的下游统计量里，即便有朝一日被发现，往往也只是出于偶然——就像本题的场景一样，几个月后，以一个说不清道不明的"优势"的面目出现，而它其实是一个披着 alpha 外衣的 bug。
