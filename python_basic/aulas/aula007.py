'''
Docstring for python_basic.aulas.aula007

Introdução a condicionais (if, elif e else)
'''

entrada = input('Você deseja entrar ou sair? (Digite: entrar ou sair para prosseguir) ')

if entrada.lower() == 'entrar': # Formatando o valor digitado, para lower case, para garantir comparação correta dos valores
    print('Você entrou no sistema')

elif entrada.lower == 'sair': # Formatando o valor digitado, para lower case, para garantir comparação correta dos valores
    print('Você saiu do programa')
    
else:
    print('Detectamos algum erro, tente novamente')