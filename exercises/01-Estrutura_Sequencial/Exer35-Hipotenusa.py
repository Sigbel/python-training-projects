"""
Exercício 35 - Hipotenusa

Faça um programa que retorne a hipotenusa do triângulo. Forneça os catetos.
"""

from math import sqrt

a = float(input("Digite o valor do cateto a: "))
b = float(input("Digite o valor do cateto b: "))

hip = sqrt(a**2 + b**2)

print(f"A hipotenusa do triângulo é: {hip:.2f}")