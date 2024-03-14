"""
Exercício 21 - Caixa Eletrônico

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
 uma nota de 5 e quatro notas de 1.
"""

valor_saque= int(input("Digite o valor do saque: "))

valor_saque_temp = valor_saque
contador100 = 0
contador50 = 0
contador10 = 0
contador5 = 0
contador1 = 0
while valor_saque_temp > 0:
    if valor_saque_temp >= 100:
        while valor_saque_temp >= 100:
            valor_saque_temp = valor_saque_temp - 100
            contador100 += 1
    elif 50 <= valor_saque_temp < 100:
        while 50 < valor_saque_temp < 100:
            valor_saque_temp = valor_saque_temp - 50
            contador50 += 1
    elif 10 <= valor_saque_temp < 50:
        while 10 < valor_saque_temp < 50:
            valor_saque_temp = valor_saque_temp - 10
            contador10 += 1
    elif 5 <= valor_saque_temp < 10:
        while 5 < valor_saque_temp < 10:
            valor_saque_temp = valor_saque_temp - 5
            contador5 += 1
    else:
        while valor_saque_temp > 0:
            valor_saque_temp = valor_saque_temp - 1
            contador1+= 1

print(f"VALOR SACADO: R${valor_saque}\nNotas de 100: {contador100}\nNotas de 50: {contador50}\nNotas de 10: {contador10}\nNotas de 5: {contador5}\nNotas de 1: {contador1}")