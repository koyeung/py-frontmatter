import argparse

from py_frontmatter import __version__

from .commands import GetCommand, SetCommand

_COMMANDS = [
    GetCommand(),
    SetCommand(),
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Process YAML front matter.")
    parser.add_argument("--version", action="version", version=__version__)
    subparsers = parser.add_subparsers(help="sub-commands")

    for command in _COMMANDS:
        command.register(subparsers)

    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        return 1

    exit_code: int = args.func(args)
    return exit_code


if __name__ == "__main__":
    main()
