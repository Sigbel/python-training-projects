"""
Exercício 20 - Conversão de Radianos em Graus

Faça um programa que peça a medida em radianos e retorne em graus.
"""

from math import pi

rad = float(input("Digite o valor em radianos: "))

graus = (rad*180)/pi

print(f"O valor em graus é: {graus:.2f} ")