---
id: patterns-proxy-kinds
node: patterns.structural
type: cloze
---
The four classic proxy variants, by what they gate: {{c1::virtual}} proxy defers creating an expensive object until first use; {{c2::protection}} proxy checks the caller's permissions before delegating; {{c3::remote}} proxy makes a network object look local (RPC stubs); {{c4::caching}} proxy memoizes results of expensive calls. All keep the real subject's interface, so clients need no changes.
