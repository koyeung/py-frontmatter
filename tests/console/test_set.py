import io

from .conftest import run_console_script


def test_set(sample, monkeypatch):
    meta_json = """\
{"title": "Hacking is fun", "tags": ["b", "c"]}"""

    monkeypatch.setattr("sys.stdin", io.StringIO(meta_json))

    run_console_script("frontmatter", "set", str(sample))

    assert (
        sample.read_text()
        == """\
---
title: Hacking is fun
tags:
- b
- c
---
# header
text
"""
    )
