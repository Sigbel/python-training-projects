"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""

num_notas = int(input("Digite a quantidade de notas: "))

soma = 0

for n in range(num_notas):
    nota = float(input(f"Digite a {n+1}ª nota: "))
    soma = soma + nota

media = soma / num_notas

print(f"A média é: {media}")
