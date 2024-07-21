"""Tests the CLI calls directly."""

from typer.testing import CliRunner

from to_do import __app_name__, __version__
from to_do.cli import cli

runner = CliRunner()


def test_version():
    result = runner.invoke(
        app=cli,
        args=["--version"],
    )
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout
