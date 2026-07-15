from __future__ import annotations

from typing import Annotated

import typer

app = typer.Typer(
    help="Capture and verify deployment evidence without mutating release systems.",
    no_args_is_help=True,
    pretty_exceptions_enable=False,
)


@app.callback()
def callback() -> None:
    """ReleasePassport command group."""


@app.command("version")
def version() -> None:
    typer.echo("release-passport 0.1.0")


def main(argv: Annotated[list[str] | None, typer.Argument(hidden=True)] = None) -> None:
    app(args=argv)
