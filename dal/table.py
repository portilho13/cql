from . import Cell

class Table:
    def __init__(self, params):
        self.params = params
        self.dic = {}
        for param in params:
            self.dic[param] = Cell(None)
    
    def printParams(self):
        for param in self.params:
            print(f"Param:  {param} | Val: {self.dic[param]}")

    def get(self, param):
        #if param not in self.params:
            #Throw Exception as param as to exist in table
        if self.dic[param]:
            return self.dic[param].get()
        #param can exist with None value
        return None
        
    def add(self, param, val):
        #if param not in self.params:
            #Throw Exception as param as to exist in table
        self.dic[param] = Cell(val)

    def remove(self, param):
        #if param not in self.params:
            #Throw Exception as param as to exist in table
        self.dic[param] = Cell(None)

    def update(self, param, val):
        #if param not in self.params:
            #Throw Exception as param as to exist in table
        self.dic[param] = Cell(val)



