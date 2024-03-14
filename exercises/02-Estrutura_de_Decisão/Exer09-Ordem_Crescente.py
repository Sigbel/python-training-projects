"""
Exercício 9 - Ordem Crescente

Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

num_01 = float(input("Digite o 1º Número: "))
num_02 = float(input("Digite o 2º Número: "))
num_03 = float(input("Digite o 3º Número: "))
maior = 0
intermediario = 0
menor = 0

#Maior
if num_01 > num_02 and num_01 > num_03:
    maior = num_01
elif num_02 > num_01 and num_02 > num_03:
    maior = num_02
else:
    maior = num_03

#Intermediario
if num_02 < num_01 < num_03:
    intermediario = num_01
elif num_01 < num_02 < num_03:
    intermediario = num_02
else:
    intermediario = num_03

#Menor
if num_01 < num_02 and num_01 < num_03:
    menor = num_01
elif num_02 < num_01 and num_02 < num_03:
    menor = num_02
else:
    menor = num_03

print()
print(f"Em ordem crescente os números ficam organizados da seguinte forma: {menor}, {intermediario}, {maior}")