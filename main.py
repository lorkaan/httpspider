#!/bin/env python3
import sys
import objs
#import argparse
#from functools import partial
from structs.graph import DirectedKeyGraph
#from cli.cli_interface import CliBase
#from cli.cli_echo import CliEcho
from cli import run_cli


    
def test(*args):
    root = args[1]
    


if __name__ == '__main__':
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    execute_dict = {}
    for sub_class in CliBase._register:
        sub_class.create_subparser(subparsers)
        execute_dict[sub_class.name] = partial(sub_class.execute)
    args = parser.parse_args()
    execute_dict[sys.argv[1]](args)
    """
    run_cli()