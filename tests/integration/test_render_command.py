from pathlib import Path

from typer.testing import CliRunner

from release_passport.cli import app


def test_render_command_matches_expected_html_output() -> None:
    fixture_dir = Path("tests/fixtures/passport-render")
    expected = (fixture_dir / "expected.html").read_text().rstrip("\n")

    result = CliRunner().invoke(
        app,
        ["render", "tests/fixtures/passport-diff/new.json", "--format", "html"],
    )

    assert result.exit_code == 0
    assert result.stdout == expected + "\n"
