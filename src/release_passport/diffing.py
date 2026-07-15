from __future__ import annotations

from pydantic import BaseModel

from release_passport.models import PassportDocument


class PassportDiff(BaseModel):
    previous_revision: str
    new_revision: str
    changed_resources_added: list[str]
    changed_resources_removed: list[str]
    images_added: list[str]
    images_removed: list[str]


def diff_passports(old: PassportDocument, new: PassportDocument) -> PassportDiff:
    old_resources = {f"{item.kind}:{item.namespace}/{item.name}" for item in old.changed_resources}
    new_resources = {f"{item.kind}:{item.namespace}/{item.name}" for item in new.changed_resources}
    old_images = {f"{item.name}@{item.digest}" for item in old.images}
    new_images = {f"{item.name}@{item.digest}" for item in new.images}

    return PassportDiff(
        previous_revision=old.new_revision,
        new_revision=new.new_revision,
        changed_resources_added=sorted(new_resources - old_resources),
        changed_resources_removed=sorted(old_resources - new_resources),
        images_added=sorted(new_images - old_images),
        images_removed=sorted(old_images - new_images),
    )
