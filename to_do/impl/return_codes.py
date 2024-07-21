"""Return codes."""

from enum import IntEnum, auto

import typer


class ReturnCode(IntEnum):
    """Return codes."""

    SUCCESS = auto()
    DIR_ERROR = auto()
    FILE_ERROR = auto()
    DB_READ_ERROR = auto()
    DB_WRITE_ERROR = auto()
    JSON_ERROR = auto()
    ID_ERROR = auto()

    @property
    def is_error(self) -> bool:
        return self != ReturnCode.SUCCESS

    @property
    def message(self) -> str:
        return ERROR_MESSAGES[self]

    def report_if_error(
        self,
        pre_msg: str = "",
    ) -> None:
        if self.is_error:
            typer.secho(
                message=(f"{pre_msg} \n {self.message}"),
                fg=typer.colors.RED,
            )
            raise typer.Exit(code=1)


ERROR_MESSAGES = {
    ReturnCode.DIR_ERROR: "Unable to read configuration file directory.",
    ReturnCode.FILE_ERROR: "Unable to read configuration file.",
    ReturnCode.DB_READ_ERROR: "Unable to read database.",
    ReturnCode.DB_WRITE_ERROR: "Unable to write to database.",
    ReturnCode.ID_ERROR: "Invalid to-do id.",
}
