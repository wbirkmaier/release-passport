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

Repository scaffolding and CLI baseline are in place. Evidence and signing slices land next.
