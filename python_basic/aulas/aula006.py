'''
Docstring for python_basic.aulas.aula006

Introdução a Input
'''

# input('Qual o seu nome? ')

# Vamos salvar a resposta dada pelo usuário, dentro de uma variável
# idade = int(input('Digite sua idade: ')) Forma errada de conversão

nome = input('Qual o seu nome? ')
idade = input('Digite sua idade: ')

def type_conversion(value):
    if isinstance(value, str) and value.isdigit():
        return int(value)
    raise ValueError ('Valor precisa ser um número inteiro')


idade = type_conversion(idade)

frase = f'Olá, meu nome é {nome}, tenho {idade} anos, e o tipo da variável idade é "{type(idade)}"'
print(frase)

print(30 * '#')

num_um = input('Digite um número: ')
num_dois = input ('Digite outro número: ')

num_um = type_conversion(num_um)
num_dois = type_conversion(num_dois)

soma = num_um + num_dois

print(f'A soma de {num_um} + {num_dois} é: {soma}')
