---
id: ai-prompt-regression-testing
node: ai.evals
type: qa
---
## Q
A teammate "just tweaks the prompt" in production config, and a provider model upgrade lands next month. What discipline prevents these from silently breaking your AI feature?

## A
Treat **prompt + model version + parameters as one deployable artifact**:

- Prompts live in **version control**, not a dashboard textbox; every change goes through the offline eval suite in CI like any code change.
- **Pin exact model versions** — a prompt is tuned against one model's behavior, and "same prompt, new model" is a breaking-change risk with no compile error.
- Provider **deprecations force migrations**, so re-running the full eval suite against the new model is the migration test plan.
- Edits fix the case in front of you and regress cases you're not looking at — only the suite catches the trade.
