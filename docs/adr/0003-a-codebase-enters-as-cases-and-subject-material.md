# A codebase enters as Cases on existing leaves, plus subject material in its own domains

Material harvested from a repository splits by a single question: is this a new
thing to know, or evidence for something we already track? Subject matter with
no home — quant data platforms, factor research, execution — becomes its own
domains (`quant-infra`, `markets`). Architecture decisions do not: a contract
saying research code may not import execution is an instance of `principles.coupling`,
so it attaches to that leaf as a **Case** rather than founding a parallel
"repository" domain where it would be reviewed separately from the principle it
demonstrates.

Cases are frozen at the commit they were read from and carry no staleness
checking. They record decisions and their reasoning, which stay interesting even
after the code moves on; judging whether one still reflects the system is the
reader's job, deliberately not the tool's. A Case is also never turned into a
card directly — a card that asks "what did we decide about X" tests recall of
our own conclusion and is worthless in an interview. Cards are written in the
lens's vocabulary as discrimination questions, with the Case as the evidence
behind them.

**Consequences.** Cases are stored per target domain, so a single codebase's
harvest scatters across domains; a generated `Codebases/<name>.md` index gives
the per-codebase view instead. Because cases are frozen, re-running triage after
the repository moves proposes only what changed and never rewrites what is
already accepted.
