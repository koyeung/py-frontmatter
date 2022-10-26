import re
from typing import TextIO, Tuple

from ruamel.yaml import YAML

from .document import Document

# regex pattern of document with yaml front matter
DOC_PATTERN = r"((?P<frontmatter>---\n(.*\n)?)---\n)?(?P<content>.*)"


def _parse_text(text: str, /) -> Tuple[str, str]:
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
    """
    match = re.match(pattern=DOC_PATTERN, string=text, flags=re.DOTALL | re.MULTILINE)

    if not match:
        raise Exception("Unable to parse input with/without yaml front matter")

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
