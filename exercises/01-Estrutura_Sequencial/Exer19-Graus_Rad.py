"""
Exercício 19 - Conversão de Graus em Radianos

Faça um programa que peça a medida em graus e retorne e m radianos.
"""

from math import pi

graus = float(input("Digite os graus: "))

rad = (graus*pi)/180

print(f"O valor em radianos é: {rad:.2f} ")