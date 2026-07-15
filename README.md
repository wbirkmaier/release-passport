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
uv run release-passport import tests/fixtures/passport-import
uv run release-passport diff tests/fixtures/passport-diff/old.json tests/fixtures/passport-diff/new.json
```

The current slice imports sanitized fixture evidence into a deterministic passport JSON document and compares two passport snapshots. Capture, signing, verification, and rendering land in later slices.
