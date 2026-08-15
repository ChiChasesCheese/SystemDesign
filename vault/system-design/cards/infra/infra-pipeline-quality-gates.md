---
id: infra-pipeline-quality-gates
node: infra.delivery
type: qa
---
## Q
Why order CI/CD pipeline stages as progressively more expensive quality gates, and what class of failure does each stage uniquely catch?

## A
Each stage should catch what is **cheapest to catch there**; the ordering exists so most failures die in seconds, not in production.

- **Build + unit tests** (seconds–minutes): logic errors, type/contract breaks.
- **Integration & contract tests** (minutes): wiring and API compatibility between services.
- **Staging / e2e**: environment-shaped bugs — config, migrations, cross-service flows.
- **Production canary**: the only gate with real traffic, real data, real scale — catches what no pre-prod environment can.

Design point: the pipeline *is* the release process. Any change that bypasses it (a manual config flip, an ad-hoc migration) is an ungated deploy.
