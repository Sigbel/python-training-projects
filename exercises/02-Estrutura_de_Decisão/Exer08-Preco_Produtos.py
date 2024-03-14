"""
Exercício 8 - Preço dos Produtos

Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

num_01 = float(input("Digite o preço do 1º produto: "))
num_02 = float(input("Digite o preço do 2º produto: "))
num_03 = float(input("Digite o preço do 3º produto: "))

if num_01 < num_02 and num_01 < num_03:
    print(f"O mais barato é o produto 1º produto")
elif num_02 < num_01 and num_02 < num_03:
    print(f"O mais barato é o produto 2º produto")
else:
    print(f"O mais barato é o produto 3º produto")