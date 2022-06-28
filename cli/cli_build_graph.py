from cli.cli_interface import CliBase, CliArgumentParser
from api.graph import createGraph as make_graph

class CliGraph(CliBase):

    name = "graph"

    _arg_defintions = {
        'root': {
            CliArgumentParser.field_key: ['-r', '--root'],
            CliArgumentParser.extra_arguments: {
                'help': "Root to Start at",
                "nargs": "+",
                "required": True
            }
        },
        'depth': {
            CliArgumentParser.field_key: ['-d', '--depth'],
            CliArgumentParser.extra_arguments: {
                'help': "Maximum depth (or degree of separation) from the Root",
                'default': 2
            }
        }
    }

    @classmethod
    def execute(cls, args):
        print(f"The Root is: {args.root}")
        graph, parsedInfo = make_graph(args.root, int(args.depth))
        print("\t------ Parsed Info -----\n")
        counter = 0
        for key, val in parsedInfo.items():
            print(f"{counter}:  {key}\t{val}\n")
            counter = counter + 1