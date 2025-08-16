# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0


def __getattr__(name: str) -> str:
    from importlib.metadata import version  # noqa: PLC0415

    if name == "__version__":
        return version("py_frontmatter")

    raise NameError(name)
