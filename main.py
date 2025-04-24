from fm import FileManager
import base64
from parser.pe import ParseError
from parser.pcql import ParserCQL
from ast.ast import Ast

def main():
    #fm = FileManager()
    #tables = fm.LoadTables()
    
    #t = tables[0]
    #t.printTable()

    #t.getByParams(["Id"])

    imp = 'IMPORT TABLE observacoes FROM "ola";'
    export = 'EXPORT TABLE observacoes AS "ola";'
    discard = 'DISCARD TABLE observacoes;'
    rename = 'RENAME TABLE ola1 ola2;'
    print_table = 'PRINT TABLE ola;'
    select = 'SELECT id,nome,etc FROM ola WHERE id >= 1;'
    create = 'CREATE TABLE completo FROM estacoes JOIN observacoes USING(Id);'
    procedure_text = """PROCEDURE atualizar_observacoes DO
        CREATE TABLE mais_quentes SELECT * FROM observacoes WHERE Temperatura > 22;
        CREATE TABLE completo FROM estacoes JOIN observacoes USING(Id);
    END"""
    call = "CALL atualizar_vendas;"

    select_with_comments = """
    SELECT id,nome,etc FROM ola WHERE id >= 1;
    -- This is a single-line comment
    {- This is a block comment
    spanning multiple lines -}
    """

    p = ParserCQL()

    queries = [imp, export, discard, rename, print_table, select, create, procedure_text, call, select_with_comments]
    for query in queries:
        print(p.parse(query))

    l = [p.parse(imp), p.parse(export)]

    ast = Ast(l)
    
    ast.parse()
    ast.pretty_print()


    #import_ast = ImportTableNode(l['identifier'], l['source'])
    #import_ast.pretty_print()

    #export_ast = ExportTableNode(l)


if __name__ == "__main__":
    main()