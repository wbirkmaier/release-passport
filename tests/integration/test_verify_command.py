import json
from pathlib import Path

from typer.testing import CliRunner

from release_passport.cli import app


def test_verify_command_matches_expected_output() -> None:
    fixture_dir = Path("tests/fixtures/passport-signing")
    expected = json.loads((fixture_dir / "expected-verification.json").read_text())

    result = CliRunner().invoke(app, ["verify", str(fixture_dir / "signed-passport.json")])

    assert result.exit_code == 0
    assert json.loads(result.stdout) == expected
