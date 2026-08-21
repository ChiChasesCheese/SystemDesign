"""Cases: a decision taken from a codebase, rewritten in a lens's vocabulary.

A case is evidence, not knowledge: it attaches to a leaf that already exists
because the decision it records is an instance of that leaf's principle. It is
frozen at the commit it was read from — the reasoning stays interesting after
the code moves on, and judging whether it still reflects the system is the
reader's job, deliberately not the tool's.

Cases are reading-shaped, so everything that already understands a reading
(map notes, the go-deeper footer) understands a case, with provenance carried
in extra frontmatter:

    ---
    nodes: [principles.coupling]
    title: Research code may not import execution
    codebase: quant-stroller
    ref: 8f2c1ab
    artefact: contract:"alpha must not import execution"
    ---
"""

from __future__ import annotations

from pathlib import Path

import yaml

from .readings import Reading, ReadingError, load_readings, parse_reading

CASES_DIRNAME = "cases"
CASE_KEYS = frozenset({"codebase", "ref", "artefact"})


class CaseError(ValueError):
    """Raised for a case file that violates the format."""


def parse_case(path: str | Path) -> Reading:
    try:
        case = parse_reading(path, CASE_KEYS)
    except ReadingError as exc:
        raise CaseError(str(exc)) from None
    for key in ("codebase", "ref", "artefact"):
        if not str(case.extra.get(key, "")).strip():
            raise CaseError(f"{path}: case is missing '{key}' — a case must say "
                            "which codebase, at which commit, and from what")
    return case


def load_cases(cases_dir: str | Path) -> tuple[list[Reading], list[str]]:
    cases, errors = load_readings(cases_dir, CASE_KEYS)
    kept, extra_errors = [], []
    for case in cases:
        try:
            kept.append(parse_case(case.path))
        except CaseError as exc:
            extra_errors.append(str(exc))
    return kept, errors + extra_errors


def write_case(
    cases_dir: str | Path,
    slug: str,
    *,
    title: str,
    nodes: list[str],
    codebase: str,
    ref: str,
    artefact: str,
    body: str,
) -> Path:
    directory = Path(cases_dir)
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{slug}.md"
    front = yaml.safe_dump(
        {"nodes": nodes, "title": title, "codebase": codebase,
         "ref": ref, "artefact": artefact},
        allow_unicode=True, sort_keys=False,
    )
    path.write_text(f"---\n{front}---\n\n# {title}\n\n{body.strip()}\n", encoding="utf-8")
    return path
