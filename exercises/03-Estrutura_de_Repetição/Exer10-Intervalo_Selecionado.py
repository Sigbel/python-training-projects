"""
Exercício 10 - Intervalo Selecionado

Faça um programa que receba dois números inteiros e gere os números inteiros que estão no 
intervalo compreendido por eles.
"""

num_01 = int(input("Digite o 1º número: "))
num_02 = int(input("Digite o 2º número: "))
print()
print("O intervalo selecionado inclui os seguintes números: ")
for n in range(num_01,num_02+1):
    print(n, end=" ")
