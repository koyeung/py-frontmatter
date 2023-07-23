# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
from .conftest import run_console_script


def test_get(sample, capsys):
    run_console_script("frontmatter", "get", str(sample))

    captured = capsys.readouterr()
    assert (
        captured.out
        == """\
{"title": "Hacker's note", "tags": ["a", "b"]}
"""
    )


def test_get__shell_quote(sample, capsys):
    run_console_script("frontmatter", "get", "--sq", str(sample))

    captured = capsys.readouterr()
    assert (
        captured.out
        == """\
'{"title": "Hacker'"'"'s note", "tags": ["a", "b"]}'
"""
    )
