"""
Exercício 10 - Peso ideal mediante altura

Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
a. Para homens: (72.7*h) - 58
b. Para mulheres: (62.1*h) - 44.7
"""

altura = float(input("Digite sua altura: "))

calculoH = (72.7*altura) - 58
calculoM = (62.1*altura) - 44.7

print(f"Se você for homem, seu peso ideal é {calculoH:.2f} \nSe você for mulher, seu peso ideal é: {calculoM:.2f}")