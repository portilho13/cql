class Cell:
    def __init__(self, val):
        if val:
            self.val = val
        
    def get(self):
        if self.val:
            return self.val
