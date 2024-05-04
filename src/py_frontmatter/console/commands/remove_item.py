# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
import argparse
import logging
from contextlib import closing

from py_frontmatter.core import load_document, remove_item

from .base_command import BaseCommand
from .utils import overwrite_file

LOGGER = logging.getLogger(__name__)


class RemoveItemCommand(BaseCommand):
    """Remove item from list in front matter."""

    name = "remove-item"
    description = "Remove item from a list"

    def register(self, subparsers) -> argparse.ArgumentParser:
        parser = super().register(subparsers)
        parser.add_argument(
            "file", type=argparse.FileType(mode="r+"), help="document file"
        )
        parser.add_argument(
            "--jsonpath", type=str, help="json path to the list", required=True
        )
        parser.add_argument(
            "--item", type=str, help="item to be removed", required=True
        )
        return parser

    def handle(self, args: argparse.Namespace):
        LOGGER.debug("args=%s", args)

        with closing(args.file):
            document = load_document(args.file)
            document = remove_item(
                document=document, jsonpath=args.jsonpath, item=args.item
            )
            overwrite_file(file=args.file, document=document)
