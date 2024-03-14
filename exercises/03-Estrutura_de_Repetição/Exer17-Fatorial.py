"""
Exercício 17 - Fatorial

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120
"""

termo_1 = int(input("Digite um número para calcular o fatorial: "))
termo_1_temp = termo_1
fatorial = 0

for n in range(termo_1-1):
    termo_seg = termo_1 - (n+1)
    fatorial = termo_1_temp * termo_seg
    termo_1_temp = fatorial

print(fatorial)
