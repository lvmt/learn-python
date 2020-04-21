# cli.py

import argparse

parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(help="commands")

## create
create_parser = subparser.add_parser(
        'create', help="create a directory")

create_parser.add_argument(
    'dirname', action="store",
    help="New dir to create" )

## Delete
delete_parser = subparser.add_parser(
        'delete', help="remove a dir")

delete_parser.add_argument(
    'dirname', action="store",
    help="the dir to remove")

delete_parser.add_argument(
    '--recursive', '-r', default=False, action="store_true",
    help="Recursively remove the dir")

args = parser.parse_args() 






