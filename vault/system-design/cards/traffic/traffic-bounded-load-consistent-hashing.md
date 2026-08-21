---
id: traffic-bounded-load-consistent-hashing
node: traffic.load-balancing
type: qa
---
## Q
Consistent hashing at the LB gives cache affinity, but plain consistent hashing has a load problem. What is it, and how does bounded-load CH fix it?

## A
Random ring placement plus skewed key popularity means some backends receive far more than the mean — affinity and balance fight each other, and a hot key can bury its home node.

**Bounded-load consistent hashing**: cap every server at `c × average load` (e.g. c = 1.25); when a key's home server is at its cap, spill to the next server around the ring. You keep ~affinity for most keys with a hard guarantee that no server exceeds the bound. Shipped in HAProxy (`hash-balance-factor`) and used for Google's and Vimeo's cache-affine routing.

## Q zh
LB 的一致性哈希给了缓存亲和性，但普通一致性哈希有负载问题。是什么，有界负载 CH 如何修复它？

## A zh
随机环放置加上倾斜的键热度意味着某些后端收到的远超平均值 — 亲和性和平衡互相对抗，热键可以埋掉它的主节点。

**有界负载一致性哈希**：将每个服务器限制为 `c × 平均负载`（例如 c = 1.25）；当键的主服务器处于其上限时，溢出到环周围的下一个服务器。你保持大多数键的约亲和性，同时有硬保证没有服务器超过界限。在 HAProxy 中已发布（`hash-balance-factor`），被 Google 和 Vimeo 的缓存亲和路由使用。

LB 的一致性哈希提供缓存亲和性，但普通一致性哈希有负载问题。是什么，有界负载 CH 如何修复它？

随机环位置加上偏斜的 key 流行意味着某些后端收到远大于平均值 — 亲和性和平衡彼此竞争，热 key 可能掩埋其主始节点。

**有界负载一致性哈希**：将每个服务器上限设为 `c × 平均负载`（例如 c = 1.25）；当 key 的主始服务器达到上限时，溅到环周围的下一个服务器。你用对大多数 key 的大致亲和性换取了硬保证，没有服务器超过界限。在 HAProxy（`hash-balance-factor`）中交付，并用于 Google 和 Vimeo 的缓存亲和路由。
