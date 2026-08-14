---
id: distributed-total-order-broadcast
node: distributed.consensus
type: cloze
---
Total order broadcast guarantees {{c1::reliable delivery (no message lost) and totally ordered delivery — every node sees the same messages in the same order}}; it is formally {{c2::equivalent to consensus — each position in the shared log is one consensus decision, so Raft/Paxos give you TOB and vice versa}}. You get linearizable compare-and-set/uniqueness on top of it by {{c3::appending your claim to the log, reading the log back, and winning only if your message is the first claim for that key — log position is the serial order}}. This log framing is why "replicated state machine", "Raft log", and "Kafka partition ordering" are the same idea at different fault-tolerance levels.
