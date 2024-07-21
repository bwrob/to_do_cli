"""App instance for to_do.

Separate from __init__.py to avoid circular imports.
"""

import typer

app = typer.Typer()
state = {"verbose": False}
