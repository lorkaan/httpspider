from cli.cli_interface import CliBase

class CliEcho(CliBase):

    name = "echo"

    _arg_defintions = {
        '--msg': {
            'help': "Message to print"
        }
    }

    @classmethod
    def execute(cls, args):
        print(f"The Message is: {args.msg}")