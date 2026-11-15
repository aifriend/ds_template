# Data Science Template

[![Tests](https://github.com/aifriend/ds_template/actions/workflows/tests.yml/badge.svg)][tests]
[![License](https://img.shields.io/github/license/aifriend/ds_template)][license]
[![Codecov](https://codecov.io/gh/aifriend/ds_template/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[tests]: https://github.com/aifriend/ds_template/actions/workflows/tests.yml
[codecov]: https://app.codecov.io/gh/aifriend/ds_template
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

This repository is a starting point for data science projects.
It gives you a standard folder layout, a Python package skeleton,
and the tooling for testing, linting and continuous integration,
so a new project does not start from an empty folder.

## What the template provides

- A Python package under `src/pdf2readable/` with separate modules for data, features, models and visualization.
  The package is named `pdf2readable` because the template was extracted from that project;
  rename it when you start your own project.
- Folders for `data/` (raw, interim, processed and external), `models/`, `notebooks/`, `references/` and `reports/`.
- A `Makefile` with common commands, and a `noxfile.py` for automated test sessions.
- Tests in `tests/`, run by GitHub Actions through `.github/workflows/tests.yml`.
- Pre-commit hooks, Black formatting and flake8 linting.
- Sphinx documentation in `docs/`, configured for Read the Docs.

## Requirements

- Python 3.10 or newer
- [Poetry] to install dependencies

## Using the template

1. Clone the repository, or create a new repository from it.
2. Install the dependencies with `make requirements`, which runs `poetry install`.
3. Rename the `pdf2readable` package, and update the name in `pyproject.toml` and in the `Makefile`.
4. Copy `.env.example` to `.env` and fill in your own values.

Other commands in the `Makefile`:

- `make test` runs the test suite.
- `make lint` checks `src` with flake8.
- `make data` builds the dataset from `data/raw` into `data/processed`.
- `make clean` deletes compiled Python files.
- `make help` lists all available commands.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Data Science Template_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@aifriend]'s [Aifriend Data Science] template.

[@aifriend]: https://github.com/aifriend
[poetry]: https://python-poetry.org/
[Data Science Template]: https://github.com/aifriend/ds_template
[file an issue]: https://github.com/aifriend/ds_template/issues

<!-- github-only -->

[license]: https://github.com/aifriend/ds_template/blob/main/LICENSE
[contributor guide]: https://github.com/aifriend/ds_template/blob/main/CONTRIBUTING.md
