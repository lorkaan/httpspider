import sys
import argparse
from functools import partial

from cli.cli_interface import CliBase
from cli.cli_echo import CliEcho
from cli.cli_build_graph import CliGraph

def run_cli():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    execute_dict = {}
    for sub_class in CliBase._register:
        sub_class.create_subparser(subparsers)
        execute_dict[sub_class.name] = partial(sub_class.execute)
    args = parser.parse_args()
    execute_dict[sys.argv[1]](args)