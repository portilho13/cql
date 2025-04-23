from .cell import Cell
from typing import List
from .qr import QueryResult

class Table:
    def __init__(self, params):
        self.params = params
        self.dic = {}
        for param in params:
            self.dic[param] = []
    
    def printParams(self):
        for param in self.params:
            print(f"Param:  {param}")
        
    def printTable(self):
        keys = list(self.dic.keys())
        num_rows = max((len(col) for col in self.dic.values()), default=0)
        rows = []
        for i in range(num_rows):
            row = []
            for key in keys:
                try:
                    cell = self.dic[key][i]
                    value = cell.get() if isinstance(cell, Cell) else cell
                except IndexError:
                    value = ""
                row.append(str(value) if value is not None else "")
            rows.append(row)
        col_widths = [
            max(len(str(k)), *(len(row[i]) for row in rows)) for i, k in enumerate(keys)
        ]
        border = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
        header = "| " + " | ".join(str(k).ljust(w) for k, w in zip(keys, col_widths)) + " |"
        print(border)
        print(header)
        print(border)
        for row in rows:
            line = "| " + " | ".join(str(cell).ljust(w) for cell, w in zip(row, col_widths)) + " |"
            print(line)
        print(border)
    


    def getByParams(self, params) -> QueryResult: #Select x, y, z FROM .....\
        qr = QueryResult(self.dic, params)
        return qr
    
    #def getByValues(self, params, liDict) -> List[Dict]: #Select x, y, z FROM .... where x = xxxx
        
    def add(self, param, val):
        self.dic[param].append(Cell(val))

    def remove(self, param):
        self.dic[param] = Cell(None)

    def update(self, param, val):
        self.dic[param] = Cell(val)
