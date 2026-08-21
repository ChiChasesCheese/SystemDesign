---
id: distributed-write-skew
node: distributed.transactions.isolation
type: qa
---
## Q
On-call rule: at least one doctor must stay on shift. Two doctors, in concurrent transactions, each check "≥2 on call" and sign themselves off. Both commit under snapshot isolation. Name the anomaly and two fixes.

## A
**Write skew**: each transaction's read set was invalidated by the *other's* write, but since they wrote **different rows**, SI's write-write conflict detection sees nothing.

- **Serializable isolation** (e.g. Postgres SSI): tracks read-write dependencies and aborts one transaction — then retry.
- **Materialize the conflict / lock the invariant**: `SELECT ... FOR UPDATE` on the rows read (or a single row representing the shift), forcing the transactions to serialize on a common lock.

Pattern to recognize: *read a predicate, write based on it* — always suspect write skew under SI.

## Q zh
什么是写偏差？为什么可重复读隔离不能防止它？

## A zh
**写偏差**：两个并发事务读相同的数据，基于那些数据进行计算，然后写入**不同的行**。每个写入满足约束，但合并违反。

例子："医生_on_call >= 1"。两个医生并发辞职：
1. Alice 查询计数 = 2，计算 ok_to_resign = true（会保留 1）。
2. Bob 查询计数 = 2，计算 ok_to_resign = true。
3. 两个都更新计数为 -1（它们各自写入不同行），计数变成 0。

为什么 RR 失败：RR 检测对**同一行**的冲突。这里它们写不同的行，所以没有检测。修复：谓词锁（锁定范围）、可序列化隔离，或应用级分布式锁。
