FROM debian

ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y curl git bash
RUN curl https://pyenv.run | bash
COPY docker/.bashrc /root
RUN apt update && apt install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget llvm libncurses5-dev \
    libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
SHELL ["/bin/bash", "--login", "-c"]
RUN pyenv install 3.8.0
RUN pyenv install 3.7.5
WORKDIR /hypermodern-python-project
RUN pyenv local 3.8.0 3.7.5
RUN python --version
RUN python3.7 --version
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py |\
    POETRY_PREVIEW=1 python
RUN poetry init --no-interaction
RUN sed -i "/^python/s/3.8/3.7/" pyproject.toml
RUN poetry add click
RUN mkdir -p src/hypermodern_python_project
COPY src/hypermodern_python_project/__init__.py src/hypermodern_python_project/
COPY src/hypermodern_python_project/console.py src/hypermodern_python_project/
RUN echo "[tool.poetry.scripts]" >> pyproject.toml
RUN echo 'hypermodern-python-project = "hypermodern_python_project.console:main"' >> pyproject.toml
RUN poetry install
RUN poetry run hypermodern-python-project --version
RUN poetry add --dev pytest
RUN mkdir tests
RUN touch tests/__init__.py
COPY tests/test_console.py tests/
RUN poetry run pytest
COPY .coveragerc ./
RUN poetry add --dev pytest-cov
RUN pip install nox
COPY docker/noxfile.py ./
RUN nox
COPY .flake8 ./
COPY docker/noxfile-lint.py ./noxfile.py
RUN nox --session=lint
COPY docker/noxfile-black.py ./noxfile.py
RUN nox --session=lint
RUN nox --session=black
COPY docker/noxfile-pytype.py ./noxfile.py
RUN nox --session=pytype
