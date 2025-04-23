from fm import FileManager
import base64
from parser.pe import ParseError

def main():
    #fm = FileManager()
    #tables = fm.LoadTables()
    
    #t = tables[0]
    #t.printTable()

    #t.getByParams(["Id"])

    e = ParseError(13, 'Expected "{" but found "%s"', "[")
    print(e)





if __name__ == "__main__":
    main()