from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from release_passport.canonical import canonicalize_passport
from release_passport.diffing import diff_passports
from release_passport.exceptions import ReleasePassportError
from release_passport.fixtures import load_passport_fixture
from release_passport.snapshot_io import load_passport

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


@app.command("diff")
def diff(
    old: Annotated[Path, typer.Argument(exists=True, readable=True, dir_okay=False)],
    new: Annotated[Path, typer.Argument(exists=True, readable=True, dir_okay=False)],
) -> None:
    try:
        report = diff_passports(load_passport(old), load_passport(new))
    except ReleasePassportError as error:
        raise typer.Exit(code=error.exit_code) from error

    typer.echo(report.model_dump_json(indent=2))


@app.command("canonicalize")
def canonicalize(
    passport_path: Annotated[Path, typer.Argument(exists=True, readable=True, dir_okay=False)],
) -> None:
    try:
        passport = load_passport(passport_path)
    except ReleasePassportError as error:
        raise typer.Exit(code=error.exit_code) from error

    typer.echo(canonicalize_passport(passport))


def main(argv: Annotated[list[str] | None, typer.Argument(hidden=True)] = None) -> None:
    app(args=argv)
