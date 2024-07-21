""" to_do entry point."""

# pyright: reportUnusedImport=false
import to_do.impl.callbacks
import to_do.impl.commands
from to_do.impl.app import app

cli = app


def cli_entry():
    cli(prog_name=__name__)


if __name__ == "__main__":
    cli_entry()
