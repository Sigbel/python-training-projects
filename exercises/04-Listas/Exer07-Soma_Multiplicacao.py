"""
Exercício 7 - Soma da Multiplicação

Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

vetor = []
soma = 0
multiplicacao = 1

for c1 in range(5):
    num = int(input(f"Digite o {c1+1}º número: "))
    soma += num
    multiplicacao *= num
    vetor.append(num)

print(f"Números: {vetor}")
print(f"Soma dos números: {soma}")
print(f"Multiplicação dos números: {multiplicacao}")
