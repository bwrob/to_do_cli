"""This module provides the RP To-Do config functionality."""

import configparser
from pathlib import Path

import typer

import to_do.impl.consts as c
from to_do import __app_name__
from to_do.impl.return_codes import ReturnCode

CONFIG_FILE = "config.ini"

CONFIG_DIR_PATH = Path(typer.get_app_dir(app_name=__app_name__))
CONFIG_FILE_PATH = CONFIG_DIR_PATH / CONFIG_FILE


def init_app(db_path: Path) -> ReturnCode:
    """Initialize the application config.

    Sets the database path in the config file.

    Args:
        db_path: The path to the database file.
    """
    config_code = __check_config_path()

    if config_code.is_error:
        return config_code

    database_code = __set_database_path(db_path)
    if database_code.is_error:
        return database_code

    return ReturnCode.SUCCESS


def __check_config_path() -> ReturnCode:
    """Check if the config folder and file exist."""
    try:
        CONFIG_DIR_PATH.mkdir(exist_ok=True)
    except OSError:
        return ReturnCode.DIR_ERROR

    try:
        CONFIG_FILE_PATH.touch(exist_ok=True)
    except OSError:
        return ReturnCode.FILE_ERROR

    return ReturnCode.SUCCESS


def __set_database_path(db_path: Path) -> ReturnCode:
    """Create the database.

    Args:
        db_path: The path to the database file.
    """
    config = configparser.ConfigParser()
    config[c.GENERAL] = {c.DATABASE: str(db_path)}
    try:
        with CONFIG_FILE_PATH.open("w") as file:
            config.write(file)
    except OSError:
        return ReturnCode.DB_WRITE_ERROR
    return ReturnCode.SUCCESS
