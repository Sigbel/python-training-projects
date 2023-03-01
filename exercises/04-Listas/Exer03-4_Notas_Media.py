"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

notas = []
soma = 0

for n in range(4):
    nota = float(input(f"Digite a {n+1}ª nota: "))
    notas.append(nota)
    soma += nota

print(f"Notas:\n{notas}")
print(f"Média das notas {soma/4}")
