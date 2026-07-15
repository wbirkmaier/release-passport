## Problem

Canonical content existed, but there was still no way to attach a deterministic local signature or verify a signed passport artifact offline.

## Approach

- added a local fixture signing model over canonical passport content
- added explicit signed-passport and verification result models
- exposed `release-passport verify <signed-passport.json>`

## Important decisions

- kept the signing path local and deterministic for this slice instead of pretending to support KMS or hardware-backed keys already
- verified the embedded unsigned passport payload directly rather than routing the signed envelope through the unsigned snapshot loader
- corrected the fixture signature value to match the actual canonical content and test secret after validation exposed the mismatch

## Test evidence

- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`
- `uv run release-passport verify tests/fixtures/passport-signing/signed-passport.json`

## Known limitations

- signing is fixture-local and not a real cryptographic key-management integration yet
- no HTML or Markdown review rendering yet

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Signature and evidence claims are justified

## Review findings

- fixed the verification path to canonicalize the embedded unsigned passport content rather than misloading the signed envelope as an unsigned passport
- updated the fixture signature to match the real canonical content and deterministic test secret
