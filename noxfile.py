import nox  # pytype: disable=import-error


nox.options.sessions = "lint", "pytype", "tests"
locations = "src", "tests", "noxfile.py"


@nox.session(python="3.8")
def black(session):
    """Run black code formatter."""
    session.install("black")
    session.run("black", *locations)


@nox.session(python="3.7")
def lint(session):
    """Lint using flake8."""
    session.install("flake8", "flake8-bugbear", "flake8-import-order", "flake8-black")
    session.run("flake8", *locations)


@nox.session(python="3.7")
def pytype(session):
    """Run the static type checker."""
    session.install("pytype")
    session.run("pytype", *locations)


@nox.session(python=["3.8", "3.7"])
def tests(session):
    """Run the test suite."""
    env = {"VIRTUAL_ENV": session.virtualenv.location}
    session.run("poetry", "install", external=True, env=env)
    session.run("pytest", "--cov", *session.posargs)


@nox.session(python="3.7")
def coverage(session):
    """Upload coverage data."""
    session.install("coverage", "codecov")
    session.run("coverage", "xml")
    session.run("codecov", *session.posargs)
