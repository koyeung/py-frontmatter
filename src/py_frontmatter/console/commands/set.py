# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
import json
import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import argparse

from py_frontmatter.core import load_document

from .base_command import BaseCommand
from .utils import overwrite_file


class SetCommand(BaseCommand):
    """Set front matter."""

    name = "set"
    description = "Set front matter from json input"

    def register(
        self, subparsers: argparse._SubParsersAction[argparse.ArgumentParser]
    ) -> argparse.ArgumentParser:
        parser = super().register(subparsers)
        parser.add_argument(
            "file",
            type=Path,
            help="document file",
        )
        return parser

    def handle(self, args: argparse.Namespace) -> None:
        meta = json.load(sys.stdin)

        with args.file.open(mode="r+") as f:
            document = load_document(f)
            document.meta = meta

            overwrite_file(file=f, document=document)
