# Changelog

## Unreleased

- Established repository scaffolding, packaging, CI, and CLI baseline.
- Added fixture-backed deployment passport modeling and an offline `import` command.
- Added deterministic passport canonicalization and before/after diffing.
- Added local signing and verification for canonical passport content.
- Added Markdown and HTML rendering for human passport review.
- Added a signer adapter boundary for local and future KMS-backed signing.
- Added a read-only `capture` command shape over the existing fixture evidence path.
