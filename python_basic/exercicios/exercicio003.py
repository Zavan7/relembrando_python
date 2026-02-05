'''
Docstring for python_basic.exercicios.exercicio003

Exercicios de if, elif e else + operadores de comparação
'''

valor_um = input('Digite o primeiro valor: ')
valor_dois = input('Digite o segundo valor: ')

if valor_um > valor_dois:
    print(f'\nPrimeiro valor é: {valor_um}')
    print(f'Sendo maior que o segundo valor, que é: {valor_dois}')

elif valor_dois > valor_um:
    print(f'\nSegundo valor é: {valor_dois}')
    print(f'Sendo maior que o primeiro valor, que é: {valor_um}')

elif valor_um == '' or valor_dois == '':
    print('\nValores não encontrados')

else:
    print('\nValores iguais')
