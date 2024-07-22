"""CLI commands."""

from pathlib import Path
from typing import Optional

import typer

from to_do.impl.app import app
from to_do.impl.config import init_app
from to_do.impl.database import DEFAULT_DB_FILE_PATH, init_database

# pyright: reportAny=false
DB_PATH_INPUT = typer.Option(
    str(DEFAULT_DB_FILE_PATH),
    "--db-path",
    "-db",
    prompt="to-do database location?",
)


@app.command()
def init(
    db_path: str = DB_PATH_INPUT,
) -> None:
    """Initialize the to-do database.

    Args:
        db_path: The path to the database file.
    """
    app_init_error = init_app(Path(db_path))
    app_init_error.report_if_error(pre_msg="Creating config file failed with:")

    db_init_error = init_database(Path(db_path))
    db_init_error.report_if_error(pre_msg="Creating database failed with:")

    typer.secho(f"The to-do database is {db_path}", fg=typer.colors.GREEN)


@app.command()
def list_tasks() -> None:
    """List all tasks."""
    print("Listing all tasks")
