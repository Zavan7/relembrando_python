'''
Docstring for python_basic.exercicios.exercicio002

Exercício IMC
'''

peso = float(input('Digite seu peso, em kg: '))
altura = float(input('Digite sua altura, em metros: '))

imc = peso / (altura * altura)

print(f'Seu IMC é: {imc:.2f} kg/m²')