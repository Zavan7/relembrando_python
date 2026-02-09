'''
Docstring for python_basic.exercicios.exercicio005
'''

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num_um = input('Digite seu número aqui, veja se é par ou impar: ')

def is_number(value: str) -> int:
    if isinstance(value, str) and value.isdigit():
        return int(value)
    raise ValueError ('Valor precisa ser um número')

num_um = is_number(num_um)

if num_um == 0:
    raise ZeroDivisionError

elif num_um % 2 == 0:
    print(f'O número {num_um} é PAR')

else:
    print(f'O número {num_um} é IMPAR')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

num_dois = input('Digite a hora atual. Ex: 10, 12, 14: ')


def is_number(value: str) -> int:
    if isinstance(value, str) and value.isdigit():
        return int(value)
    raise ValueError ('Valor precisa ser um número')

num_dois = is_number(num_dois)

if num_dois >= 0 and num_dois <= 11:
    print('Bom dia!')

elif num_dois >= 12 and num_dois <= 17:
    print('Boa tarde!')

elif num_dois >= 18 and num_dois <= 23:
    print('Boa noite!')

else:
    print('Horario inválido')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')

elif len(nome) >= 5 and len(nome) <=6:
    print('Seu nome é normal')

else:
    print('Seu nome é grande')