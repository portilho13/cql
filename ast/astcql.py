from .an import AstNode 

class ImportTableNode(AstNode):
    def __init__(self, text):
        self.type = "IMPORT"
        self.table_name = text["identifier"]
        self.source = text["source"]

class ExportTableNode(AstNode):
    def __init__(self, text):
        self.table_name = text["identifier"]
        self.destination = text["destination"]

class DiscardTableNode(AstNode):
    def __init__(self, table_name):
        self.table_name = table_name

class RenameTableNode(AstNode):
    def __init__(self, old_name, new_name):
        self.old_name = old_name
        self.new_name = new_name

class PrintTableNode(AstNode):
    def __init__(self, table_name):
        self.table_name = table_name

class SelectNode(AstNode):
    def __init__(self, sel, from_table_name, optional_condition, limit):
        self.sel = sel,
        self.from_table_name = from_table_name
        self.optional_condition = optional_condition
        self.limit = limit

class OptionalConditionNode(AstNode):
    def __init__(self, condition):
        self.condition = condition

class ConditionNode(AstNode):
    def __init__(self, identifier, operator, value, extra):
        self.identifier = identifier
        self.operator = operator
        self.value = value
        self.extra = extra