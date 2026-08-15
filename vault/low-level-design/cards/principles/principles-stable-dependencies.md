---
id: principles-stable-dependencies
node: principles.coupling
type: cloze
---
Coupling has a direction. **Afferent** coupling Ca = classes that {{c1::depend on this one}} (incoming, hard to change); **efferent** coupling Ce = classes {{c2::this one depends on}} (outgoing, easy to change). Instability I = {{c3::Ce / (Ca + Ce)}}, so I = 0 is maximally stable and I = 1 maximally unstable. The **stable-dependencies principle**: dependencies should point {{c4::toward more stable components}} — volatile code may depend on stable code, never the reverse. When the arrow must run the wrong way, fix it by {{c5::defining an interface owned by the depending (higher-level) side}} so the volatile detail depends on it instead.
