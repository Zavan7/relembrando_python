'''
Docstring for python_basic.aula002

Introdução aos tipos de dados
'''

type_str = 'Pode ser identado com aspas simples ou duplas' #string
type_int = 12345 #int
type_float = 123.45 #float
type_bool = True or False #booleano
caracter_escape_um = 'Vitor \'Zavan\'' #string
caracter_escape_dois = "Vitor 'Zavan'" #string

print(caracter_escape_um)
print(caracter_escape_dois)


'''
Vamos dar uma atenção aos ints e floats
Float é separado por ponto(.)
Usamos virgula, para separar argumentos ('teste', 123, True)
'''
print(type(type_float))
print(type(type_bool))
print(type(type_int))


'''
Vamos dar uma atenção nos tipos, boolean
True or False
'''

print(10 == 10) #Sim => True (Verdadeiro)
print(10 > 10) #Não => False (Falso)
print(type(10 > 10)) #Não => False (Falso)


'''
Type conversion

Vamos ver como converter os tipos em Python
'''

soma = 1+1
print(float(soma))

concat = 'a' + ' - ' +'1'
print(concat)

# concat_ou_soma_um = 1 + '1' - Vai dar erro
# print(concat_ou_soma_um)

concat_ou_soma_dois = 1 + int('1')
print(concat_ou_soma_dois)

int_para_str = 'a' + str(11)
print(int_para_str)

'''
Strings vazias, 0, valores vazios, None, são False
'''
print(bool(0)) #=> False
print(bool('')) #=> False
print(bool(None)) #=> False