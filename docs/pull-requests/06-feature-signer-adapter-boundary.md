## Problem

ReleasePassport's local signing path worked, but it still coupled the CLI directly to one signing implementation, which would make later KMS support more invasive.

## Approach

- added a signer adapter interface
- implemented a shipped local signer adapter
- added an explicit placeholder KMS signer adapter that fails clearly rather than pretending live signing works

## Important decisions

- kept the adapter boundary narrow with one `sign()` method returning the existing signature model
- left verification and canonicalization untouched so future signers can reuse the same deterministic content path
- made the KMS adapter deliberately explicit about being unimplemented in this cycle

## Test evidence

- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`

## Known limitations

- KMS-backed signing is not implemented yet
- the CLI still uses the existing local verification secret path in this cycle

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Signature and evidence claims are justified

## Review findings

- no material findings after local self-review
