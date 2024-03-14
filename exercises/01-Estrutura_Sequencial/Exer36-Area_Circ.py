"""
Exercício 36 - Área do Círculo

Faça um programa que retorne a área do círculo. Forneça o raio.
"""

from math import pi

raio = float(input("Digite o raio do circulo: "))

area = pi * raio**2

print(f"A área do circulo é: {area:.2f}")