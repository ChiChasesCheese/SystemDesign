---
id: backtest-mt-fwer-vs-fdr
node: backtest.overfitting.multiple-testing
type: qa
---
## Q
A prop desk screens 200 candidate signals with the intent of deploying exactly one, live, with real capital. Separately, an academic-style research team screens 5,000 candidate factors with the intent of publishing a shortlist of ~50 for other researchers to validate further. Which multiple-testing control — family-wise error rate (FWER) or false discovery rate (FDR) — fits each situation, and why would using the wrong one break each process?

## A
**FWER controls the probability that *any* test in the batch is a false positive**; **FDR controls the *expected proportion* of false positives among the tests you flag as discoveries.** The right choice depends on what a false positive costs you.

The prop desk is picking one thing to trade — a single false positive *is* the outcome, dollar for dollar, so it needs **FWER control** (e.g. Bonferroni: divide the significance threshold by 200, or equivalently raise the required t-stat; this is the logic behind Harvey-Liu's argument that a "new factor" should clear a t-stat of ~3.0 rather than the conventional 2.0, once the size of the factor-zoo search is priced in). Using FDR here would be wrong: FDR happily tolerates flagging a controlled fraction of false positives as long as most flagged results are true, but the desk only cares about the *one* it deploys — a 10% expected false-discovery rate across 5,000 doesn't tell you whether the specific signal you picked is one of the false ones.

The academic screen is producing a *shortlist* for further, separate validation (backtests, PBO, out-of-sample) rather than deploying anything directly — so it can afford, and should want, **FDR control**: it tolerates a known fraction of false positives in exchange for much more statistical power to find the true signals among 5,000 candidates. Applying FWER here (Bonferroni over 5,000 tests) would set the bar so high that almost nothing survives, killing the recall the shortlist stage exists to provide — you'd throw away real candidates because the correction was calibrated for "acting on any single flagged result," not "handing 50 candidates to a second filtering stage."

## Q zh
某量化自营团队从 200 个候选信号里做筛选，目的是**只部署其中一个**、实盘真金白银交易。另一个学术风格的研究团队筛选 5000 个候选因子，目的是发表一份约 50 个因子的短名单，供其他研究者进一步验证。哪种多重检验控制方式——family-wise error rate（FWER）还是 false discovery rate（FDR）——分别适合这两种情形？用错了会怎样破坏各自的流程？

## A zh
**FWER 控制的是"整批检验里出现至少一个假阳性"的概率；FDR 控制的是"被标记为发现的结果中，假阳性所占比例"的期望值。** 选哪个取决于假阳性会让你付出什么代价。

自营团队要挑一个东西去交易——**一个假阳性就是最终结果本身**，真金白银地对应到亏损，所以需要 **FWER 控制**（例如 Bonferroni：把显著性阈值除以 200，等价于提高所需的 t 值；这正是 Harvey-Liu 主张"新因子"应过 t 值 ~3.0 而非传统的 2.0 的逻辑，一旦把整个因子文献的搜索规模计入）。在这里用 FDR 就错了：FDR 允许在总体大多数标记结果为真的前提下，容忍固定比例的假阳性被标记出来——但自营团队只关心自己部署的**那一个**，5000 个里 10% 的期望假发现率并不能告诉你，你挑中的这一个具体信号是不是那些假的之一。

学术筛选产出的是一份**短名单**，供之后独立的验证阶段（回测、PBO、样本外）继续把关，而不是直接部署任何东西——所以它承受得起、也应该追求 **FDR 控制**：以容忍已知比例的假阳性为代价，换取在 5000 个候选里找出真实信号的**统计功效**大幅提升。如果在这里用 FWER（对 5000 次检验做 Bonferroni），门槛会高到几乎没有任何东西能存活，扼杀掉短名单阶段本该提供的召回率——你会因为用了"针对任何单个标记结果直接行动"校准出的门槛，而丢掉真实候选，可这里的场景其实是"把 50 个候选交给下一道过滤"。
