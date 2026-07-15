from __future__ import annotations

import json
from pathlib import Path

from pydantic import ValidationError

from release_passport.exceptions import ReleasePassportError
from release_passport.models import PassportDocument


def load_passport_fixture(fixtures_dir: Path) -> PassportDocument:
    path = fixtures_dir / "passport.json"
    try:
        return PassportDocument.model_validate(json.loads(path.read_text()))
    except FileNotFoundError as error:
        raise ReleasePassportError(f"fixture file not found: {path}") from error
    except ValidationError as error:
        raise ReleasePassportError(f"invalid fixture file: {path}: {error}") from error
