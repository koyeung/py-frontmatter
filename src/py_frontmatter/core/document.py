# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
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
        LOGGER.debug(
            "create new list in path jsonpath=%s with element item=%s", jsonpath, item
        )
        jsonpath_expr.update_or_create(meta, [item])
        return document

    if len(matches) > 1:  # pragma: no cover
        msg = f"support only single match of jsonpath={jsonpath!r}"
        raise RuntimeError(msg)

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
            msg = f"unable to locate jsonpath={jsonpath!r}"
            raise RuntimeError(msg)

        LOGGER.debug("jsonpath=%s not exists; no action", jsonpath)
        return document

    if len(matches) > 1:  # pragma: no cover
        msg = f"support only single match of jsonpath={jsonpath!r}"
        raise RuntimeError(msg)

    found = matches[0]

    if item not in found.value:
        LOGGER.warning("item doesn't exists in list jsonpath=%s, no action", jsonpath)
        return document

    found.value.remove(item)
    return document
