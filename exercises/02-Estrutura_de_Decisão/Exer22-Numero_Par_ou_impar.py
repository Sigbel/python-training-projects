"""
Exercício 22 - Número Par ou Ímpar

Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo
(resto da divisão).
"""

num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
    print("O número é par!")
else:
    print("O número é ímpar!")