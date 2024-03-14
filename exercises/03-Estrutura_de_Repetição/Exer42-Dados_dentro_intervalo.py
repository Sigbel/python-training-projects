"""
Exercício 42 - Dados Dentro do Intervalo

Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles 
estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá 
terminar quando for lido um número negativo.
"""

c_1 = 0
c_2 = 0
c_3 = 0
c_4 = 0

while True:
    num = int(input("Digite um número: "))
    if 0 <= num <= 25:
        c_1 += 1
    elif 26 <= num <= 50:
        c_2 += 1 
    elif 51 <= num <= 75:
        c_3 += 1 
    elif 76 <= num <= 100: 
        c_4 += 1
    elif num < 0:
        break

print("Quantidade de números dentro dos intervalos:")
print(f"[0-25] - {c_1}")
print(f"[26-50] - {c_2}")
print(f"[51-75] - {c_3}")
print(f"[76-100] - {c_4}")
