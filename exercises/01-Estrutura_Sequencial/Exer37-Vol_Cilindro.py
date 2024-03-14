"""
Exercício 37 - Volume do Cilindro

Faça um programa que retorne o volume do cilindro. Forneça a altura e o raio.
"""

from math import pi

altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))

vol = pi* raio**2 * altura

print(f"O volume do cilindro é: {vol:.2f}")