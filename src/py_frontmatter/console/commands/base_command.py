import argparse


class BaseCommand:
    """Base class of command."""

    name = "base"
    description = "base description"

    def register(self, subparsers) -> argparse.ArgumentParser:

        parser = subparsers.add_parser(self.name, help=self.description)
        parser.set_defaults(func=self.handle)
        return parser

    def handle(self, args: argparse.Namespace):  # pragma: no cover
        del args
