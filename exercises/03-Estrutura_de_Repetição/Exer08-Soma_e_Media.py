"""
Exercício 9 - Soma e Média

Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

soma = 0

for n in range(5):
    num = float(input(f"Digite o {n+1}º número: "))
    soma = num + soma
media = soma / 5

print()
print(f"A soma dos números é {soma}\nA média é {media}")
