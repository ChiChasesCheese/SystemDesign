---
id: storage-amplification-triangle
node: storage.internals
type: cloze
---
Storage engines juggle three amplifications you can't minimize simultaneously: {{c1::write amplification}} (bytes physically written per byte of user write — LSM compaction rewrites data many times), {{c2::read amplification}} (structures consulted per lookup — LSM reads may touch many SSTables, B-trees ~one path), and {{c3::space amplification}} (disk used vs live data — LSM holds obsolete versions until compaction; B-trees carry fragmented half-empty pages). Leveled compaction trades higher write amp for lower read/space amp; size-tiered does the reverse.
