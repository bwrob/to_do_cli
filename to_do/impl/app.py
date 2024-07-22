"""App instance for to_do.

Separate from __init__.py to avoid circular imports.
"""

import typer
import logging
from to_do import __app_name__

# Gather singleton objects here to avoid circular imports.
app = typer.Typer()
state = {"verbose": False}
logger = logging.getLogger(name=__app_name__)
