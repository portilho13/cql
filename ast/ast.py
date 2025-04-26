
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
            instr.pretty_print(indent + 2)

    def parse(self):
        programa = ProgramaNode(self.instructions)
        self.parsed_instructions = programa.commands
