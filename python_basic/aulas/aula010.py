'''
Docstring for python_basic.aulas.aula010

Fatiamento de strings
[i:f:p] [::]
Função len, retornar a quantidade de caracteres da str
'''

variavel = 'Olá, mundo!'

print('\n- Índices Positivos:')
print(variavel[1])      # Acessa o caractere que está no índice 1
print(variavel[:3])     # Retorna do início até o índice 3 (o 3 não é incluído)
print(variavel[2:])     # Retorna do índice 2 até o final da string
print(variavel[2:8])    # Retorna do índice 2 ao 7 (o índice 8 não é incluído)

'''
Da para fazer com valores de índices negativos
'''

print('\n- Índices Negativos:')
print(variavel[-1])      # Acessa o último caractere da string
print(variavel[:-3])     # Retorna do início até o índice -3 (exclui os 3 últimos caracteres)
print(variavel[-2:])     # Retorna do índice -2 até o final (os 2 últimos caracteres)
print(variavel[-8:-2])   # Retorna do índice -8 ao -3 (o índice -2 não é incluído)

print(variavel[1:8:2])   # Retorna do índice 0 ao 7, pulando de 2 em 2 caracteres
print(variavel[::-1])    # Inverte a string

'''
Introdução ao len
'''

print('\n- Função len:')


print(len(variavel))