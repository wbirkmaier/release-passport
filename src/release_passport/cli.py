from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from release_passport.exceptions import ReleasePassportError
from release_passport.fixtures import load_passport_fixture

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


@app.command("import")
def import_fixture(
    fixtures: Annotated[
        Path,
        typer.Argument(exists=True, readable=True, file_okay=False, dir_okay=True),
    ],
) -> None:
    try:
        passport = load_passport_fixture(fixtures)
    except ReleasePassportError as error:
        raise typer.Exit(code=error.exit_code) from error

    typer.echo(passport.model_dump_json(indent=2))


def main(argv: Annotated[list[str] | None, typer.Argument(hidden=True)] = None) -> None:
    app(args=argv)
