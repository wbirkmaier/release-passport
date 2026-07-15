## Problem

ReleasePassport could import fixture evidence, but it still lacked the deterministic canonical form needed for trustworthy signing and a useful diff for comparing two release passports.

## Approach

- added canonical JSON generation with sorted keys and stable separators
- added typed passport snapshot loading and a focused diff model
- exposed `release-passport diff` and `release-passport canonicalize`

## Important decisions

- canonicalized the full passport document before any signing work instead of inventing a partial hash input later
- kept the first diff focused on revisions, changed resources, and image digests because those are the most review-relevant release changes
- corrected the golden canonical output to match the actual lexical key ordering produced by the canonicalizer

## Test evidence

- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`
- `uv run release-passport diff tests/fixtures/passport-diff/old.json tests/fixtures/passport-diff/new.json`
- `uv run release-passport canonicalize tests/fixtures/passport-diff/new.json`

## Known limitations

- no signing or verification yet
- diff output is intentionally targeted, not a generic recursive object diff

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Signature and evidence claims are justified

## Review findings

- fixed the expected canonical JSON ordering during review after validating the canonicalizer output
