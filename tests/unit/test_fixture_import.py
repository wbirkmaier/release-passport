from pathlib import Path

from release_passport.fixtures import load_passport_fixture


def test_load_passport_fixture_preserves_revisions_and_images() -> None:
    passport = load_passport_fixture(Path("tests/fixtures/passport-import"))

    assert passport.previous_revision == "d3adb33f"
    assert (
        passport.images[0].digest
        == "sha256:111122223333444455556666777788889999aaaabbbbccccddddeeeeffff0000"
    )
