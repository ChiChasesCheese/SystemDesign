---
id: backtest-pbo-fifty-percent-meaning
node: backtest.overfitting.pbo
type: qa
---
## Q
You ran CSCV over 20 parameter configurations of a single trading rule and got PBO = 52%. A colleague concludes "this proves the strategy doesn't work." Is that the right conclusion? What does PBO actually indict, and what could still be true about, say, configuration #14 specifically?

## A
**PBO indicts the selection procedure — "pick whichever configuration has the best in-sample Sharpe" — not any individual configuration.** A 52% PBO says that this specific act of choosing-the-IS-winner, applied across resampled train/test splits, is statistically no better than picking a configuration at random from the set: the in-sample-best config ends up at-or-below the OOS median about half the time. It says nothing about whether configuration #14 in particular — one fixed parameter set — has a real edge. PBO never singles out one configuration for a verdict; by construction it evaluates the *rule* ("select by in-sample performance") applied to the whole candidate set, not any member of that set individually.

So the colleague's conclusion overreaches: #14 could still be genuinely good, mediocre, or bad — PBO simply gives you no way to tell, because *in-sample performance is not a reliable signal for telling them apart here*. The practical consequence is about method, not verdict: if you believe a good configuration exists somewhere in that set of 20, in-sample-Sharpe-ranking is not how you'll reliably find it — you'd need a different route (an economically motivated prior on the parameter, more/better out-of-sample data, a structurally different validation scheme). And because PBO evaluates a selection procedure applied to *this specific candidate set*, it doesn't transfer: running CSCV on a different family of configurations requires a fresh PBO computation — a low or high PBO here says nothing about how trustworthy in-sample selection would be on a different set of candidates.

## Q zh
你对一条交易规则的 20 组参数配置跑了 CSCV，得到 PBO = 52%。一位同事得出结论："这证明这个策略不行。"这个结论对吗？PBO 到底指控的是什么？关于第 14 号配置本身，又可能仍然是什么情况？

## A zh
**PBO 指控的是选择流程——"挑样本内 Sharpe 最好的那个配置"——而不是任何一个具体配置。** PBO = 52% 说的是，这个具体的"挑样本内赢家"的动作，在重采样得到的训练/测试切分中反复执行时，统计上并不比从整个集合里随机挑一个更好：样本内最优的配置，大约一半的时候落在样本外中位数或以下。它对第 14 号配置——某一组固定的参数——本身是否有真实 edge 完全没有回答。PBO 从不针对某一个配置给出判决；从构造上看，它评估的是"按样本内表现挑选"这条**规则**应用于整个候选集合的效果，而不是集合中任何一个成员本身。

所以同事的结论下得过头了：第 14 号配置完全可能仍然是真正好的、平庸的，或者差的——PBO 单纯没有给出办法区分，因为**在这里，样本内表现根本不是能可靠区分它们的信号**。实际的后果是关于方法而非判决：如果你相信这 20 个配置里存在一个好的，靠"样本内 Sharpe 排名"并不是能可靠找到它的办法——你需要另一条路径（对参数有经济学依据的先验、更多/更好的样本外数据、结构上不同的验证方案）。而且由于 PBO 评估的是这套选择流程应用在**这个具体候选集合**上的效果，它不会迁移：对另一批不同的配置家族跑 CSCV，需要重新计算 PBO——这里的 PBO 高低，对另一批候选集合上样本内选择是否可信毫无参考价值。
