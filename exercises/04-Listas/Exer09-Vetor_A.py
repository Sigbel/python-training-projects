"""
Exercício 9 - Vetor A

Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos 
do vetor.
"""

vetor_A = []
soma = 0

for n in range(10):
    num = float(input(f"Digite {n+1}º número: "))
    vetor_A.append(num)

for numeros in vetor_A:
    quadrado = numeros**2
    soma += quadrado

print(soma)
