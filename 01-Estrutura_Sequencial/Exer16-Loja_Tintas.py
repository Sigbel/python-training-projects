"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço
total.
"""

metros_quadrados = float(input("Digite quantos metros quadrados vão ser pintados: "))

quantidade = metros_quadrados/(18*3)
exata = round(quantidade+0.5)

print(f"A quantidade de latas vai ser: {exata}")
print(f"O valor pago será: {exata*80}")

