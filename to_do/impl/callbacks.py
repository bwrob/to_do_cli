"""Defines callbacks."""

from typing import Optional

import typer

from to_do import __app_name__, __version__
from to_do.impl.app import app, state


def __version_callback(value: bool):
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


def __verbose_callback(value: bool) -> None:
    state["verbose"] = value


# pyright: reportAny=false
VERSION_CALLBACK = typer.Option(
    None,
    "--version",
    "-v",
    help="Show the application's version.",
    callback=__version_callback,
    is_eager=True,
)

VERBOSE_CALLBACK = typer.Option(
    None,
    "--verbose",
    "-vb",
    help="Show the application's version.",
    callback=__verbose_callback,
    is_eager=True,
)


# pyright: reportDeprecated=false
@app.callback()
def main(
    version: Optional[bool] = VERBOSE_CALLBACK,
    verbose: Optional[bool] = VERSION_CALLBACK,
) -> None:
    return
