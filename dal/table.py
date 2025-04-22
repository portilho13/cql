from .cell import Cell

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

        # Determine the number of rows (max length among all columns)
        num_rows = max((len(col) for col in self.dic.values()), default=0)

        # Build rows by extracting values from each Cell
        rows = []
        for i in range(num_rows):
            row = []
            for key in keys:
                try:
                    cell = self.dic[key][i]
                    value = cell.get() if isinstance(cell, Cell) else cell
                except IndexError:
                    value = ""  # Handle missing cells in shorter columns
                row.append(str(value) if value is not None else "")
            rows.append(row)

        # Calculate column widths based on headers and values
        col_widths = [
            max(len(str(k)), *(len(row[i]) for row in rows)) for i, k in enumerate(keys)
        ]

        # Build table border
        border = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

        # Build header row
        header = "| " + " | ".join(str(k).ljust(w) for k, w in zip(keys, col_widths)) + " |"

        # Print the table
        print(border)
        print(header)
        print(border)
        for row in rows:
            line = "| " + " | ".join(str(cell).ljust(w) for cell, w in zip(row, col_widths)) + " |"
            print(line)
        print(border)


    def get(self, param):
        #if param not in self.params:
            #Throw Exception as param as to exist in table
        if self.dic[param]:
            return self.dic[param]
        #param can exist with None value
        return None
        
    def add(self, param, val):
        #if param not in self.params:
            #Throw Exception as param as to exist in table
        self.dic[param].append(Cell(val))

    def remove(self, param):
        #if param not in self.params:
            #Throw Exception as param as to exist in table
        self.dic[param] = Cell(None)

    def update(self, param, val):
        #if param not in self.params:
            #Throw Exception as param as to exist in table
        self.dic[param] = Cell(val)



