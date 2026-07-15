## Problem

ReleasePassport had the lower-level `import` command, but it still lacked the operational `capture` command shape described in the tool’s intended workflow.

## Approach

- added a read-only `capture` command over the existing fixture-backed evidence path
- validated that the requested application name matches the captured passport
- reused the existing passport document output instead of creating a second capture schema

## Important decisions

- kept `capture` as an alias over the same fixture-backed model in this cycle instead of pretending live collection already exists
- used a distinct exit path when the requested application does not match the captured evidence
- preserved `import` for lower-level fixture workflows while exposing the higher-level operational command shape

## Test evidence

- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`
- `uv run release-passport capture payments-api --fixtures tests/fixtures/passport-import`

## Known limitations

- `capture` is still fixture-backed and not yet a live Argo CD collector
- no KMS-backed signing or capture adapter boundary yet in this slice

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Signature and evidence claims are justified

## Review findings

- no material findings after local self-review
