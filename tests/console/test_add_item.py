# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
from .conftest import run_console_script


def test_add_item(sample):
    run_console_script(
        "frontmatter", "add-item", "--jsonpath", "$.tags", "--item", "c", str(sample)
    )

    assert (
        sample.read_text()
        == """\
---
title: Hacker's note
tags: [a, b, c]
---
# header
text
"""
    )


def test_add_item__item_exists(sample):
    run_console_script(
        "frontmatter", "add-item", "--jsonpath", "$.tags", "--item", "b", str(sample)
    )

    assert (
        sample.read_text()
        == """\
---
title: Hacker's note
tags: [a, b]
---
# header
text
"""
    )


def test_add_item__jsonpath_not_exists(sample):
    run_console_script(
        "frontmatter",
        "add-item",
        "--jsonpath",
        "$.new_tags",
        "--item",
        "c",
        str(sample),
    )

    assert (
        sample.read_text()
        == """\
---
title: Hacker's note
tags: [a, b]
new_tags:
- c
---
# header
text
"""
    )
