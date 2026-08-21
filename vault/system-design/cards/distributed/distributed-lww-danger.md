---
id: distributed-lww-danger
node: distributed.time
type: qa
---
## Q
Why is last-write-wins by wall-clock timestamp a data-loss mechanism, not a conflict resolution strategy?

## A
Wall clocks on different nodes disagree: NTP sync leaves ms–100s of ms of skew, clocks **step backwards** on correction, and VMs pause. So "last" is decided by whichever node's clock runs fast — a genuinely later write can carry an *earlier* timestamp and be **silently discarded**. Cassandra-style LWW drops concurrent writes with no error and no trace.

Acceptable only when losing one of two concurrent updates is fine (e.g. idempotent "current status" values). Otherwise: version vectors to *detect* concurrency and merge, CRDTs, or route conflicting writes through a single leader. Hybrid: TrueTime-style bounded clocks (Spanner) make timestamp ordering safe by waiting out the uncertainty.

## Q zh
Last-Write-Wins（LWW）冲突解决有什么危险？

## A zh
**LWW**：并发写冲突时，取时间戳最新的写作为最终值，丢弃其他写。

**危险**：
1. **无声数据丢失**：旧的写被无声丢弃，应用未必察觉。
2. **时钟不可信**：如果时钟不同步或被恶意修改，可能选错值。
3. **违反业务逻辑**：e.g., 转账后撤销（撤销的时间可能比转账新），不应该选撤销。
4. **不可恢复**：丢失的数据无法恢复。

**何时安全**：只在幂等操作或值可以合并的场景（如 CRDT 计数器的递增）。

推荐：应用层检测冲突并手动合并，而不是盲目 LWW。
