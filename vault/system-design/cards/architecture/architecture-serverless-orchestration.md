---
id: architecture-serverless-orchestration
node: architecture.serverless
type: qa
---
## Q
A workflow (order → charge → fulfill → notify) takes hours and must survive crashes, but FaaS functions cap at ~15 minutes and keep no state. What's the pattern?

## A
**Durable workflow orchestration** (Step Functions, Temporal, Durable Functions): the workflow's *state machine* lives in the orchestrator's durable store, and each step runs as a short, **idempotent** function invocation. The orchestrator persists progress after every step, so a crash resumes from the last completed step — never holding state in a long-running process.

This also gives you retries with backoff per step, timers ("wait 3 days"), and compensation hooks — effectively managed **saga** execution.

Contrast with **choreography** (functions chained via events): fine for 2–3 steps, but end-to-end state becomes invisible and error handling scatters — orchestrate once a human needs to answer "where is order 123 stuck?"
