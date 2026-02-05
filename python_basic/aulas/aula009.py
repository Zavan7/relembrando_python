'''
Docstring for python_basic.aulas.aula009

Interpolação de strings
'''

# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)

nome = 'Vitor'
valor = 10.95
variavel = '%s, tem um energético que custou R$ %f' % (nome, valor)
exadecial = 1780

print(variavel)
print ('O exadecial de %d, é %08X' % (exadecial, exadecial))