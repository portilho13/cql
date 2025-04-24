from .ast import AstNode 

class ImportNode(AstNode):
    def __init__(self, table_name, source):
        self.type = "IMPORT"
        self.table_name = table_name
        self.source = source