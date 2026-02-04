'''
Docstring for python_basic.aulas.aula005

Introsução ás f-strings e método format
'''

nome = 'Vitor'
idade = 29
altura = 1.80

texto_um = f'Olá, meu nome é {nome}, tenho {idade} anos, tenho {altura:.2f} de altura.'

print(texto_um)

'''
Método format
'''

print()

a = 'A'
b = 'B'
c = 1.1
string = 'a={par_um} b={par_dois} c={par_tres}'


formato = string.format(
    par_um=a, par_dois=b, par_tres=c
)


print(formato)