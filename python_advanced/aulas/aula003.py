'''
Docstring for python_advanced.aulas.aula003
'''

class SquareIterator:
    def __init__(self, max_root_value):
        self.max_root_value = max_root_value
        self.current_root_value = 0
    
    def __iter__ (self):
        return self
    
    def __next__ (self):
        if self.current_root_value >= self.max_root_value:
            raise StopIteration
        square_value = self.current_root_value ** 2
        self.current_root_value += 1
        return square_value
    
for square in SquareIterator(10):
    print(square)