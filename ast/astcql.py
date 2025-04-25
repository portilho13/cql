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
    def __init__(self, text):
        self.table_name = text["identifier"]

class RenameTableNode(AstNode):
    def __init__(self, text):
        self.old_name = text["old_identifier"]
        self.new_name = text["new_identifier"]

class PrintTableNode(AstNode):
    def __init__(self, text):
        self.table_name = text["identifier"]

class SelectNode(AstNode):
    def __init__(self, text):
        self.sel = text["sel"],
        self.from_table_name = text["identifier"]
        self.optional_condition = OptionalConditionNode(text["condicao_opcional"])
        self.limit = text["limit_opcional"]

class ExtraConditionNode(AstNode):
    def __init__(self, text):
        self.condition = OptionalConditionNode(text["condicao_extra"])

class OptionalConditionNode(AstNode):
    def __init__(self, text):
        self.identifier = text["identifier"]
        self.operator = text["operador"]
        self.value = text["valor"]
        self.extra = ExtraConditionNode(text["condicao_extra"])
