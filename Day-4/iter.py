class Iteration:
    def __init__(self,data):
        self.data = data
        self.index = len(data)
      

    def _iter_(self):
        return self

    def __next__(self):
        
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

    name = input("enter the name:")
    
    iter(name)
    last = len(name)
    for char in range(last): print(name[last-1-char])