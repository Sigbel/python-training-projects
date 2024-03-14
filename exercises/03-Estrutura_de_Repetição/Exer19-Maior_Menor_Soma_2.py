"""
Exercício 19 - Maior e Menor Soma (2)

Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

qtde_conjunto = int(input("Digite a quantidade de termos: "))

menor = 0
maior = 0
soma = 0
c = 0

print()
for n in range(qtde_conjunto):
    num = int(input(f"Digite o {n+1}º número: "))
    while num < 0 or num > 1000:
        num = int(input(f"Por favor, digite um número entre 0 e 1000.\nTente novamente: "))
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
