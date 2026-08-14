---
id: patterns-creational-cues
node: patterns.creational
type: cloze
---
Creational pattern selection cues: many optional constructor parameters → {{c1::builder}}; must create consistent **families** of related objects (theme, vendor) → {{c2::abstract factory}}; let subclasses/plug-ins decide the concrete class of one product → {{c3::factory method}}; new instances are cheap copies of configured exemplars → {{c4::prototype}}; exactly one shared instance — prefer {{c5::a single instance wired at the composition root (DI)}} over a classic singleton.
