# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
import io

import pytest

from py_frontmatter.core.dump import dump_document
from py_frontmatter.core.load import load_document


@pytest.mark.parametrize(
    "text",
    [
        """\
---
# some comment
tags: [a, b]
---
hello world!""",
        """\
---
---
hello world!""",
        """\
---
# some comment
tags: [a, b]
---
""",
    ],
)
def test_round_trip__same_input_output(text):
    with io.StringIO(text) as buffer:
        document = load_document(buffer)

    with io.StringIO() as buffer:
        dump_document(document, buffer)

        result = buffer.getvalue()
        assert result == text


def test_round_trip__no_frontmatter_input():
    text = """\
hello world!"""

    with io.StringIO(text) as buffer:
        document = load_document(buffer)

    assert document.content == "hello world!"
    assert not document.meta

    with io.StringIO() as buffer:
        dump_document(document, buffer)

        result = buffer.getvalue()
        assert (
            result
            == """\
---
---
hello world!"""
        )
