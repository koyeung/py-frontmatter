# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
import argparse
import logging
from contextlib import closing

from py_frontmatter.core import add_item, load_document

from .base_command import BaseCommand
from .utils import overwrite_file

LOGGER = logging.getLogger(__name__)


class AddItemCommand(BaseCommand):
    """Add item to list in front matter."""

    name = "add-item"
    description = "Add item to list"

    def register(self, subparsers) -> argparse.ArgumentParser:
        parser = super().register(subparsers)
        parser.add_argument(
            "file", type=argparse.FileType(mode="r+"), help="document file"
        )
        parser.add_argument(
            "--jsonpath", type=str, help="json path to the list", required=True
        )
        parser.add_argument("--item", type=str, help="item to be added", required=True)
        return parser

    def handle(self, args: argparse.Namespace) -> None:
        LOGGER.debug("args=%s", args)

        with closing(args.file):
            document = load_document(args.file)
            document = add_item(
                document=document, jsonpath=args.jsonpath, item=args.item
            )
            overwrite_file(file=args.file, document=document)
