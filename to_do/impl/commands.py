"""CLI commands."""

import rich

from to_do.impl.app import app

"""This module provides the RP To-Do CLI."""
# rptodo/cli.py

from pathlib import Path
from typing import Optional

import typer

from to_do.impl.config import init_app
from to_do.impl.database import DEFAULT_DB_FILE_PATH, init_database
from to_do.impl.return_codes import ERROR_MESSAGES

app = typer.Typer()

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
def add(task: str):
    """Add a task."""
    rich.print(f"Adding task: {task}")


@app.command()
def edit(task_id: int, task: str):
    """Edit a task."""
    rich.print(f"Editing task: {task_id} {task}")


@app.command()
def remove(task_id: int):
    """Remove a task."""
    rich.print(f"Removing task: {task_id}")


@app.command()
def list_tasks():
    """List all tasks."""
    rich.print("Listing all tasks")
