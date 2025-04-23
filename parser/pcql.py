from parser.parser import Parser
from parser.pe import ParseError

class ParserCQL(Parser):
    def start(self):
        return self.programa()

    def programa(self):
        commands = []
        commands.append(self.comando())
        self.char(";")
        try:
            commands.extend(self.programa())
        except ParseError:
            pass  # ε (empty): end of program
        return commands

    def comando(self):
        return self.match('import_table', 'export_table')

    def import_table(self):
        self.keyword("IMPORT TABLE")
        ident_start = self.char("a-zA-Z_")
        identifier = self.identificador(ident_start)
        self.keyword("FROM")
        string = self.string_literal()
        return {"type": "IMPORT", "identifier": identifier, "source": string}

    def identificador(self, first_char):
        rv = first_char
        while True:
            try:
                ch = self.char("a-zA-Z0-9_")
                rv += ch
            except ParseError:
                break
        return rv

    def string_literal(self):
        self.char('"')
        start = self.pos + 1
        while True:
            ch = self.char()
            if ch == '"':
                break
        end = self.pos
        return self.text[start:end]
    
    def export_table(self):
        self.keyword("EXPORT TABLE")
        ident_start = self.char("a-zA-Z_")
        identifier = self.identificador(ident_start)
        self.keyword("AS")
        string = self.string_literal()
        return {"type": "EXPORT", "identifier": identifier, "destination": string}
    
