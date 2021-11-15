"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que 
gere a série até que o valor seja maior que 500.
"""

termo_1 = 0
termo_2 = 1
soma = 0
c = 0

print(f"Sequência: {termo_1}, {termo_2}",end=" ")
while soma < 500:
    soma = termo_1 + termo_2
    termo_1 = termo_2
    termo_2 = soma
    c += 1
    print(f", {soma}",end=" ")
