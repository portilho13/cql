from typing import List, Dict

class QueryResult:
    def __init__(self, dic, params):
        self.res = []

        for param in params:
            di = {}
            di[param] = [val.get() for val in dic[param]]
            self.res.append(di)

        self.printSelectedTable(self.res)

    
    def printSelectedTable(self, res: List[Dict]):
        if not res:
            print("No data available.")
            return
        keys = [key for dic in res for key in dic.keys()]
        columns = [dic[key] for dic in res for key in dic.keys()]
        num_rows = max(len(col) for col in columns)
        for i in range(len(columns)):
            if len(columns[i]) < num_rows:
                columns[i] += [""] * (num_rows - len(columns[i]))
        rows = list(zip(*columns))
        col_widths = [
            max(len(str(k)), *(len(str(row[i])) for row in rows)) for i, k in enumerate(keys)
        ]
        border = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
        header = "| " + " | ".join(k.ljust(w) for k, w in zip(keys, col_widths)) + " |"
        print(border)
        print(header)
        print(border)
        for row in rows:
            line = "| " + " | ".join(str(cell).ljust(w) for cell, w in zip(row, col_widths)) + " |"
            print(line)
        print(border)
        