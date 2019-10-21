import click.testing
import pytest  # pytype: disable=import-error

from hypermodern_python_project import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_help_succeeds(runner):
    result = runner.invoke(console.main, ["--help"])
    assert result.exit_code == 0
