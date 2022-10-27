import argparse
import json
import sys
from contextlib import closing

from py_frontmatter.core import dump_document, load_document

from .base_command import BaseCommand


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

    def handle(self, args: argparse.Namespace) -> int:

        meta = json.load(sys.stdin)

        with closing(args.file):
            document = load_document(args.file)
            document.meta = meta

            args.file.seek(0)
            args.file.truncate()
            dump_document(document, args.file)

        return 0
