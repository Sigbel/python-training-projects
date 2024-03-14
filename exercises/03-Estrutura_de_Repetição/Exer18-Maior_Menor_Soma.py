"""
Exercício 18 - Maior e Menor Soma

Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a 
soma dos valores.
"""

qtde_conjunto = int(input("Digite a quantidade de termos: "))

menor = 0
maior = 0
soma = 0
c = 0

print()
for n in range(qtde_conjunto):
    num = int(input(f"Digite o {n+1}º número: "))
    while c < 1:
        menor = num
        c +=1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma = soma + num

print()
print(f"O maior número é: {maior}\nO menor número é: {menor}\nA soma de todos os números é: {soma}")
