---
id: storage-encoding-compat-directions
node: storage.encoding
type: cloze
---
Schema evolution has two directions: {{c1::backward compatibility}} means **new code can read data written by old code** (the common, easier case — new readers handle old records), while {{c2::forward compatibility}} means **old code can read data written by new code** (harder — old readers must tolerate fields they don't know about, typically by {{c3::preserving/ignoring unknown fields}} rather than erroring or silently dropping them on rewrite).
