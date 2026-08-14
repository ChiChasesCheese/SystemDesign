---
id: foundations-latency-sequential-reads
node: foundations.numbers
type: cloze
---
Reading 1 MB sequentially: from memory {{c1::~10–50 µs}}, from SSD {{c2::~200 µs–1 ms}} — sequential I/O is close enough to memory speed that {{c3::append-only / log-structured}} designs deliberately trade random writes for sequential ones.
