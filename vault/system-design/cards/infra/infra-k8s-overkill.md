---
id: infra-k8s-overkill
node: infra.containers
type: qa
---
## Q
When is Kubernetes over-engineering, and what do you run instead?

## A
K8s charges a **platform tax** — cluster upgrades, networking/ingress/observability stack, YAML sprawl, and in practice a platform team to own it. That tax is overkill when you have a handful of ordinary HTTP services, a small team, and no special scheduling needs.

- Instead: **managed container platforms** (Cloud Run, Fargate/ECS) give per-container deploys and autoscaling with no cluster to operate; a monolith on a PaaS stays viable longer than most teams admit.
- Adopt k8s when you're otherwise *building* its features — custom scheduling, service discovery, batch/GPU orchestration — or need its ecosystem (operators) across many teams.
