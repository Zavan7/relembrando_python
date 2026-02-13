'''
Docstring for python_basic.exercicios.exercicio006
'''

nome = 'Vitor Zavan'
tamanho_nome = len(nome)
indice = 0
new_name = '*'

while indice < tamanho_nome:
    letra = nome[indice]
    new_name += f'{letra}*'
    indice += 1

print(new_name)