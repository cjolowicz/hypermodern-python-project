import nox


@nox.session(python=["3.8", "3.7"])
def lint(session):
    """Lint using flake8."""
    session.install("flake8", "flake8-bugbear")
    session.run("flake8", "src", "tests", "noxfile.py")


@nox.session(python=["3.8", "3.7"])
def tests(session):
    """Run the test suite."""
    env = {"VIRTUAL_ENV": session.virtualenv.location}
    session.run("poetry", "install", external=True, env=env)
    session.run("pytest", "--cov", *session.posargs)
