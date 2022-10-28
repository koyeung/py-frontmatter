from .conftest import run_console_script


def test_add_tag(sample):
    exit_code = run_console_script("frontmatter", "add-tag", "--tag", "c", str(sample))
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


def test_add_tag__tag_exists(sample):
    exit_code = run_console_script("frontmatter", "add-tag", "--tag", "b", str(sample))
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


def test_add_item__tags_not_exists(sample_wo_tags):
    exit_code = run_console_script(
        "frontmatter", "add-tag", "--tag", "c", str(sample_wo_tags)
    )
    assert exit_code == 0

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
