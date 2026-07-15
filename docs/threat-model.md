# Threat Model

## Assets

- deployment evidence metadata
- canonical unsigned content
- signatures and verification results

## Risks

- embedding secrets or private credentials in a passport
- signing nondeterministic content
- implying verification that did not actually occur

## Mitigations

- deterministic canonicalization before hashing
- explicit separation of unsigned evidence and signature records
- fixture-first tests for capture and verification paths
