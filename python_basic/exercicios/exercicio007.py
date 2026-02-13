'''
Docstring for python_basic.exercicios.exercicio007
'''


def type_conversion(value):
    if isinstance(value, str) and value.isdigit():
        return int(value)
    raise ValueError


while True:
    sair = input('Para sair, digite (S), caso não, aperte enter e continue: ')
    if sair.upper() == 'S':
        print('Você saiu, nos vemos em breve!')
        break

    try:
        operador = input('Escolha um operador matemático (+ - / *): ')
        num_um = input('Digite um número: ')
        num_dois = input('Digite outro número: ')

        num_um = type_conversion(num_um)
        num_dois = type_conversion(num_dois)

    except ValueError as e:
        print(f'Erro: {e}')


    if operador == '+':
        print(f'SOMA: {num_um + num_dois}')

    elif operador == '-':
        print(f'SUBTRAÇÃO: {num_um - num_dois}')

    elif operador == '/':
        if num_dois == 0:
            print('Não existe divisão por zero')
        elif num_um == 0:
            print('Não existe divisão por zero')
        else:
            print(f'DIVISÃO: {num_um / num_dois}')

    elif operador == '*':
        print(f'MULTIPLICAÇÃO: {num_um * num_dois}')

    else:
        print('Operador inválido')

