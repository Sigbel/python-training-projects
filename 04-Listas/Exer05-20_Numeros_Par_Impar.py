"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os 
números IMPARES no vetor impar. Imprima os três vetores.
"""

par = []
impar = []
numeros = []

for n in range(20):
    num = int(input(f"Digite o {n+1}º número: "))
    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f"Números: {numeros}")
print(f"Pares: {par}")
print(f"Impares: {impar}")
