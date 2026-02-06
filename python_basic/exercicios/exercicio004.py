'''
Docstring for python_basic.exercicios.exercicio004

Reforçando conhecimento
'''

def type_conversion(value):
    '''
    Docstring for type_conversion
    
    :param value: Description

    Função para validar valores int fornecidos pelo usuário
    '''
    if isinstance(value, str) and value.isdigit():
        return int(value)
    raise ValueError ('Valor precisa ser um número inteiro')

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

idade = type_conversion(idade)

if not nome or not idade:
    print('Nome e/ou idade ausentes')

elif nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaço(s)')
    else:
        print('Seu nome NÃO contém espeço(s)')

    print(f'Seu nome contém {len(nome)} caractéres')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')

else:
    print('Erro, tente novamente')