---
id: quality-divergent-vs-shotgun
node: quality.smells
type: qa
---
## Q
Divergent change vs shotgun surgery — both are change preventers. Distinguish them and give each one's fix.

## A
They're mirror images, defined by the mapping between *reasons to change* and *classes touched*:

- **Divergent change**: **one class, many reasons** — every new pricing rule, every new report format, every DB tweak all edit the same class. Fix: **extract class** — split by responsibility so each class has one reason to change (SRP).
- **Shotgun surgery**: **one reason, many classes** — adding a currency means small edits in 12 files. Fix: **move method/field** to consolidate the scattered behavior into one class (or introduce the missing abstraction that owns it).

Memory hook: divergent = too much *converges into* one class; shotgun = one change *sprays across* many.
