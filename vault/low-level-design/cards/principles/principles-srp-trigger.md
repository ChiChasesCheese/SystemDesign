---
id: principles-srp-trigger
node: principles.solid
type: qa
---
## Q
`Invoice` computes totals, renders itself to PDF, and saves itself to the DB. Which SOLID principle flags this, what is the actual test, and the refactor?

## A
**SRP**. The test is *reasons to change*, not "does one thing": accounting changes the totals, design changes the layout, the DBA changes persistence — three stakeholders, one class.

Refactor: keep domain math in `Invoice`; extract `InvoicePrinter` and `InvoiceRepository`. Each class now changes for exactly one actor.
