---
id: data-quality-cross-source-reconciliation
node: data.quality
type: qa
---
## Q
Vendor A and Vendor B both report AAPL's close for the same day as $190.12, agreeing to the cent. Does this agreement prove the price is correct? Give a real scenario where it wouldn't, and state what actually counts as independent confirmation.

## A
**No — agreement only proves correctness if the two sources are actually independent, and a great deal of "vendor diversity" in practice is not.** Many data vendors do not operate their own exchange connectivity; they resell or re-package a feed from the same handful of upstream sources (a SIP feed, a small number of consolidated-data resellers, or even each other). If Vendor A and Vendor B both ultimately source from the same upstream feed, a bug in that feed — a busted print that wasn't corrected, a stale-cache issue, a bad corporate-action adjustment applied upstream — will appear identically in both vendors' data. Two sources agreeing tells you the error, if any, wasn't introduced *independently* by each vendor's own pipeline; it tells you nothing about an error present in their shared upstream. This is exactly the incident described in the platform's own data-layer writeup: two independent-seeming cleaning passes both missed the same unadjusted spinoff because neither pass's error was independent of the shared root cause.

**Real independent confirmation requires provenance-verified independence** — knowing, not assuming, that two sources have genuinely separate paths back to the primary market: e.g. one source drawing from direct exchange feeds and another from a fundamentally different data lineage (a different SIP participant, a different exchange-licensed redistributor, or a manually-sourced regulatory filing rather than any market-data feed at all). Practically, this means a reconciliation system should track *and store* each source's actual upstream lineage, not just its vendor name, flag pairs that share an upstream as non-independent for reconciliation purposes even if they "usually" agree, and treat agreement between two known-independent sources as meaningfully stronger evidence than agreement between two sources of unknown or shared lineage.

## Q zh
供应商 A 和供应商 B 都把 AAPL 同一天的收盘价报告为 190.12 美元，精确到分都一致。这种一致是否证明这个价格是对的？给出一个不成立的真实场景，并说明真正算得上独立确认的是什么。

## A zh
**不能——一致只有在两个来源真正独立的前提下才能证明正确性，而实践中大量所谓的"供应商多样性"并不独立。** 许多数据供应商并不运营自己的交易所连接；他们转售或再打包来自同一小撮上游来源的行情（一路 SIP 行情、少数几家合并数据转售商，甚至彼此之间互相转售）。如果供应商 A 和供应商 B 最终都源自同一个上游行情，那么那个行情里的一个 bug——一笔未被更正的作废成交、一个缓存过期问题、一次上游应用错误的公司行为复权——会在两家供应商的数据里一模一样地出现。两个来源一致，只能说明如果存在错误，它不是由每家供应商各自的流水线*独立*引入的；它完全说明不了它们共享的上游里是否存在错误。这正是该平台自己数据层文章里描述的那次事故：两个看似独立的清洗流程都漏掉了同一次未复权的分拆，因为两个流程的错误都不独立于共同的根因。

**真正独立的确认需要经过溯源验证的独立性**——要真正知道、而不是假设两个来源回溯到主市场的路径是否确实分开：例如一个来源取自直连交易所行情，另一个来自根本不同的数据血统（不同的 SIP 参与方、不同的交易所授权再分发商，或干脆是人工采集的监管申报文件，而不是任何一路行情数据）。实践中，这意味着一个对账系统应当追踪*并保存*每个来源真实的上游血统，而不只是供应商名称，把共享同一上游的来源对，即便它们"通常"一致，也标记为在对账意义上不独立，并把两个已知独立来源之间的一致，视为比来源不明或血统共享之间的一致更强得多的证据。
