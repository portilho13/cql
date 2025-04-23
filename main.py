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

    text = 'IMPORT TABLE observacoes FROM "ola";'

    p = ParserCQL()
    p.parse(text)





if __name__ == "__main__":
    main()