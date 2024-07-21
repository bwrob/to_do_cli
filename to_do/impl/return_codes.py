"""Return codes."""

from enum import IntEnum, auto


class ReturnCode(IntEnum):
    """Return codes."""

    SUCCESS = auto()
    DIR_ERROR = auto()
    FILE_ERROR = auto()
    DB_READ_ERROR = auto()
    DB_WRITE_ERROR = auto()
    JSON_ERROR = auto()
    ID_ERROR = auto()


ERROR_MESSAGES = {
    ReturnCode.DIR_ERROR: "Unable to read configuration file directory.",
    ReturnCode.FILE_ERROR: "Unable to read configuration file.",
    ReturnCode.DB_READ_ERROR: "Unable to read database.",
    ReturnCode.DB_WRITE_ERROR: "Unable to write to database.",
    ReturnCode.ID_ERROR: "Invalid to-do id.",
}
