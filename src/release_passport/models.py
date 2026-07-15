from __future__ import annotations

from pydantic import BaseModel, Field


class ChangedResource(BaseModel):
    kind: str
    namespace: str
    name: str


class ContainerImage(BaseModel):
    name: str
    digest: str


class PassportDocument(BaseModel):
    application: str
    repository: str
    previous_revision: str
    new_revision: str
    commit_sha: str
    manifest_checksum: str
    sync_initiator: str
    sync_result: str
    health_state: str
    deployment_timestamp: str
    approval_reference: str | None = None
    rollback_target: str | None = None
    changed_resources: list[ChangedResource] = Field(default_factory=list)
    images: list[ContainerImage] = Field(default_factory=list)
    evidence_source_ids: list[str] = Field(default_factory=list)
