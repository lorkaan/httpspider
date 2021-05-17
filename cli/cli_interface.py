import argparse

class _CliInterfaceMeta(type):

    def __init__(cls, name, bases, dct):
        try:
            cls._register.append(cls)
        except Exception:
            cls._register = []


class CliBase(metaclass=_CliInterfaceMeta):

    name = "__base__"

    _arg_defintions = {}

    @classmethod
    def _load_parser_args(cls, parser):
        for k, v in cls._arg_defintions.items():
            parser.add_argument(k, **v)

    @classmethod
    def create_subparser(cls, sub_parser):
        parser = sub_parser.add_parser(cls.name)
        cls._load_parser_args(parser)
    
    @classmethod
    def execute(cls, args):
        raise NotImplementedError("Execute is not implmented")