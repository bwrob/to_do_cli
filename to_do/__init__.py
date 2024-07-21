"""Top-level package for to_do."""

__app_description__ = (
    "Simple CLI to-do app to track tasks."
    "The program will allow you to add, edit, and remove tasks."
)
__app_name__ = "to_do"
__version__ = "0.1.0"
__author__ = "bwrob"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(7)

ERROR_MESSAGES = {
    DIR_ERROR: "Unable to read configuration file directory.",
    FILE_ERROR: "Unable to read configuration file.",
    DB_READ_ERROR: "Unable to read database.",
    DB_WRITE_ERROR: "Unable to write to database.",
    ID_ERROR: "Invalid to-do id.",
}
