# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

from .conftest import run_console_script


def test_add_tag(sample: Path) -> None:
    run_console_script("frontmatter", "add-tag", "--tag", "c", str(sample))

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


def test_add_tag__tag_exists(sample: Path) -> None:
    run_console_script("frontmatter", "add-tag", "--tag", "b", str(sample))

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


def test_add_item__tags_not_exists(sample_wo_tags: Path) -> None:
    run_console_script("frontmatter", "add-tag", "--tag", "c", str(sample_wo_tags))

    assert (
        sample_wo_tags.read_text()
        == """\
---
title: Hacker's note
tags:
- c
---
# header
text
"""
    )
