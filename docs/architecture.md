# Architecture

ReleasePassport separates evidence capture, canonicalization, signing, verification, and rendering.

## Planned flow

1. Adapters load deployment evidence from fixtures or live sources.
2. Normalizers convert evidence into a typed passport document.
3. Canonicalization produces deterministic unsigned content.
4. Signers and verifiers operate on canonical bytes.
5. Renderers emit JSON, Markdown, and HTML summaries.

The current shipped signer is local and deterministic, with a dedicated adapter boundary so KMS-backed signing can be added later without changing canonicalization or verification flows.
