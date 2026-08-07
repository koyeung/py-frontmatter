# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
import json
import shlex
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import argparse

from py_frontmatter.core import load_document

from .base_command import BaseCommand


class GetCommand(BaseCommand):
    """Get front matter."""

    name = "get"
    description = "Retrieve front matter as json string"

    def register(
        self, subparsers: argparse._SubParsersAction[argparse.ArgumentParser]
    ) -> argparse.ArgumentParser:
        parser = super().register(subparsers)
        parser.add_argument("infile", type=Path, help="input file")
        parser.add_argument(
            "--sq",
            action="store_true",
            help="shell quote (experimental)",
        )
        return parser

    def handle(self, args: argparse.Namespace) -> None:
        with args.infile.open(mode="r+") as f:
            document = load_document(f)

        meta_json = json.dumps(document.meta)

        if args.sq:
            meta_json = shlex.quote(meta_json)

        print(meta_json)  # noqa: T201
