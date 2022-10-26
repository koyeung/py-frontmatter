from typing import TextIO

from ruamel.yaml import YAML

from .document import Document


def dump_document(document: Document, /, fp: TextIO) -> None:
    """Dump document as stream with yaml front matter.

    :param document: document
    :param fp: output stream
    """
    yaml = YAML(typ="rt")

    fp.write("---\n")
    if document.meta:
        yaml.dump(document.meta, fp)
    fp.write("---\n")

    if document.content:
        fp.write(document.content)
