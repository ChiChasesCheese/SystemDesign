---
id: infra-flags-deploy-release
node: infra.delivery
type: cloze
---
Feature flags separate {{c1::deploy}} (code reaches production, dark and inert) from {{c2::release}} (behavior exposed to users) — shipping becomes routine and low-stakes, exposure becomes a runtime decision per cohort, and reverting is an instant {{c3::kill switch (flag off)}} instead of a redeploy. The tax: stale flags multiply untested code-path combinations, so every flag needs an owner and an expiry.
