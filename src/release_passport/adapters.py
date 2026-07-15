from __future__ import annotations

from dataclasses import dataclass

from release_passport.exceptions import ReleasePassportError
from release_passport.signing import SignatureRecord, sign_canonical_content


class SignerAdapter:
    def sign(self, canonical_content: str) -> SignatureRecord:
        raise NotImplementedError


@dataclass(frozen=True)
class LocalSignerAdapter(SignerAdapter):
    key_id: str = "fixture-key-1"
    secret: str = "fixture-secret"

    def sign(self, canonical_content: str) -> SignatureRecord:
        return sign_canonical_content(canonical_content, self.key_id, self.secret)


@dataclass(frozen=True)
class KmsSignerAdapter(SignerAdapter):
    key_id: str = "kms-key-future"

    def sign(self, canonical_content: str) -> SignatureRecord:
        raise ReleasePassportError(
            "AWS KMS signing is not implemented in this cycle; use the local signer adapter instead"
        )


def get_signer_adapter(mode: str) -> SignerAdapter:
    if mode == "local":
        return LocalSignerAdapter()
    if mode == "kms":
        return KmsSignerAdapter()
    raise ReleasePassportError(f"unsupported signer mode: {mode}")
