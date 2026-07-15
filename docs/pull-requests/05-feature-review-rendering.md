## Problem

ReleasePassport had deterministic JSON and verification output, but no human-readable review format for deployment evidence.

## Approach

- added Markdown and HTML rendering from the unsigned passport model
- exposed `release-passport render <passport.json> --format markdown|html`
- kept rendered review output separate from the signed envelope path

## Important decisions

- rendered from the unsigned passport model instead of the signed envelope so presentation stays separate from signature validation
- kept HTML deliberately simple and dependency-free rather than adding a templating stack this early
- used golden-file tests for both Markdown and HTML to keep review output stable

## Test evidence

- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`
- `uv run release-passport render tests/fixtures/passport-diff/new.json --format html`

## Known limitations

- rendering is intentionally compact and does not yet include signature metadata or expanded evidence timelines
- only Markdown and HTML are supported in this slice

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Signature and evidence claims are justified

## Review findings

- replaced a brittle tuple-style HTML string construction with an explicit `"".join(...)` form during review to keep the renderer syntax-safe and formatter-friendly
