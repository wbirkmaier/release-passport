from pathlib import Path

from release_passport.diffing import diff_passports
from release_passport.snapshot_io import load_passport


def test_diff_passports_reports_changed_resources_and_images() -> None:
    old = load_passport(Path("tests/fixtures/passport-diff/old.json"))
    new = load_passport(Path("tests/fixtures/passport-diff/new.json"))

    diff = diff_passports(old, new)

    assert diff.changed_resources_added == ["Deployment:payments/api"]
    assert diff.images_added == [
        "ghcr.io/example/payments-api@sha256:22223333444455556666777788889999aaaabbbbccccddddeeeeffff00001111"
    ]
