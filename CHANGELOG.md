# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

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
[0.5.0a1]: https://github.com/koyeung/py-frontmatter/releases/tag/0.5.0a1
[0.5.0a0]: https://github.com/koyeung/py-frontmatter/releases/tag/0.5.0a0
[0.4.0]: https://github.com/koyeung/py-frontmatter/releases/tag/0.4.0
[0.3.0]: https://github.com/koyeung/py-frontmatter/releases/tag/0.3.0
[0.2.0]: https://github.com/koyeung/py-frontmatter/releases/tag/0.2.0
[0.1.0]: https://github.com/koyeung/py-frontmatter/releases/tag/0.1.0
