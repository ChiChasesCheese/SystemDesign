---
id: principles-isp-trigger
node: principles.solid
type: qa
---
## Q
Your `Machine` interface declares print/scan/fax; the basic printer implements `scan()` and `fax()` as throwing stubs. Which principle, and the refactor?

## A
**ISP** — no client (or implementer) should be forced to depend on methods it doesn't use. Those throwing stubs are also latent LSP bombs: any caller holding a `Machine` can blow up.

Refactor into role interfaces `Printer`, `Scanner`, `Fax`; the multifunction device implements all three; each client takes only the role it needs. Trigger to memorize: **no-op or throwing implementations = fat interface**.
