'''
Docstring for python_advanced.aulas.aula001

Função geradora
Uma função geradora sempre retornará um objeto gerador. Ela nunca poderá retornar outra coisa
'''

from typing import Iterator

def gen_nums() -> Iterator[int]:
    n = 0
    while n < 4:
        yield n
        n += 1
    yield 45

# for num in gen_nums():
#     print(num)

sequence = gen_nums()
print(type(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence, 'Vitor'))