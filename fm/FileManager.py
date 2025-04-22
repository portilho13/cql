import os
import csv
from typing import List, Dict
from dal import Table

class FileManager:
    def __init__(self, path='./tables'):
        self.path = path

    def LoadTables(self) -> List[Table]:
        files_names = os.listdir(self.path)

        files_dirs = [self.path + "/" + file_name for file_name in files_names] # file dir = main dir + tables folder + table name

        for file in files_dirs:
            l = self.readFiles(file)
            params = self.getParamNames(l)
            t = Table(params)
            self.populateTable(t, l)
            t.printTable()
    
    def readFiles(self, file) -> List[Dict[str, str]]:
        with open(file) as f:
            l = [] # List of returning dicts
            line = csv.DictReader(f)
            for row in line:
                l.append(row)
            return l
    
    def getParamNames(self, liDicts) -> List[str]:
        params = []
        dic = liDicts[0]
        if len(dic) == 0:
            return []
        for key in dic.keys():
            if key not in params:
                params.append(key)
        return params
    
    def populateTable(self, table, liDict) -> Table:
        for dic in liDict:
            for _, (key, value) in enumerate(dic.items()):
                table.add(key, value)
        return table