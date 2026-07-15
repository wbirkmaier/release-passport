from pathlib import Path

from release_passport.adapters import KmsSignerAdapter, LocalSignerAdapter
from release_passport.canonical import canonicalize_passport
from release_passport.exceptions import ReleasePassportError
from release_passport.signing import sign_canonical_content, verify_canonical_content
from release_passport.snapshot_io import load_passport


def test_sign_and_verify_canonical_content() -> None:
    canonical = canonicalize_passport(load_passport(Path("tests/fixtures/passport-diff/new.json")))

    signature = sign_canonical_content(canonical, key_id="fixture-key-1", secret="fixture-secret")
    result = verify_canonical_content(canonical, signature, secret="fixture-secret")

    assert result.verified is True


def test_local_signer_adapter_signs_canonical_content() -> None:
    canonical = canonicalize_passport(load_passport(Path("tests/fixtures/passport-diff/new.json")))

    assert LocalSignerAdapter().sign(canonical).key_id == "fixture-key-1"


def test_kms_signer_adapter_reports_not_implemented() -> None:
    try:
        KmsSignerAdapter().sign("{}")
    except ReleasePassportError as error:
        assert "AWS KMS signing is not implemented" in str(error)
    else:
        raise AssertionError("expected ReleasePassportError")
