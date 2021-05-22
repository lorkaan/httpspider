import argparse

class CliArgumentParser:

    field_key = "__fields__"
    extra_arguments = "__kwargs__"

    @classmethod
    def parse_dict(cls, key, obj):
        if not isinstance(obj, dict):
            raise TypeError(f"Can not parse object of type: {type(obj)}")
        names = obj.get(cls.field_key, [])
        keyword_args = obj.get(cls.extra_arguments, None)
        if not isinstance(names, list):
            raise TypeError(f"The key: {cls.field_key} needs to be of type 'list'")
        if len(names) <= 0:
            names.append(key)
        if isinstance(keyword_args, dict) and len(keyword_args.keys()) > 0:
            return names, keyword_args
        else:
            return names, None # just in case of non-dict entry

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
            aliases, argument_opts = CliArgumentParser.parse_dict(k, v)
            if isinstance(argument_opts, dict):
                parser.add_argument(*aliases, **argument_opts)
            else:
                parser.add_argument(*aliases)

    @classmethod
    def create_subparser(cls, sub_parser):
        parser = sub_parser.add_parser(cls.name)
        cls._load_parser_args(parser)
    
    @classmethod
    def execute(cls, args):
        raise NotImplementedError("Execute is not implmented")