import argparse
import logging

from py_frontmatter import __version__

from .commands import AddItemCommand, GetCommand, RemoveItemCommand, SetCommand

LOGGER = logging.getLogger(__name__)
_LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s %(message)s"

_COMMANDS = [GetCommand(), SetCommand(), AddItemCommand(), RemoveItemCommand()]


def main() -> int:
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
        return 1

    exit_code: int = args.func(args)
    return exit_code


if __name__ == "__main__":
    main()
