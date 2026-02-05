"""
Docstring for python_basic.aulas.aula008

Introdução a Operadores de Comparação e Operadores Lógicos
"""

# ==================================================
print('\n=== OPERADORES DE COMPARAÇÃO ===\n')
# ==================================================

# >  Maior
maior = 2 > 1

# >= Maior ou igual
maior_ou_igual = 2 >= 2

# <  Menor
menor = 1 < 2

# <= Menor ou igual
menor_ou_igual = 3 <= 4

# == Igual
igual = 'a' == 'a'

# != Diferente
diferente = 'A' != 'a'

print('Maior (2 > 1):', maior)
print('Maior ou igual (2 >= 2):', maior_ou_igual)
print('Menor (1 < 2):', menor)
print('Menor ou igual (3 <= 4):', menor_ou_igual)
print('Igual ("a" == "a"):', igual)
print('Diferente ("A" != "a"):', diferente)

# Observação:
# Operadores de comparação SEMPRE retornam um valor booleano (True ou False)


# ==================================================
print('\n=== OPERADORES LÓGICOS: AND ===\n')
# ==================================================

# AND: todas as condições precisam ser True
resultado_and = True and True and False
print('True and True and False:', resultado_and)

entrada = input('[E]ntrar [S]air: ')
senha_ = '123456'
senha = input('Digite sua senha: ')

if entrada == 'S':
    print('Você saiu')

elif entrada == 'E' and senha == senha_:
    print('Bem-vindo de volta!')

elif entrada == 'E' and senha != senha_:
    print('Senha e/ou login incorretos, tente novamente')

else:
    print('Error 404')


# ==================================================
print('\n=== OPERADORES LÓGICOS: OR ===\n')
# ==================================================

# OR: pelo menos uma condição precisa ser True
resultado_or = True or True or False
print('True or True or False:', resultado_or)

entrada = input('[E]ntrar [S]air: ')
senha = input('Digite sua senha: ')

if entrada == 'S' or entrada == 's':
    print('Você saiu')

elif (entrada == 'E' or entrada == 'e') and senha == senha_:
    print('Bem-vindo de volta!')

elif (entrada == 'E' or entrada == 'e') and senha != senha_:
    print('Senha e/ou login incorretos, tente novamente')

else:
    print('Error 404')


# ==================================================
print('\n=== OPERADOR LÓGICO: NOT ===\n')
# ==================================================

# NOT: inverte o valor lógico
print('not True:', not True)
print('not False:', not False)
print('not 0:', not 0)
print('not "":', not '')

senha = input('Digite sua senha: ')
if not senha:
    print('Senha não digitada')
else:
    print('Senha digitada')


# ==================================================
print('\n=== OPERADOR LÓGICO: IN ===\n')
# ==================================================

# IN: verifica se um valor está presente em uma sequência
lista_um = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print('Lista:', lista_um)
print('1 in lista_um:', 1 in lista_um)
print('10 in lista_um:', 10 in lista_um)


# ==================================================
print('\n=== OPERADOR LÓGICO: NOT IN ===\n')
# ==================================================

# NOT IN: verifica se um valor NÃO está presente em uma sequência
print('10 not in lista_um:', 10 not in lista_um)
print('2 not in lista_um:', 2 not in lista_um)
