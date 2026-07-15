## Problem

ReleasePassport had a repository baseline but no working deployment evidence path.

## Approach

- added typed passport models for revisions, changed resources, images, and evidence source IDs
- implemented a fixture loader for an offline passport document
- exposed `release-passport import <fixture-dir>` with deterministic JSON output

## Important decisions

- kept the first slice import-only so the core passport document could be exercised before adding signing or verification complexity
- modeled evidence source IDs explicitly rather than burying provenance in freeform text
- kept the passport free of any secret-bearing fields

## Test evidence

- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`
- `uv run release-passport import tests/fixtures/passport-import`

## Known limitations

- no canonicalization, signing, verification, or rendered review output yet
- import is fixture-backed rather than capture-from-live-source in this slice

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Signature and evidence claims are justified

## Review findings

- no material findings after local self-review
