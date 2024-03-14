"""
Exercício 2 - 10 Vetores Inversos

Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

lista = []

for n in range(10):
    num = float(input(f"Digite o {n+1}º valor: "))
    lista.append(num)

print(lista)
print(lista[::-1])
