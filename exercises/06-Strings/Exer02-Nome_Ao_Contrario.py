"""
Exercício 2 - Nome ao Contrário

Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o 
nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o 
usuário pode digitar letras maiúsculas ou minúsculas.
"""

nome = str(input('Digite seu nome [Maiúscula ou Minúscula]: ')).upper()

temp = []
for c1 in nome:
    temp.append(c1)

print(''.join(temp[::-1]))
