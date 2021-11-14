"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""

num = int(input("Digite um número de 1 a 7: "))

if num == 1:
    print("O dia é domingo.")
elif num == 2:
    print("O dia é segunda.")
elif num == 3:
    print("O dia é terça.")
elif num == 4:
    print("O dia é quarta.")
elif num == 5:
    print("O dia é quinta.")
elif num == 6:
    print("O dia é sexta.")
elif num == 7:
    print("O dia é sábado.")
else:
    print("Digite um número válido!")