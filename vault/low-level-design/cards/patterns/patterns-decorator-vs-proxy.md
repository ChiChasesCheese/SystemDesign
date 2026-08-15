---
id: patterns-decorator-vs-proxy
node: patterns.structural
type: qa
---
## Q
Decorator and proxy have identical structure — same interface, wrap the real object, delegate. What actually distinguishes them?

## A
**Intent and who controls composition.**

- **Decorator** *adds behavior* the client chose: the client (or composition root) stacks wrappers at will — `new Buffered(new Encrypted(new FileStream(...)))`. Open-ended, stackable, order matters.
- **Proxy** *controls access* to the object on its own authority: lazy loading (virtual), permissions (protection), remoteness, caching. The client usually doesn't know or decide it's there; typically exactly one proxy, often managing the real object's lifecycle itself.

Interview tell: "add responsibilities dynamically" → decorator; "stand in for / gate access to" → proxy.
