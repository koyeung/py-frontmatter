import logging
from dataclasses import dataclass

import jsonpath_ng
import ruamel.yaml.comments

LOGGER = logging.getLogger(__name__)


@dataclass
class Document:
    """Class for document."""

    meta: ruamel.yaml.comments.CommentedMap
    content: str | None


def add_item(*, document: Document, jsonpath: str, item: str) -> Document:
    jsonpath_expr = jsonpath_ng.parse(jsonpath)

    meta = document.meta
    matches = jsonpath_expr.find(meta)

    if not matches:
        LOGGER.debug(f"create new list in path {jsonpath=} with element {item=}")
        jsonpath_expr.update_or_create(meta, [item])
        return document

    if len(matches) > 1:  # pragma: no cover
        raise RuntimeError(f"support only single match of {jsonpath=}")

    found = matches[0]

    if item not in found.value:
        found.value.append(item)
    else:
        LOGGER.debug("item exists already; no need to update")

    return document


def remove_item(
    *,
    document: Document,
    jsonpath: str,
    item: str,
    raise_if_unknown_jsonpath: bool = True,
) -> Document:
    jsonpath_expr = jsonpath_ng.parse(jsonpath)

    meta = document.meta
    matches = jsonpath_expr.find(meta)

    if not matches:
        if raise_if_unknown_jsonpath:
            raise RuntimeError(f"unable to locate {jsonpath=}")

        LOGGER.debug(f"{jsonpath=} not exists; no action")
        return document

    if len(matches) > 1:  # pragma: no cover
        raise RuntimeError(f"support only single match of {jsonpath=}")

    found = matches[0]

    if item not in found.value:
        LOGGER.warning(f"item doesn't exists in list {jsonpath=}, no action")
        return document

    found.value.remove(item)
    return document
