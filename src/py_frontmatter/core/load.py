# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
import re
from typing import TextIO

from ruamel.yaml import YAML

from .document import Document

# regex pattern of document with yaml front matter
DOC_PATTERN = r"((?P<frontmatter>---\n(.+?\n)?)---\n)?(?P<content>.*)"


def _parse_text(text: str, /) -> tuple[str, str]:
    r"""Extract yaml front matter string and content.

    >>> text = 'hello world!'
    >>> _parse_text(text)
    (None, 'hello world!')

    >>> text = '''\
    ... ---
    ... ---
    ... hello world!'''
    >>> _parse_text(text)
    ('---\n', 'hello world!')

    >>> text = '''\
    ... ---
    ... tags: ["a", "b"]
    ... ---
    ... hello world!'''
    >>> _parse_text(text)
    ('---\ntags: ["a", "b"]\n', 'hello world!')

    Only extract front matter (first yaml document)
    >>> text = '''\
    ... ---
    ... tags: ["a", "b"]
    ... ---
    ... content
    ... ---
    ... hello world!'''
    >>> _parse_text(text)
    ('---\ntags: ["a", "b"]\n', 'content\n---\nhello world!')
    """
    match = re.match(pattern=DOC_PATTERN, string=text, flags=re.DOTALL | re.MULTILINE)

    if not match:
        msg = "Unable to parse input with/without yaml front matter"
        raise RuntimeError(msg)

    matched_groups = match.groupdict()
    return matched_groups["frontmatter"], matched_groups["content"]


def load_document(fp: TextIO, /) -> Document:
    """Load document from stream, optionally with yaml front matter.

    :param fp: output stream
    :return: document object.
    """
    text = fp.read()
    frontmatter, content = _parse_text(text)

    if frontmatter is not None:
        yaml = YAML(typ="rt")
        meta = yaml.load(frontmatter)
    else:
        meta = {}

    return Document(meta=meta, content=content)
