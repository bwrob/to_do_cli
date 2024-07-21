"""This module provides the RP To-Do database functionality."""

# rptodo/database.py

import configparser
from pathlib import Path

import to_do.impl.consts as c
from to_do.impl.return_codes import ReturnCode

DEFAULT_DB_FILE_PATH = Path.home().joinpath("." + Path.home().stem + "_todo.json")


def get_database_path(config_file: Path) -> Path:
    """Return the current path to the to-do database.

    Args:
        config_file: The path to the config file.
    """
    config = configparser.ConfigParser()
    _ = config.read(config_file)
    return Path(config[c.GENERAL][c.DATABASE])


def init_database(db_path: Path) -> ReturnCode:
    """Create the to-do database.

    Args:
        db_path: The path to the database file.
    """
    try:
        _ = db_path.write_text(data="[]")
        return ReturnCode.SUCCESS
    except OSError:
        return ReturnCode.DB_WRITE_ERROR
