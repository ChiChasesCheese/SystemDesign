---
id: backtest-pbo-rank-to-pbo-stat
node: backtest.overfitting.pbo
type: qa
---
## Q
After running CSCV you have, for each of the 252 train/test splits, the out-of-sample rank of whichever configuration was the in-sample winner in that split. How does this collection of OOS ranks turn into the single number PBO, and what does PBO = 50% concretely say about those ranks?

## A
**Each split's IS-winner is converted from a raw OOS rank into a relative rank ω̄ ∈ (0,1)** — its percentile among all N configurations' OOS performance in that split — **then into a logit λ = ln(ω̄ / (1 − ω̄))**. λ > 0 means the IS-winner landed in the OOS top half for that split; λ ≤ 0 means it landed at or below the OOS median. **PBO is the fraction of the 252 splits where λ ≤ 0.**

PBO = 50% means: across the CSCV splits, the configuration you'd have picked by trusting in-sample performance lands in the **bottom half** out-of-sample just as often as the top half — the in-sample ranking carries zero information about how the same configuration ranks out-of-sample, exactly what coin-flip selection would produce. PBO near 0% means the IS-winner reliably stays an OOS top performer (in-sample ranking is genuinely informative — the selection procedure generalizes). PBO near 100% is a stronger and more damning result than 50%: it means the IS-winner reliably becomes an OOS **loser**, i.e. in-sample rank is actively anti-correlated with OOS rank — the metric being optimized in-sample is systematically rewarding whatever happens to reverse out of sample, the signature of a search that's tracking noise rather than signal.

## Q zh
跑完 CSCV 之后，你对 252 种训练/测试切分中的每一种，都拿到了"那次切分里样本内表现最好的配置"对应的样本外排名。这一组样本外排名是怎么变成 PBO 这一个数字的？PBO = 50% 具体在说这些排名的什么情况？

## A zh
**每次切分的样本内赢家，先从一个原始的样本外排名转换成相对排名 ω̄ ∈ (0,1)**——也就是它在该切分中所有 N 个配置样本外表现里所处的百分位——**再转换成一个 logit：λ = ln(ω̄ / (1 − ω̄))**。λ > 0 意味着该切分中样本内赢家落在了样本外的前一半；λ ≤ 0 意味着它落在了样本外中位数或以下。**PBO 就是 252 次切分中 λ ≤ 0 所占的比例。**

PBO = 50% 意味着：在所有 CSCV 切分中，如果你相信样本内表现去挑选配置，挑出来的那个落在样本外**后一半**的次数和落在前一半的次数一样多——样本内排名对该配置在样本外的排名毫无信息量，恰好就是硬币抛掷式随机选择会产生的结果。PBO 接近 0% 意味着样本内赢家可靠地保持样本外前列表现（样本内排名确实有信息量——这套选择流程能泛化）。PBO 接近 100% 比 50% 更糟、结论更狠：它意味着样本内赢家可靠地变成样本外的**输家**，即样本内排名与样本外排名是**主动负相关**的——样本内被优化的那个指标，系统性地奖励了那些恰好会在样本外反转的配置，这正是一个在追踪噪音而非信号的搜索过程的标志。
