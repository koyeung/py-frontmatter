from .conftest import run_console_script


def test_add_item(sample):
    exit_code = run_console_script(
        "frontmatter", "add-item", "--jsonpath", "$.tags", "--item", "c", str(sample)
    )
    assert exit_code == 0

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
    exit_code = run_console_script(
        "frontmatter", "add-item", "--jsonpath", "$.tags", "--item", "b", str(sample)
    )
    assert exit_code == 0

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
    exit_code = run_console_script(
        "frontmatter",
        "add-item",
        "--jsonpath",
        "$.new_tags",
        "--item",
        "c",
        str(sample),
    )
    assert exit_code == 0

    assert (
        sample.read_text()
        == """\
---
title: Hacker's note
tags:
- a
- b
new_tags:
- c
---
# header
text
"""
    )
