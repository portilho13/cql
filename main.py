from fm import FileManager
import base64

def main():
    fm = FileManager()
    tables = fm.LoadTables()
    
    t = tables[0]
    #t.printTable()

    t.getByParams(["Id"])





if __name__ == "__main__":
    main()