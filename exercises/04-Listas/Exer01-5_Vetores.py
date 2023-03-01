"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""

lista = []

for n in range(5):
    num = float(input(f"Digite o {n+1}º número: "))
    lista.append(num)

for numero in lista:
    print(numero, end = " ")
