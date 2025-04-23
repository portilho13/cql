from fm import FileManager
import base64
from parser.pe import ParseError
from parser.parser import Parser

def main():
    #fm = FileManager()
    #tables = fm.LoadTables()
    
    #t = tables[0]
    #t.printTable()

    #t.getByParams(["Id"])

    text = "" \
    "SELECT * FROM observacoes;"

    p = Parser()
    p.parse(text)





if __name__ == "__main__":
    main()