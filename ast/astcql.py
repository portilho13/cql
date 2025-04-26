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
        self.sel = text["sel"]
        self.from_table_name = text["identifier"]
        self.optional_condition = OptionalConditionNode(text["condicao_opcional"]) if text["condicao_opcional"] else None
        self.limit = text["limit_opcional"]

class ExtraConditionNode(AstNode):
    def __init__(self, text):
        self.optional_condition = OptionalConditionNode(text["condicao_opcional"]) if text["condicao_opcional"] else None

class OptionalConditionNode(AstNode):
    def __init__(self, text):
        self.identifier = text["identifier"]
        self.operator = text["operador"]
        self.value = text["valor"]
        self.extra = [ExtraConditionNode(state) for state in text["condicao_extra"]] if text["condicao_extra"] else []
    
class CreateNode(AstNode):
    def __init__(self, text):
        self.table_name = text["identifier"]
        self.create_body = CreateBodyNode(text["create_body"])

class CreateBodyNode(AstNode):
    def __init__(self, text):
        match text["type"]:
            case "SELECT":
                self.type = "SELECT"
                self.body = SelectNode(text)
            case "FROM":
                self.type = "FROM"
                self.source_name = text["identifier2"]
                self.join_name = text["identifier3"]
                self.body = None

class ProcedureNode(AstNode):
    def __init__(self, text):
        self.identifier = text["identifier"]
        programa = text["programa"]
        self.programa = ProgramaNode(programa["commands"])

class ProgramaNode(AstNode):
    def __init__(self, instructions_list):
        self.commands = []

        for ins in instructions_list:
            node_type = ins["type"]

            match node_type:
                case "IMPORT":
                    self.commands.append(ImportTableNode(ins))
                case "EXPORT":
                    self.commands.append(ExportTableNode(ins))
                case "DISCARD":
                    self.commands.append(DiscardTableNode(ins))
                case "RENAME":
                    self.commands.append(RenameTableNode(ins))
                case "PRINT":
                    self.commands.append(PrintTableNode(ins))
                case "SELECT":
                    self.commands.append(SelectNode(ins))
                case "CREATE":
                    self.commands.append(CreateNode(ins))
                case "PROCEDURE":
                    self.commands.append(ProcedureNode(ins))
                case "PROGRAMA":
                    self.commands.extend(ProgramaNode(ins["commands"]).commands)
                case "CALL":
                    self.commands.append(CallNode(ins))
                case _:
                    print(f"Unknown node type: {node_type}")

class CallNode(AstNode):
    def __init__(self, text):
        self.identifier = text["identifier"]

