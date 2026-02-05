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

print('\n__ Mais sobre f-strings__\n')

'''
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
'''

variavel_um = 'ABC'
variavel_dois = 1000.986485

print(f'{variavel_um}')
print(f'{variavel_um:>10}')
print(f'{variavel_um:<10}')
print(f'{variavel_um:#^10}')
print(f'{variavel_dois:+,.2f}')
print(f'{variavel_um!r}')
print(f'{variavel_um!s}')
print(f'{variavel_um!a}')