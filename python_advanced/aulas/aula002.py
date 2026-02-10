'''
Docstring for python_advanced.aulas.aula002

Função geradora
'''

def fetch_squares(max_root):
    squares = []
    for num in range(max_root):
        squares.append(num ** 2)
    return squares

MAX = 5

for squares in fetch_squares(MAX):
    print(squares)