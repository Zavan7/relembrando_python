'''
Docstring for python_basic.aula003

Introdução a váriaveis
'''

nome_completo = 'Vitor Zavan'
idade = 29
maior_de_idade = lambda idade: idade >=18 #função anônima, mais sobre, no futuro
curso_ativo = True
nota = 9.8

formulario_aluno = {
    'Nome_completo:': nome_completo,
    'Idade:': idade,
    'É maior de idade?': maior_de_idade(idade),
    'Está ativo no curso?': curso_ativo,
    'Nota': nota
}
for x, y in formulario_aluno.items():
    print(x, y)
