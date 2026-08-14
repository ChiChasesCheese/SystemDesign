---
id: async-queue-vs-pubsub
node: async.queues
type: qa
---
## Q
When do you choose a work queue (competing consumers) over pub/sub fan-out?

## A
- **Work queue**: each message is a *task* that exactly one consumer should perform (send email, resize image). Consumers compete; adding consumers increases throughput.
- **Pub/sub**: each message is a *fact* that multiple independent subscribers each need (order-placed → billing, analytics, notifications). Every subscriber group gets its own copy.
- Rule of thumb: one owner of the side effect → queue; many downstream reactions → pub/sub.
