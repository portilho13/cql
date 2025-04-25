
from ast.astcql import *

class Ast():
    def __init__(self, instructions):
        self.instructions = instructions
        self.parsed_instructions = []

    def pretty_print(self, indent=0):
        prefix = " " * (indent * 2)
        print(f"{prefix}Ast:")

        if not self.parsed_instructions:
            print(f"{prefix}  (no parsed instructions)")
            return

        print(f"{prefix}  parsed_instructions:")
        for instr in self.parsed_instructions:
            if isinstance(instr, AstNode):
                instr.pretty_print(indent + 2)
            else:
                print(f"{prefix}    {instr}")

    

    def parse(self):
        for instruction in self.instructions:
            ins = instruction[0]
            node_type = ins["type"] #Fix this, ast should be created recursibly ?

            match node_type:
                case "IMPORT":
                    self.parsed_instructions.append(ImportTableNode(ins))
                case "EXPORT":
                    self.parsed_instructions.append(ExportTableNode(ins))
                case "DISCARD":
                    self.parsed_instructions.append(DiscardTableNode(ins))
                case "RENAME":
                    self.parsed_instructions.append(RenameTableNode(ins))
                case "PRINT":
                    self.parsed_instructions.append(PrintTableNode(ins))
                case "SELECT":
                    self.parsed_instructions.append(SelectNode(ins))
                case _:
                    pass