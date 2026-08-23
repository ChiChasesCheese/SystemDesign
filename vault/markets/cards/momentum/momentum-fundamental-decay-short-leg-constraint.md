---
id: momentum-fundamental-decay-short-leg-constraint
node: momentum.fundamental
type: qa
---
## Q
A researcher backtests PEAD on Chinese A-shares — long the highest-SUE
decile, short the lowest-SUE decile — and finds a strong long-short return.
But single-stock short-selling is heavily restricted in that market, so the
"deployable" version of the strategy can only hold the long leg. What should
you expect to happen to the strategy's performance, and what general fact
about where PEAD's alpha lives does this expose?

## A
**Expect most of the edge to disappear.** Studies of PEAD's live,
post-publication performance repeatedly find that the profit in a long-short
construction is concentrated in the short leg — shorting the worst-SUE,
biggest-miss stocks — rather than split evenly between the two legs; the
long leg (buying beat-and-raise names) on its own is considerably weaker and
often not statistically significant after costs. A market where single-name
shorting is banned or heavily restricted forces the strategy down to just
that weaker long leg, so what looked like a robust long-short anomaly in
backtest can collapse into an unremarkable, barely-there effect once it has
to be deployed under the market's real constraints.

More generally, this is one of the two forces behind PEAD's well-documented
post-publication decay (alongside McLean and Pontiff's broader finding that
anomaly returns shrink after academic publication as more capital hunts the
same signal): the anomaly is not "80% as strong" everywhere it's tried — its
strength is asymmetric across the long and short legs, so wherever the
short leg is constrained or costly to execute, the deployable version of
PEAD is structurally weaker than the academic long-short number, independent
of any further crowding or decay over time.

## Q zh
一位研究者在中国 A 股上回测 PEAD——做多 SUE 最高的一档、做空 SUE 最低的一
档——发现一个很强的多空收益。但这个市场对单只股票的做空有严格限制,所以策
略"可部署"的版本只能持有多头腿。你应该预期策略的表现会发生什么?这暴露了
关于 PEAD 的 alpha 到底藏在哪里的一个普遍事实是什么?

## A zh
**应该预期大部分 edge 会消失。** 关于 PEAD 在发表后实盘表现的研究反复发
现,多空构造里的利润集中在空头腿——做空 SUE 最差、最不及预期的股票——而不
是均匀分布在两条腿上;单独的多头腿(买入超预期且上调指引的股票)要弱得
多,扣除成本后往往不显著。一个禁止或严格限制单只股票做空的市场,会把策略
逼退到只剩这条较弱的多头腿,于是回测里看起来稳健的多空异象,一旦要在这个
市场的真实约束下部署,就可能塌缩成一个平平无奇、几乎不存在的效应。

更一般地说,这是 PEAD 有据可查的发表后收益衰减背后的两股力量之一(另一股
是 McLean 和 Pontiff 更广泛的发现:随着更多资金追逐同一个信号,异象收益在
学术发表后会收缩):这个异象并不是"在任何地方部署都还剩 80% 的强度"——它
的强度在多头腿和空头腿之间是不对称的,所以无论在哪个市场空头腿受限或执行
成本高昂,PEAD 可部署的版本都会在结构上比学术论文里的多空数字更弱,这和随
时间推移进一步的拥挤或衰减是两回事。
