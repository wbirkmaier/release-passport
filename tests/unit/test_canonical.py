from pathlib import Path

from release_passport.canonical import canonicalize_passport
from release_passport.snapshot_io import load_passport


def test_canonicalize_passport_matches_expected_output() -> None:
    passport = load_passport(Path("tests/fixtures/passport-diff/new.json"))

    assert canonicalize_passport(passport) == Path(
        "tests/fixtures/passport-diff/expected-canonical.json"
    ).read_text().rstrip("\n")
