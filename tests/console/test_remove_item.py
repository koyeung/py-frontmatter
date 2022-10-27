import pytest

from .conftest import run_console_script


def test_remove_item(sample):
    exit_code = run_console_script(
        "frontmatter", "remove-item", "--jsonpath", "$.tags", "--item", "a", str(sample)
    )
    assert exit_code == 0

    assert (
        sample.read_text()
        == """\
---
title: Hacker's note
tags: [b]
---
# header
text
"""
    )


def test_remove__item_not_exists(sample):
    exit_code = run_console_script(
        "frontmatter", "remove-item", "--jsonpath", "$.tags", "--item", "c", str(sample)
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


def test_remove__jsonpath_not_exists(sample):
    with pytest.raises(RuntimeError) as exc:
        run_console_script(
            "frontmatter",
            "remove-item",
            "--jsonpath",
            "$.new_tags",
            "--item",
            "c",
            str(sample),
        )

    assert str(exc.value) == "unable to locate jsonpath='$.new_tags'"
