from fm import FileManager
import base64
from parser.pe import ParseError
from parser.pcql import ParserCQL

def main():
    #fm = FileManager()
    #tables = fm.LoadTables()
    
    #t = tables[0]
    #t.printTable()

    #t.getByParams(["Id"])

    imp = 'IMPORT TABLE observacoes FROM "ola";'
    export = 'EXPORT TABLE observacoes AS "ola";'

    p = ParserCQL()
    print(p.parse(export))





if __name__ == "__main__":
    main()