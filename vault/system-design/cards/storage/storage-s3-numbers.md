---
id: storage-s3-numbers
node: storage.object
type: cloze
---
S3-class object storage is designed for {{c1::11 nines (99.999999999%)}} of *durability* — achieved by erasure-coding/replicating across multiple availability zones — but its *availability* SLA is only around {{c2::99.9–99.99%}}, so callers must still handle 5xx/retries. Durability ≠ availability: your bytes survive, but you can't always read them right now.
