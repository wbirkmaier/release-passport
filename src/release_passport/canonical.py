from __future__ import annotations

import json

from release_passport.models import PassportDocument


def canonicalize_passport(passport: PassportDocument) -> str:
    return json.dumps(passport.model_dump(mode="json"), sort_keys=True, separators=(",", ":"))
