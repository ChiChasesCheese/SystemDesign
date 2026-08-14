---
id: reliability-config-deploy-risk
node: reliability.resilience
type: qa
---
## Q
Why are config/flag changes the riskiest deploy class — behind many of the largest real outages — and what discipline fixes it?

## A
Config changes bypass everything that makes code deploys safe: they often propagate **globally and near-instantly** (no canary, no batches), skip CI/tests, feel "small" so they skip review — and one bad value (routing rule, quota, feature flag) can take down every region at once.

Fix: treat config as a deploy artifact —

- **Version-controlled and validated** (schema/lint/dry-run before apply).
- **Progressive rollout** with the same canary stages as code, never global-at-once.
- **Automatic rollback triggers**: the rollout system watches SLIs and reverts on regression without waiting for a human.
