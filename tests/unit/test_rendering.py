from pathlib import Path

from release_passport.rendering import render_passport
from release_passport.snapshot_io import load_passport


def test_render_markdown_matches_expected_output() -> None:
    passport = load_passport(Path("tests/fixtures/passport-diff/new.json"))

    assert render_passport(passport, "markdown") == Path(
        "tests/fixtures/passport-render/expected.md"
    ).read_text().rstrip("\n")


def test_render_html_matches_expected_output() -> None:
    passport = load_passport(Path("tests/fixtures/passport-diff/new.json"))

    assert render_passport(passport, "html") == Path(
        "tests/fixtures/passport-render/expected.html"
    ).read_text().rstrip("\n")
