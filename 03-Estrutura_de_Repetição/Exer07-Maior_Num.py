"""
Faça um programa que leia 5 números e informe o maior número.
"""

maior = 0

for n in range(5):
    num = int(input(f"Digite o {n+1}º número: "))
    if num > maior:
        maior = num

print(f"O maior número digitado foi: {maior}")
