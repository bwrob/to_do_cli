"""CLI commands."""

import rich

from to_do.impl.app import app


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
