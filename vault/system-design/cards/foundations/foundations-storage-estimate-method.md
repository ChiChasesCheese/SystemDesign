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
