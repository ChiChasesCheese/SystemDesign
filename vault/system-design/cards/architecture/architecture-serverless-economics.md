---
id: architecture-serverless-economics
node: architecture.serverless
type: qa
---
## Q
When does per-request (FaaS) pricing beat owning servers, and when does it flip?

## A
FaaS wins when utilization is **low or spiky**: you pay only for execution time, and idle costs zero — cron jobs, webhooks, rare admin endpoints, unpredictable bursts, and scale-to-zero for anything with dead hours. You're also buying off the ops bill (patching, capacity planning, autoscaling config).

It flips at **steady, high utilization**: per-invocation pricing carries a large premium over the same compute as reserved instances/containers — a server busy most of the day is several-fold cheaper than the equivalent Lambda-hours. High-throughput constant traffic on FaaS is the classic cost horror story.

Interview answer shape: "spiky or idle → serverless; flat and busy → provisioned; measure the crossover in $/vCPU-hour at your duty cycle."
