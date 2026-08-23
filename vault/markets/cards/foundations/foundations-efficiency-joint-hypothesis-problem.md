---
id: foundations-efficiency-joint-hypothesis-problem
node: foundations.efficiency
type: qa
---
## Q
A researcher finds that stocks with low price-to-book ratios earn statistically significant excess returns relative to CAPM's prediction over the following decade. Does this prove the market is inefficient? Explain the "joint hypothesis problem" that makes this conclusion impossible to draw cleanly.

## A
**No — every test of market efficiency is unavoidably a joint test of efficiency *and* whatever asset-pricing model was used to define "normal," expected return.** To call a return "abnormal" or "excess," the researcher first had to specify a benchmark for what return the stock *should* have earned given its risk — here, CAPM's Rf + β(Rm − Rf). The low-price-to-book stocks earned more than that CAPM benchmark predicted.

There are two equally consistent explanations for that gap, and the data alone cannot distinguish them: (1) the market is inefficient and is systematically mispricing these stocks, leaving free money on the table, or (2) the market is perfectly efficient, but CAPM is the wrong model of required return — book-to-market is proxying for a real, priced risk factor CAPM omits (distress risk, in the Fama-French interpretation), so the "excess" return is actually fair compensation for a risk the single-factor model doesn't capture. Fama (1970, revisited 1991) named this the joint hypothesis problem: because you can never test market efficiency without also assuming a specific equilibrium pricing model, a rejection of the model-plus-efficiency package can always be blamed on either half, and no clean test of efficiency alone exists — every "anomaly" in finance carries this ambiguity permanently attached.

## Q zh
某研究者发现，低账面市值比（低 price-to-book）的股票，在随后十年里相对 CAPM 的预测赚到了统计显著的超额收益。这能证明市场无效吗？请解释让这个结论无法被干净地得出的"联合假设问题（joint hypothesis problem）"。

## A zh
**不能——任何关于市场有效性的检验，都不可避免地是对"市场有效性"和"用来定义正常/预期收益的那个资产定价模型"的联合检验。** 要把某个收益称为"异常"或"超额"，研究者首先必须指定一个基准，代表这只股票按其风险"本应"赚到多少收益——这里用的基准是 CAPM 的 Rf + β(Rm − Rf)。低账面市值比的股票赚到的收益，高于这个 CAPM 基准的预测值。

对这个差距，存在两种同样自洽、数据本身无法区分的解释：(1) 市场是无效的，正在系统性地给这些股票定价错误，桌上留着白捡的钱；(2) 市场是完全有效的，但 CAPM 是一个错误的必要收益模型——账面市值比其实是在代理一个 CAPM 遗漏了的、真实存在且被定价的风险因子（按 Fama-French 的解读，是财务困境风险），所以这份"超额"收益其实是对单因子模型没能捕捉到的某种风险的合理补偿。Fama（1970 年提出，1991 年重申）把这称为联合假设问题：因为你永远无法在不假设某个具体均衡定价模型的前提下检验市场有效性，所以"模型 + 有效性"这个组合被数据拒绝时，责任永远可以推给其中任何一半——单独检验有效性本身的干净方法并不存在，金融学里每一个"异象"都永久带着这份无法消解的模糊性。
