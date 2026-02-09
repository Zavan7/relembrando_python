'''
Docstring for python_basic.aula003

Introdução a váriaveis
'''

nome_completo = 'Vitor Zavan'
idade = 29
maior_de_idade = lambda idade: idade >=18 # Função anônima, mais sobre, no futuro
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


'''
Variáveis e constantes
'''
# Variável
velocidade = 60 # Velocidade atual do carro
local_carro = 100 # Local em que o carro está na estrada


# Constante
RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

if (
    velocidade > RADAR_1
    and LOCAL_1 - RADAR_RANGE <= local_carro <= LOCAL_1 + RADAR_RANGE
):
    print('Multa')

else:
    print('Boa viagem')


'''
Função id
'''

var_um = 'a'
var_dois = 'b'
print(id(var_um))
print(id(var_dois))