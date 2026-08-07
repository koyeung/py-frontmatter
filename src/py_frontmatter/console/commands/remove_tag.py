# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
import logging
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import argparse

from py_frontmatter.core import load_document, remove_item

from .base_command import BaseCommand
from .constants import TAG_JSONPATH
from .utils import overwrite_file

LOGGER = logging.getLogger(__name__)


class RemoveTagCommand(BaseCommand):
    """Remove tag in front matter."""

    name = "remove-tag"
    description = "Remove tag on document"

    def register(
        self, subparsers: argparse._SubParsersAction[argparse.ArgumentParser]
    ) -> argparse.ArgumentParser:
        parser = super().register(subparsers)
        parser.add_argument(
            "file",
            type=Path,
            help="document file",
        )
        parser.add_argument("--tag", type=str, help="tag to remove", required=True)
        return parser

    def handle(self, args: argparse.Namespace) -> None:
        LOGGER.debug("args=%s", args)

        with args.file.open(mode="r+") as f:
            document = load_document(f)
            document = remove_item(
                document=document,
                jsonpath=TAG_JSONPATH,
                item=args.tag,
                raise_if_unknown_jsonpath=False,
            )
            overwrite_file(file=f, document=document)
