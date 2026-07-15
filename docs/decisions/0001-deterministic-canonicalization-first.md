# ADR 0001: Start With Deterministic Canonicalization

## Status

Accepted

## Context

Signing only has value if the unsigned content is stable and reproducible across environments.

## Decision

Start with deterministic passport content and fixture-backed evidence before adding signer integrations.

## Consequences

- signing and verification behavior become testable offline
- later adapter additions can reuse the same canonical content path
