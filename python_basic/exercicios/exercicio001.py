'''
Docstring for python_basic.exercicios.exercicio001

Exercicio inicial com conceitos básicos de python
'''

from datetime import datetime

nome = 'Vitor'
sobrenome = 'Zavan'
idade = idade = 30
ano_nascimento = datetime.now().year - idade
maior_idade = lambda idade: idade >=18
altura_metros = 1.81

formulario = {
    'Nome: ': nome,
    'Sobrenome: ': sobrenome,
    'Idade: ': idade,
    'Ano de nascimento: ': ano_nascimento,
    'Maior de idade? ': maior_idade(idade),
    'Altura em metros: ': altura_metros
}

for x, y in formulario.items():
    print(x, y)