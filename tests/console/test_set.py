# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
import io
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

    import pytest

from .conftest import run_console_script


def test_set(sample: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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
