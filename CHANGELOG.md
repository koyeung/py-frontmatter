# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [0.5.0a5] - 2025-08-16
- fix trusted publishing

## [0.5.0a4] - 2025-08-16
### Changed
- migrate to [uv](https://docs.astral.sh/uv/)
  - use uv for check, test, build and publish
- perform more check by [ruff](https://github.com/astral-sh/ruff)
* revise pre-commit hooks
* cleanup unused hatch settings
* add justfile

## [0.5.0a3] - 2023-08-23
### Changed
* migrate from [poetry](https://python-poetry.org) and [tox](https://tox.wiki/) to [Hatch](https://hatch.pypa.io/latest/)
    * github workflow: replace `tox` by `hatch run`
* perform lint by [ruff](https://github.com/astral-sh/ruff)
* simplify checks in `.pre-commit-config.yaml`

## [0.5.0a2] - 2022-11-14
### Changed
* reduce rely on `pre-commit` in CI.

## [0.5.0a1] - 2022-11-13
### Changed
* not using `pre-commit.ci`

## [0.5.0a0] - 2022-11-13
### Changed
* revise readme

## [0.4.0] - 2022-11-13
### Changed
* use [pre-commit](https://pre-commit.com/)
* use [pre-commit.ci](https://pre-commit.ci)
* use [actions/cache](https://github.com/actions/cache)
* use [pypa/gh-action-pip-audit](https://github.com/pypa/gh-action-pip-audit)
* run lint checks from `pre-commit` in CI
* use [build](https://pypa-build.readthedocs.io/en/stable/) as PEP 517 build frontend
* run tests using `sdist` installed by `tox`
* add `poetry-audit` to `pre-commit` config
* add `tox-ini-fmt` to `pre-commit` config

## [0.3.0] - 2022-10-28
### Added
* add `add-item`, `remove-item` sub-commands
* add `add-tag`, `remove-tag` sub-commands

### Changed
* no return exit code from `main()`

## [0.2.0] - 2022-10-27
### Added
* add `get` and `set` sub-commands

### Changed
* revise github action workflow

## [0.1.0] - 2022-10-26
### Added
* functions to load/dump document file with front matter.
* initial project setup


[Unreleased]: https://github.com/koyeung/py-frontmatter/compare/main...HEAD
[0.5.0a3]: https://github.com/koyeung/py-frontmatter/releases/tag/0.5.0a3
[0.5.0a2]: https://github.com/koyeung/py-frontmatter/releases/tag/0.5.0a2
[0.5.0a1]: https://github.com/koyeung/py-frontmatter/releases/tag/0.5.0a1
[0.5.0a0]: https://github.com/koyeung/py-frontmatter/releases/tag/0.5.0a0
[0.4.0]: https://github.com/koyeung/py-frontmatter/releases/tag/0.4.0
[0.3.0]: https://github.com/koyeung/py-frontmatter/releases/tag/0.3.0
[0.2.0]: https://github.com/koyeung/py-frontmatter/releases/tag/0.2.0
[0.1.0]: https://github.com/koyeung/py-frontmatter/releases/tag/0.1.0
