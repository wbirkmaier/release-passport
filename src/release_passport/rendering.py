from __future__ import annotations

from release_passport.exceptions import ReleasePassportError
from release_passport.models import PassportDocument


def render_passport(passport: PassportDocument, output_format: str) -> str:
    if output_format == "markdown":
        return _render_markdown(passport)
    if output_format == "html":
        return _render_html(passport)
    raise ReleasePassportError(f"unsupported render format: {output_format}")


def _render_markdown(passport: PassportDocument) -> str:
    lines = [
        f"# Release Passport: `{passport.application}`",
        "",
        f"Repository: `{passport.repository}`",
        f"Revision: `{passport.previous_revision}` -> `{passport.new_revision}`",
        f"Commit: `{passport.commit_sha}`",
        f"Health: `{passport.health_state}`",
        "",
        "## Changed Resources",
    ]
    lines.extend(
        f"- `{resource.kind}` `{resource.namespace}/{resource.name}`"
        for resource in passport.changed_resources
    )
    return "\n".join(lines)


def _render_html(passport: PassportDocument) -> str:
    resource_items = "".join(
        f"<li><code>{resource.kind}</code> <code>{resource.namespace}/{resource.name}</code></li>"
        for resource in passport.changed_resources
    )
    return "".join(
        [
            "<html><body>",
            f"<h1>Release Passport: <code>{passport.application}</code></h1>",
            f"<p>Repository: <code>{passport.repository}</code></p>",
            (
                f"<p>Revision: <code>{passport.previous_revision}</code> -&gt; "
                f"<code>{passport.new_revision}</code></p>"
            ),
            f"<p>Commit: <code>{passport.commit_sha}</code></p>",
            f"<p>Health: <code>{passport.health_state}</code></p>",
            f"<ul>{resource_items}</ul>",
            "</body></html>",
        ]
    )
