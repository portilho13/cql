from parser.parser import Parser
from parser.pe import ParseError

class ParserCQL(Parser):
    def start(self):
        return self.programa()

    def programa(self):
        commands = []
        commands.append(self.comando())
        try:
            self.char(";")
            commands.extend(self.programa())
        except ParseError:
            pass  # ε (empty): end of program
        return commands

    def comando(self):
        return self.match('import_table', 
                          'export_table', 
                          'discard_table', 
                          'rename',
                          'print_table',
                          'select',
                          'create_table',
                          'procedure_def',
                          'procedure_call'
                          )

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
        c = self.maybe_char('"')
        if c is None:
            return None
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
    
    def discard_table(self):
        self.keyword("DISCARD TABLE")
        ident_start = self.char("a-zA-Z_")
        identifier = self.identificador(ident_start)
        return {"type": "DISCARD", "identifier": identifier}
    
    def rename(self):
        self.keyword("RENAME TABLE")
        ident_start_old = self.char("a-zA-Z_")
        identifier_old = self.identificador(ident_start_old)

        self.eat_whitespace() # Remove withespace between Identifiers

        ident_start_new = self.char("a-zA-Z_")
        identifier_new = self.identificador(ident_start_new)
        return {"type": "RENAME", "old_identifier": identifier_old, "new_identifier": identifier_new}

    def print_table(self):
        self.keyword("PRINT TABLE")
        ident_start = self.char("a-zA-Z_")
        identifier = self.identificador(ident_start)
        return {"type": "PRINT", "identifier": identifier}
    
    def select(self):
        self.keyword("SELECT")
        sel = self.selecao()
        self.keyword("FROM")
        ident_start = self.char("a-zA-Z_")
        identifier = self.identificador(ident_start)
        condicao_opcional = self.condicao_opcional()
        limit_opcional = self.limit_opcional()

        return {"type": "SELECT", "sel": sel, "identifier": identifier,
                "condicao_opcional": condicao_opcional, "limit_opcional": limit_opcional}

    
    def selecao(self):
        c = self.maybe_char("*")
        if c is None:
            return self.lista_colunas()
        else:
            return c
    
    def lista_colunas(self):
        li = []
        ident_start = self.char("a-zA-Z_")
        identifier = self.identificador(ident_start)

        li.append(identifier)

        c = self.maybe_char(",")
        if c is None: # If no mor identifiers return
            return li
        
        try:
            li.extend(self.lista_colunas())
        except ParseError:
            pass
        return li
    
    def condicao_opcional(self):
        try:
            self.keyword("WHERE")
            return self.condicao()
        except ParseError:
            pass # ε (empty): end of program
        return None

    def condicao(self):
        ident_start = self.char("a-zA-Z_")
        identifier = self.identificador(ident_start)
        operador = self.keyword("<=", ">=", "<>", "=", "<", ">") #Order this way because of self.pos
        valor = self.valor()
        condicao_extra = self.condicao_extra()
        return {"identifier": identifier, "operador": operador, "valor": valor,
                "condicao_extra": condicao_extra}

    def numero(self): # Only works with int's for now
        digits = ""
        digits += self.char("0-9")

        while True:
            try:
                digits += self.char("0-9")
            except ParseError:
                break
        
        return digits
    
    def valor(self):
        try:    # <numero>
            return self.numero()
        except ParseError:
            pass

        try: # <string literal>
            return self.string_literal()
        except ParseError:
            pass

        try: # <identificador>
            ident_start = self.char("a-zA-Z_")
            return self.identificador(ident_start)
        except ParseError:
            pass
    
    def condicao_extra(self):
        try:
            self.keyword("AND")
            return self.condicao()
        except ParseError:
            pass
        return None

    def limit_opcional(self):
        try:
            self.keyword("LIMIT")
            return self.numero()
        except ParseError:
            pass
        return None

    def create_table(self):
        self.keyword("CREATE TABLE")
        ident_start = self.char("a-zA-Z_")
        identifier = self.identificador(ident_start)
        create_body = self.create_body()
        return {
            "type": "CREATE",
            "identifier": identifier,
            "create_body": create_body 
        }

    def create_body(self):
        try:
            self.keyword("SELECT")
            selecao = self.selecao()
            self.keyword("FROM")
            ident_start = self.char("a-zA-Z_")
            identifier = self.identificador(ident_start)
            condicao_opcional = self.condicao_opcional()
            return {
                "selecao": selecao,
                "identifier": identifier,
                "condicao_opcional": condicao_opcional,
            }
        except ParseError:
            self.keyword("FROM")
            ident_start = self.char("a-zA-Z_")
            identifier = self.identificador(ident_start)
            self.keyword("JOIN")

            ident_start = self.char("a-zA-Z_")
            identifier2 = self.identificador(ident_start)

            self.keyword("USING")

            self.char("(")
            ident_start = self.char("a-zA-Z_")
            identifier3 = self.identificador(ident_start)
            self.char(")")

            return {
                "identifier": identifier,
                "identifier2": identifier2,
                "identifier3": identifier3,
            }
        
    def procedure_def(self):
        self.keyword("PROCEDURE")

        ident_start = self.char("a-zA-Z_")
        identifier = self.identificador(ident_start)

        self.keyword("DO")

        programa = self.programa()
        print(programa)


        self.keyword("END")

        return {
            "type": "PROCEDURE",
            "identifier": identifier,
            "programa": programa
        }
    
    def procedure_call(self):
        self.keyword("CALL")
        ident_start = self.char("a-zA-Z_")
        identifier = self.identificador(ident_start)

        return {
            "type": "CALL",
            "identifier": identifier
        }


        

        



    
