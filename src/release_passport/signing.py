from __future__ import annotations

import hashlib

from pydantic import BaseModel


class SignatureRecord(BaseModel):
    key_id: str
    algorithm: str
    signature: str


class SignedPassport(BaseModel):
    passport: dict[str, object]
    signature: SignatureRecord


class VerificationResult(BaseModel):
    key_id: str
    algorithm: str
    verified: bool


def sign_canonical_content(canonical_content: str, key_id: str, secret: str) -> SignatureRecord:
    digest = hashlib.sha256(f"{key_id}:{secret}:{canonical_content}".encode()).hexdigest()
    return SignatureRecord(key_id=key_id, algorithm="sha256-fixture", signature=digest)


def verify_canonical_content(
    canonical_content: str,
    signature: SignatureRecord,
    secret: str,
) -> VerificationResult:
    expected = sign_canonical_content(canonical_content, signature.key_id, secret)
    return VerificationResult(
        key_id=signature.key_id,
        algorithm=signature.algorithm,
        verified=expected.signature == signature.signature,
    )
