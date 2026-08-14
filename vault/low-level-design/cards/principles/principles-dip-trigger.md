---
id: principles-dip-trigger
node: principles.solid
type: qa
---
## Q
```java
class ReportService {
  private final MySqlReportStore store = new MySqlReportStore();
}
```
What does DIP say is wrong, what's the refactor, and how does DIP differ from dependency injection?

## A
High-level policy (`ReportService`) depends on a concrete low-level detail. DIP: both should depend on an abstraction shaped by the policy's needs — a `ReportStore` interface — so the dependency arrow points *toward* the policy.

Refactor: accept `ReportStore` via the constructor. DIP is the design rule (who depends on whom); **DI is merely the mechanism** that satisfies it by passing the concrete in from outside.
