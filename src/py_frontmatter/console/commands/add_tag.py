# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
import argparse
import logging
from contextlib import closing

from py_frontmatter.core import add_item, load_document

from .base_command import BaseCommand
from .constants import TAG_JSONPATH
from .utils import overwrite_file

LOGGER = logging.getLogger(__name__)


class AddTagCommand(BaseCommand):
    """Add tag in front matter."""

    name = "add-tag"
    description = "Add tag to document"

    def register(self, subparsers) -> argparse.ArgumentParser:
        parser = super().register(subparsers)
        parser.add_argument(
            "file", type=argparse.FileType(mode="r+"), help="document file"
        )
        parser.add_argument("--tag", type=str, help="tag to add", required=True)
        return parser

    def handle(self, args: argparse.Namespace) -> None:
        LOGGER.debug("args=%s", args)

        with closing(args.file):
            document = load_document(args.file)
            document = add_item(document=document, jsonpath=TAG_JSONPATH, item=args.tag)
            overwrite_file(file=args.file, document=document)
