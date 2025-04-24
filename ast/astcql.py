from .ast import AstNode 

class ImportTableNode(AstNode):
    def __init__(self, table_name, source):
        self.type = "IMPORT"
        self.table_name = table_name
        self.source = source

class ExportTableNode(AstNode):
    def __init__(self, table_name, destination):
        self.type = "EXPORT"
        self.table_name = table_name
        self.destination = destination

class DiscardTableNode(AstNode):
    def __init__(self, table_name):
        self.type = "DISCARD"
        self.table_name = table_name

class RenameTableNode(AstNode):
    def __init__(self, old_name, new_name):
        self.type = "RENAME"
        self.old_name = old_name
        self.new_name = new_name

class PrintTableNode(AstNode):
    def __init__(self, table_name):
        self.type = "PRINT"
        self.table_name = table_name

class SelectNode(AstNode):
    def __init__(self, sel, from_table_name, condition, limit):
        self.type = "SELECT"
        self.sel = sel,
        self.from_table_name = from_table_name
        self.condition = condition
        self.limit = limit

class ConditionNode(AstNode):
    def __init__(self, identifier, operator, value, extra):
        self.identifier = identifier
        self.operator = operator
        self.value = value
        self.extra = extra