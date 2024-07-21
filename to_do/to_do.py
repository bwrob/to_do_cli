"""
TO_DO CLI PROGRAM

This is a simple program to track tasks. The program will allow you to add, edit,
and remove tasks.
"""

import rich
import typer

cli = typer.Typer()


@cli.command()
def add(task: str):
    """Add a task."""
    rich.print(f"Adding task: {task}")


@cli.command()
def edit(task_id: int, task: str):
    """Edit a task."""
    rich.print(f"Editing task: {task_id} {task}")


@cli.command()
def remove(task_id: int):
    """Remove a task."""
    rich.print(f"Removing task: {task_id}")


@cli.command()
def list_tasks():
    """List all tasks."""
    rich.print("Listing all tasks")


if __name__ == "__main__":
    cli()
