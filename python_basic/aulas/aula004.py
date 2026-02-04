'''
Docstring for python_basic.aulas.aula004

Operadores lógicos
'''

print('Operadores lógicos')
adicao = 10 + 10
print('Adição:', adicao)

subtracao = 10 - 5
print('Subtração:', subtracao)

multiplicacao = 10 * 10
print('Multiplicação:', multiplicacao)

divisao = 10 / 2.2
print('Divisão:', divisao)

divisao_inteira = 10 // 2.2
print('Divisao Inteira:', divisao_inteira)

divisao_inteira = 10 // 2.2
print('Divisao Inteira, formatado para int:', int(divisao_inteira))

exponenciacao = 2 ** 10
print('Exponenciação:', exponenciacao)

resto_divisao = 55 % 2
print('Módulo ou resto de divissão:', resto_divisao)

repeticao =  10 * '#'
print('Repetição: 10 * #:', repeticao)


'''
Peculiaridades dos operadores
'''

print()
print('Peculiaridades dos operadores')
concatenacao = 'V' + 'i'+ 't' + 'o'+ 'r'
print(concatenacao)


'''
Precedências dos operadores
'''

# 1º - (n + n)
# 2º - **
# 3º - * / // %
# 4º - + -

print()
print('Precedências dos operadores')
conta_um = 1 + 1 ** 5 + 5
print(conta_um)

conta_dois = (1 + 1) ** (5 + 5)
print(conta_dois)