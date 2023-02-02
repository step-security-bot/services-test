import typer

from services_test import __version__
from services_test.lib import hello_world

APP_NAME = "services-test"
CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}

app = typer.Typer()

# https://typer.tiangolo.com/tutorial/options/version/
def version_callback(value: bool) -> None:
    if value:
        typer.echo(f"services-test, version {__version__}")
        raise typer.Exit()


@app.callback(context_settings=CONTEXT_SETTINGS)
def cli(
    version: bool = typer.Option(  # noqa: B008
        False,
        "-V",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show the version and exit.",
    )
) -> None:
    """
    services-test Command Line Interface.
    """


@app.command()
def hello(msg: str = typer.Argument(..., help="The message.")) -> None:  # noqa: B008
    """Hello world command."""
    typer.echo(hello_world(msg))
