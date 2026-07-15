## Problem

ReleasePassport needed a repository baseline before any evidence capture or signing logic could be added safely.

## Approach

- initialized packaging, CI, contributor docs, and repository metadata
- added a typed Typer CLI entrypoint and smoke tests
- documented architecture, threat model, and deterministic canonicalization direction

## Important decisions

- kept the first slice focused on repository foundations rather than mixing setup with evidence logic
- started with a fixture-first architecture because deployment evidence should be testable offline
- kept the CLI surface intentionally small until the passport model lands

## Test evidence

- `uv sync --all-extras --dev`
- `uv run ruff format --check .`
- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`
- `uv run release-passport --help`

## Known limitations

- no passport capture or verification yet
- no signing or rendering yet

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Signature and evidence claims are justified

## Review findings

- no material findings after local self-review
