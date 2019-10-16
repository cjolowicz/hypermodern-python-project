import click.testing
import pytest

from hypermodern_python_project.__main__ import main


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_help_succeeds(runner):
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
