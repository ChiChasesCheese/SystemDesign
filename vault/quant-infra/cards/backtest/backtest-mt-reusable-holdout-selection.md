---
id: backtest-mt-reusable-holdout-selection
node: backtest.overfitting.multiple-testing
type: qa
---
## Q
A researcher trains a strategy only on 2010-2019 data, then checks its Sharpe on the untouched 2020-2024 holdout. It's mediocre, so they tweak the entry threshold and check the holdout again. Not great, tweak again, check again — six iterations total — and ship the last version, logging `n_trials=1` because "I only trained on one period, 2010-2019." What's wrong with `n_trials=1`, and what should have been counted?

## A
**Every adaptive look at the holdout that informs the next change is a trial, whether or not a formal parameter got re-fit on that data.** This is the reusable-holdout problem (Dwork et al. 2015, "The reusable holdout," *Science*): repeatedly querying a held-out set and adjusting based on what you saw turns that set into a second training set, even though no optimizer ever touched its rows directly — the researcher's own judgment is the optimizer, and their brain updated on every one of the six looks. A holdout is only "clean" — genuinely informative about generalization — if it is queried **once, non-adaptively**, after everything else is frozen.

The honest trial count here is **6**, not 1: six times the strategy (in whatever form it existed at that moment) was evaluated against the same 2020-2024 window and the result fed back into a decision. Logging `n_trials=1` and computing a deflated Sharpe or PSR against that count understates the search that actually happened, feeding an artificially low significance bar into the gate — a lucky sixth try then looks like a single clean out-of-sample confirmation instead of the survivor of six adaptive rounds. The fix is either a **third, genuinely untouched split** reserved for the one final decision, or querying the holdout through a mechanism (e.g. adding calibrated noise, as in the reusable-holdout literature) that limits how much information each look leaks.

## Q zh
一位研究者只用 2010-2019 年的数据训练策略，然后在未碰过的 2020-2024 留出集（holdout）上检查 Sharpe。表现平平，于是调整入场阈值再看一次留出集；不够好，再调再看——总共六轮——最后上线最后一版，并把 `n_trials` 记为 1，理由是"我只在 2010-2019 这一个时期上训练过"。`n_trials=1` 错在哪里？本该记录的是什么？

## A zh
**每一次基于观察留出集结果而做出下一步调整的"自适应查看"都是一次试验，无论那次调整有没有正式地在这份数据上重新拟合参数。** 这就是可重用留出集问题（reusable-holdout problem，Dwork et al. 2015，"The reusable holdout"，*Science*）：反复查询一个留出集并据此调整，会把这个留出集变成第二个训练集，哪怕没有任何优化器直接碰过它的行数——研究者自己的判断就是那个优化器，六次查看中的每一次都在更新他的判断。留出集只有在**一次性、非自适应**地被查询、且此前一切已经冻结的情况下，才是"干净的"、真正能反映泛化能力的。

这里诚实的试验次数是 **6**，而不是 1：策略（无论当时是哪个版本）在同一个 2020-2024 窗口上被评估了六次，每次结果都反馈进了一个决定。把 `n_trials` 记成 1 再据此算 deflated Sharpe 或 PSR，会低估实际发生的搜索规模，把一个人为偏低的显著性门槛喂给闸门——于是第六次的幸运结果，看起来就像一次干净的样本外确认，而不是六轮自适应筛选后的幸存者。修复方式要么是留出**第三份、真正未被碰过的数据**专门用于最后那一次决定，要么通过某种机制（比如可重用留出集文献里的、加入校准噪音）查询留出集，限制每次查看能泄漏多少信息。
