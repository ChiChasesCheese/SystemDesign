---
id: ai-eval-set-vs-ab
node: ai.evals
type: qa
---
## Q
For an LLM feature, what plays the role of unit tests vs canary/A-B — and why can't "I tried five prompts and it looked good" replace either?

## A
- **Offline eval set** = the unit/regression suite: a versioned dataset of real inputs with expected outputs or scoring rubrics, run automatically on every prompt/model/pipeline change. Cheap, reproducible, **gates deploy**.
- **Online A/B** = the canary: real traffic, real outcome metrics (task completion, thumbs, escalation rate). Catches distribution drift and UX effects offline sets can't, but is slow, noisy, and burns users on bad variants.

Manual spot-checks fail because outputs are **nondeterministic and high-variance**: five samples can't distinguish a 2% from a 10% failure rate, so eval sets need hundreds of cases and **score thresholds, not exact-match assertions**.
