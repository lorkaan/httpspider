from cli.cli_interface import CliBase, CliArgumentParser
from api.graph import createGraphSpider as make_graph

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
        graph = None        # Reasonable Default for initialization
        parsedInfo = {}     # Reasonable Default for initialization
        #graph, parsedInfo = make_graph(args.root, int(args.depth))
        graph_tuple_list = make_graph(args.root, int(args.depth)) # This makes a list of size 1 now with tuples as elements
        if isinstance(graph_tuple_list, list) and len(graph_tuple_list) >= 1 and isinstance(graph_tuple_list[0], tuple) and len(graph_tuple_list[0]) >= 2:
            # Changes made graph output a list, further handling required but this hack will hold up
            # For Now
            graph_tuple = graph_tuple_list[0]
            graph = graph_tuple[1]
            parsedInfo = graph_tuple[0]
        counter = 0
        for key, val in parsedInfo.items():
            print(f"{counter}:  {key}\t{val}\n")
            counter = counter + 1
        if graph == None:
            print("Graph Could not be made due to Internal Error")
        else:
            print("All Done")