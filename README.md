# ReleasePassport

ReleasePassport captures deployment evidence into a deterministic artifact that can be reviewed, signed, and verified later.

## Current focus

- offline capture from sanitized deployment fixtures
- deterministic JSON evidence bundles
- explicit signature and verification boundaries

## Deliberate limits

- no secret storage
- no implicit signing
- no mutation of Argo CD or Kubernetes resources

## Running modes

- Offline: fixture-backed passport capture and verification
- Live: planned read-only adapters for Argo CD and repository metadata

## Safety

- read-only by default
- deterministic canonical content
- signatures handled separately from unsigned evidence

## Status

```bash
uv run release-passport capture payments-api --fixtures tests/fixtures/passport-import
uv run release-passport import tests/fixtures/passport-import
uv run release-passport diff tests/fixtures/passport-diff/old.json tests/fixtures/passport-diff/new.json
uv run release-passport verify tests/fixtures/passport-signing/signed-passport.json
uv run release-passport render tests/fixtures/passport-diff/new.json --format html
```

The current slice imports sanitized fixture evidence into a deterministic passport JSON document, compares two passport snapshots, verifies a locally signed passport artifact, and renders human-readable HTML or Markdown from the unsigned passport model.

The current signer is local and fixture-oriented. A KMS-backed signer is planned behind the same interface.
