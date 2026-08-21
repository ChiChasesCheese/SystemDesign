---
id: foundations-storage-estimate-method
node: foundations.estimation
type: qa
---
## Q
Estimate storage for 100M-DAU Twitter-like service, 2 tweets/user/day, ~1 KB/tweet (skip media), 5-year retention. Walk the math.

## A
- Writes/day: 100M × 2 = **2 × 10⁸ tweets/day**
- Data/day: 2 × 10⁸ × 1 KB = **200 GB/day**
- 5 years ≈ 2,000 days → **~400 TB** raw; ×3 replication → **~1.2 PB**

Keep every input a round power of ten and state units at each step — the method is the signal, not decimal precision.


## Q zh
快速估算存储需求的三步方法。

## A zh
1. **每个实体的大小**：一条用户记录或一条推文大约多少字节？（通常 100 字节到 1 KB）
2. **实体数量**：一年内会产生多少？从 DAU 和使用模式推导。例如 1M DAU × 365 天 × 每天 1 条推文 = 365M 推文/年。
3. **增长**：需要多少存储来容纳 1、3、5 年的数据？365M 推文 × 500 字节 ≈ 180 GB/年。

注意：这忽略了索引、复制、日志 — 实际上乘以 2–3。
