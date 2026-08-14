---
id: foundations-load-parameters
node: foundations.method
type: qa
---
## Q
"Scalable" is meaningless until you describe load. What are load parameters, and how do you pick the right one — e.g. for Twitter's home timeline?

## A
Load parameters are the numbers that describe demand on *your* architecture: QPS per operation, read/write ratio, concurrent connections, cache hit rate, working-set size — and crucially their **distribution**, not just averages.

Pick the parameter the bottleneck actually depends on: Twitter's is not tweet-write QPS (a few k/s) but **followers per user**, because each tweet fans out into ~75 timeline writes and the distribution is extremely skewed (celebrities). Naming the wrong parameter means designing for the wrong problem. See [[foundations-fanout-estimation]].
