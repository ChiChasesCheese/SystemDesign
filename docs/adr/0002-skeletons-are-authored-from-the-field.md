# Skeletons are authored from the field, never derived from a codebase

A studied repository is the obvious place to get a skeleton from: its docs are
already organised, already ours, and already true. We do the opposite — the
`quant-infra` and `markets` skeletons are written from the field's canonical
sources first, and the codebase is mapped onto them afterwards.

The reason is what the mapping leaves behind. A skeleton derived from a
repository has exactly the shape of that repository, so the parts of the subject
the author never built and never wrote down are invisible in it — the blind spot
reproduces itself. Mapping onto an independently authored skeleton makes those
parts show up as leaves with nothing attached, and that list of empty leaves is
the most valuable thing the exercise produces: a syllabus for interviews and a
roadmap for the system. `trellis stats` already reports it, so the gap list
costs no new machinery.

**Consequences.** Authoring comes before ingesting, and it is the slow part —
due diligence on the field, then 120–140 nodes, before a single artefact is
triaged. The skeleton's correctness depends on the survey behind it rather than
on working code, so it is reviewed as an opinion about the subject, not as a
description of the repository.
