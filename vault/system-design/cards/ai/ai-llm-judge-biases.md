---
id: ai-llm-judge-biases
node: ai.evals
type: qa
---
## Q
Why use an LLM as the judge when scoring another LLM's outputs, and which systematic biases must the harness design around?

## A
Why: free-form text has no exact-match oracle, and human labeling doesn't scale to every CI run — a judge model scoring against a **rubric** is the workable middle ground.

Known biases to design around:
- **Position bias**: in pairwise comparisons, favors the first (or last) answer — so **swap order and score both ways**.
- **Verbosity bias**: longer answers score higher regardless of quality.
- **Self-preference**: rates output from its own model family higher — prefer a different-family judge.
- **Style-over-substance**: confident, well-formatted wrong answers beat hesitant right ones — rubrics must anchor on factual criteria.

Ground rule: **calibrate the judge against a human-labeled sample** before trusting it; an unvalidated judge is an unvalidated metric.
