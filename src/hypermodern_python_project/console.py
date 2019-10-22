import click

from . import __version__


@click.command()
@click.argument("name", default="world")
@click.option("--color/--no-color", default=True, help="Disable colors.")
@click.version_option(version=__version__)
def main(name, color):
    """The hypermodern Python script."""
    if color:
        click.secho(f"Hello {name}", fg="green")
    else:
        click.echo(f"Hello {name}")
