"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a 
quantidade de números impares.
"""

contador_par = 0
contador_impar = 0
contador = 0

for n in range(10):
    num = int(input(f"Digite o {n+1}º número: "))
    if num % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1

print()
print(f"A quantidade de números pares é: {contador_par}\nA quantidade números ímpares é: {contador_impar}")
