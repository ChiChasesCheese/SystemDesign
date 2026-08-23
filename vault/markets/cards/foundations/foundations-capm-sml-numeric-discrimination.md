---
id: foundations-capm-sml-numeric-discrimination
node: foundations.capm
type: qa
---
## Q
Risk-free rate is 3%, market risk premium (E[Rm] − Rf) is 6%. Stock A has beta 0.8 and realized return 12%; Stock B has beta 1.5 and realized return 12%. Both realized the same 12% return — does the security market line say they were equally mispriced? Compute each stock's CAPM-predicted return and alpha, and state which one the model flags as an anomaly.

## A
**No — identical realized returns do not mean identical pricing outcomes under CAPM, because the model predicts different required returns for different betas.** SML-predicted return = Rf + β(Rm − Rf):

- Stock A: 3% + 0.8 × 6% = 3% + 4.8% = **7.8% predicted**. Realized 12% − predicted 7.8% = **+4.2% alpha**. A earned far more than its market-risk exposure justifies — CAPM flags it as underpriced (a positive-alpha anomaly worth explaining).
- Stock B: 3% + 1.5 × 6% = 3% + 9% = **12% predicted**. Realized 12% − predicted 12% = **0% alpha**. B earned exactly what its higher market-risk exposure entitled it to — CAPM has nothing to explain here, the stock sat right on the line.

So despite an identical headline return, A is the anomaly and B is not: CAPM's verdict depends entirely on realized return *relative to the return owed for the beta taken*, not on the raw realized number. This is the discrimination CAPM is built to make — and it's why "the stock went up a lot" is not the same claim as "the stock beat CAPM."

## Q zh
无风险利率是 3%，市场风险溢价（E[Rm] − Rf）是 6%。A 股票 beta 为 0.8，已实现收益 12%；B 股票 beta 为 1.5，已实现收益同样是 12%。两者已实现收益相同——按证券市场线（SML）来看，它们的定价偏离程度也相同吗？分别算出两只股票的 CAPM 预测收益和 alpha，并说明模型会把哪一只标记为异象。

## A zh
**不相同——在 CAPM 下，收益相同不代表定价结果相同，因为模型对不同的 beta 会预测不同的必要收益。** SML 预测收益 = Rf + β(Rm − Rf)：

- A 股票：3% + 0.8 × 6% = 3% + 4.8% = **预测 7.8%**。已实现 12% − 预测 7.8% = **alpha = +4.2%**。A 赚到的远多于其市场风险敞口所应得的——CAPM 把它标记为定价过低（一个值得解释的正 alpha 异象）。
- B 股票：3% + 1.5 × 6% = 3% + 9% = **预测 12%**。已实现 12% − 预测 12% = **alpha = 0%**。B 恰好赚到了其更高市场风险敞口应得的那份收益——CAPM 在这里没有什么需要解释的，这只股票正好落在线上。

所以，尽管两者表面收益相同，A 才是异象，B 不是：CAPM 的判定完全取决于已实现收益**相对于所承担 beta 应得收益**的差距，而不是原始收益数字本身。这正是 CAPM 被设计出来要做的那种区分——也是为什么"这只股票涨了很多"和"这只股票跑赢了 CAPM"根本不是同一回事。
