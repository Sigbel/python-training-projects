"""
Exercício 23 - Número Inteiro ou Decimal

Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
arredondamento.
"""

num = input("Digite um número: ")

try:
    num = int(num)
except:
    try:
        num = float(num)
    except:
        print("Erro")
if type(num) == int:
    print("Número inteiro!")
elif type(num) == float:
    print("Número Decimal")