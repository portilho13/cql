
from ast.astcql import *

class AstNode():
    def __init__(self):
        self.isVisited = False

    def pretty_print(self, indent=0):
        prefix = " " * (indent * 2)
        print(f"{prefix}{self.__class__.__name__}")
        for key, value in self.__dict__.items():
            if isinstance(value, AstNode):
                print(f"{prefix}  {key}:")
                value.pretty_print(indent + 2)
            elif isinstance(value, list):
                print(f"{prefix}  {key}: [")
                for item in value:
                    if isinstance(item, AstNode):
                        item.pretty_print(indent + 3)
                    else:
                        print(f"{' ' * ((indent + 3) * 2)}{item}")
                print(f"{prefix}  ]")
            else:
                print(f"{prefix}  {key}: {value}")
    

    def parse(self, text):
        node_type = text["type"]

        match node_type:
            case "IMPORT":
                return ImportTableNode(text)
