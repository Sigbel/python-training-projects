"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.
"""

num_1 = int(input("Digite o 1º número inteiro: "))
num_2 = int(input("Digire o 2º número inteiro: "))
num_3 = float(input("Digire o número real: "))

print(f"O produto do dobro do primeiro com a metade do segundo é: {(num_1*2)*(num_2/2)}")
print(f"A soma do triplo do primeiro com o terceiro é: {(num_1*3)+num_3}")
print(f"O terceiro elevado ao cubo é: {num_3**3:.2f}")