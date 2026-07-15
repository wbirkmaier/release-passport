from __future__ import annotations

from pathlib import Path

from pydantic import ValidationError

from release_passport.exceptions import ReleasePassportError
from release_passport.models import PassportDocument


def load_passport(path: Path) -> PassportDocument:
    try:
        return PassportDocument.model_validate_json(path.read_text())
    except FileNotFoundError as error:
        raise ReleasePassportError(f"passport file not found: {path}") from error
    except ValidationError as error:
        raise ReleasePassportError(f"invalid passport file: {path}: {error}") from error
