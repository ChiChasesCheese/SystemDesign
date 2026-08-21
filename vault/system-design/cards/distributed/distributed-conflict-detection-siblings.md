---
id: distributed-conflict-detection-siblings
node: distributed.replication.multi-leader
type: qa
---
## Q
Mechanically, how does a replica decide that two writes to the same key *conflict* rather than one superseding the other — and what does it do with the pair?

## A
Each key carries a **version vector** (one counter per leader/replica). A client reads, gets the value plus its version (an opaque "causal context"), and echoes that version on the next write. On arrival the replica compares:

- Incoming version **dominates** the stored one (≥ in every slot) → the writer saw the stored value; **overwrite**.
- Versions are **incomparable** → genuinely concurrent; keep **both as siblings**.

Siblings are then resolved by application semantics — merge (union a shopping cart, take the max), let the user pick, or apply a type whose merge is defined (CRDT). Riak/Dynamo expose siblings explicitly; the *failure* is a store that silently collapses incomparable versions with a timestamp, because that discards a write the system knew was concurrent.

## Q zh
Dynamo 风格的系统中如何检测和处理冲突兄弟值？

## A zh
**检测**：当读到一个 key 有多个版本（不同的 vector clock），表示有并发写冲突→产生 "siblings"。

**处理策略**：
- **Last-Write-Wins（LWW）**：按时间戳选最新的，简单但丢失数据。
- **应用层合并**：应用理解业务逻辑，手动合并兄弟值（e.g., 将购物车的两个版本合并成并集）。
- **向量时钟辅助**：用向量时钟判断是否真的并发（有偏序则不冲突）。

通常推荐应用层合并，因为 LWW 无法恢复丢失的数据。
