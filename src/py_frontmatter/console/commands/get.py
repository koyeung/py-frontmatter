# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
import argparse
import json
import shlex
from contextlib import closing

from py_frontmatter.core import load_document

from .base_command import BaseCommand


class GetCommand(BaseCommand):
    """Get front matter."""

    name = "get"
    description = "Retrieve front matter as json string"

    def register(self, subparsers) -> argparse.ArgumentParser:
        parser = super().register(subparsers)
        parser.add_argument("infile", type=argparse.FileType(), help="input file")
        parser.add_argument(
            "--sq", action="store_true", help="shell quote (experimental)"
        )
        return parser

    def handle(self, args: argparse.Namespace) -> None:
        with closing(args.infile):
            document = load_document(args.infile)

        meta_json = json.dumps(document.meta)

        if args.sq:
            meta_json = shlex.quote(meta_json)

        print(meta_json)  # noqa: T201
