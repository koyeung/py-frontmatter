from dataclasses import dataclass

import ruamel.yaml.comments


@dataclass
class Document:
    """Class for document."""

    meta: ruamel.yaml.comments.CommentedMap
    content: str | None
