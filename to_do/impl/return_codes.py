"""Return codes."""

from enum import IntEnum, auto

import typer


class ReturnCode(IntEnum):
    """Return codes for the To-Do CLI."""

    DB_READ_ERROR = auto()
    DB_WRITE_ERROR = auto()
    DIR_ERROR = auto()
    FILE_ERROR = auto()
    ID_ERROR = auto()
    JSON_ERROR = auto()
    SUCCESS = auto()

    @property
    def is_error(self) -> bool:
        """Check if the return code is an error."""
        return self != ReturnCode.SUCCESS

    @property
    def message(self) -> str:
        """Get the message for the return code."""
        return ERROR_MESSAGES[self]

    def report_if_error(
        self,
        pre_msg: str = "",
    ) -> None:
        """Report the return code if it is an error.

        Args:
            pre_msg: The message to print before the error message.
        """
        if self.is_error:
            typer.secho(
                message=(f"{pre_msg} \n {self.message}"),
                fg=typer.colors.RED,
            )
            raise typer.Exit(code=1)


ERROR_MESSAGES = {
    ReturnCode.DB_READ_ERROR: "Unable to read database.",
    ReturnCode.DB_WRITE_ERROR: "Unable to write to database.",
    ReturnCode.DIR_ERROR: "Unable to read configuration file directory.",
    ReturnCode.FILE_ERROR: "Unable to read configuration file.",
    ReturnCode.ID_ERROR: "Invalid to-do id.",
    ReturnCode.JSON_ERROR: "Unable to parse JSON.",
    ReturnCode.SUCCESS: "Success.",
}
