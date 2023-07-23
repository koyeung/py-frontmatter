# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
import argparse
import logging

from py_frontmatter import __version__

from .commands import (
    AddItemCommand,
    AddTagCommand,
    GetCommand,
    RemoveItemCommand,
    RemoveTagCommand,
    SetCommand,
)

LOGGER = logging.getLogger(__name__)
_LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s %(message)s"

_COMMANDS = [
    GetCommand(),
    SetCommand(),
    AddItemCommand(),
    RemoveItemCommand(),
    AddTagCommand(),
    RemoveTagCommand(),
]


def main() -> None:
    logging.basicConfig(level=logging.INFO, format=_LOG_FORMAT)

    parser = argparse.ArgumentParser(description="Process YAML front matter.")
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument("--debug", action="store_true", help="show debug log messages")

    subparsers = parser.add_subparsers(help="sub-commands")
    for command in _COMMANDS:
        command.register(subparsers)

    args = parser.parse_args()

    if args.debug:
        logging.getLogger("py_frontmatter").setLevel(logging.DEBUG)

    if not hasattr(args, "func"):
        parser.print_help()

    args.func(args)


if __name__ == "__main__":
    main()
