---
id: networking-http1-hol-workarounds
node: networking.protocols
type: qa
---
## Q
HTTP/1.1's head-of-line blocking lives at the application layer. What exactly blocks, and which browser-era hacks did it force (now anti-patterns under HTTP/2)?

## A
One connection carries **one request at a time**; responses must come back in order, and pipelining broke on middleboxes so browsers disabled it — leaving ~6 parallel TCP connections per host as the only concurrency.

Forced hacks: **domain sharding** (more hostnames → more connections), **concatenation/spriting** (fewer requests), inlining assets.

Under HTTP/2 multiplexing these hurt: sharding splits one prioritized connection into several and pays extra handshakes; concatenated blobs destroy caching granularity (one changed byte invalidates the bundle).

## Q zh
HTTP/1.1 的行首阻塞存在于应用层。到底是什么阻塞，哪些浏览器时代的 hacks 它强制（现在是 HTTP/2 下的反模式）？

## A zh
一个连接一次承载**一个请求**；响应必须按顺序回来，管道传输在中间盒上中断所以浏览器禁用它 — 留下每个主机约 6 个并行 TCP 连接作为唯一的并发。

强制的 hacks：**域名分片**（更多主机名 → 更多连接）、**连接/精灵化**（更少请求）、内联资产。

在 HTTP/2 多路复用下这些伤害：分片将一个优先级连接拆分成几个并支付额外的握手；连接的块破坏缓存粒度（一个改变的字节使整个包无效）。

HTTP/1.1 的行首阻塞活在应用层。确切地什么阻塞，浏览器时代的哪些黑客技巧它强制使用（现在在 HTTP/2 下是反模式）？

一个连接承载**一次一个请求**；响应必须按顺序返回，管道在中间件上破坏了所以浏览器禁用它 — 留下每个主机约 6 个并行 TCP 连接作为唯一的并发。

强制的黑客：**域名分片**（更多的主机名 → 更多连接）、**连接/精灵图**（更少请求）、内联资源。

在 HTTP/2 多路复用下这些伤害：分片将一个优先连接分成几个并支付额外握手；连接的 blob 破坏缓存粒度（一个改变的字节使整个包无效）。
