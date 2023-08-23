# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
import argparse
import json
import sys
from contextlib import closing

from py_frontmatter.core import load_document

from .base_command import BaseCommand
from .utils import overwrite_file


class SetCommand(BaseCommand):
    """Set front matter."""

    name = "set"
    description = "Set front matter from json input"

    def register(self, subparsers) -> argparse.ArgumentParser:
        parser = super().register(subparsers)
        parser.add_argument(
            "file", type=argparse.FileType(mode="r+"), help="document file"
        )
        return parser

    def handle(self, args: argparse.Namespace) -> None:
        meta = json.load(sys.stdin)

        with closing(args.file):
            document = load_document(args.file)
            document.meta = meta

            overwrite_file(file=args.file, document=document)
