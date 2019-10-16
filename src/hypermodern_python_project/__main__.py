import click

from hypermodern_python_project import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """The hypermodern Python script."""
