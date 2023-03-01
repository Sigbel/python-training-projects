"""
Faça um Programa que leia três números e mostre o maior deles.
"""

num_01 = float(input("Digite o 1º Número: "))
num_02 = float(input("Digite o 2º Número: "))
num_03 = float(input("Digite o 3º Número: "))

if num_01 > num_02 and num_01 > num_03:
    print(f"O maior número é: {num_01}")
elif num_02 > num_01 and num_02 > num_03:
    print(f"O maior número é: {num_02}")
else:
    print(f"O maior número é: {num_03}")