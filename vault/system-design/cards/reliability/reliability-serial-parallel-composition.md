---
id: reliability-serial-parallel-composition
node: reliability.availability
type: cloze
---
Components in **series** multiply availabilities: two 99.9% dependencies give {{c1::0.999 × 0.999 ≈ 99.8%}} — every hard dependency subtracts nines. Components in **parallel** (either can serve) give 1 − (1−A)², so two 99.9% replicas yield {{c2::99.9999%}} — assuming truly independent failure modes.
