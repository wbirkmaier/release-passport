import json
from pathlib import Path

from typer.testing import CliRunner

from release_passport.cli import app


def test_import_command_matches_expected_output() -> None:
    fixture_dir = Path("tests/fixtures/passport-import")
    expected = json.loads((fixture_dir / "expected-passport.json").read_text())

    result = CliRunner().invoke(app, ["import", str(fixture_dir)])

    assert result.exit_code == 0
    assert json.loads(result.stdout) == expected


def test_capture_command_matches_expected_output() -> None:
    fixture_dir = Path("tests/fixtures/passport-import")
    expected = json.loads((fixture_dir / "expected-passport.json").read_text())

    result = CliRunner().invoke(
        app,
        ["capture", "payments-api", "--fixtures", str(fixture_dir)],
    )

    assert result.exit_code == 0
    assert json.loads(result.stdout) == expected
