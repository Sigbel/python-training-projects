"""
Exercício 11 - Conversão de Fahrenheit para Celsius

Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

fahrenheit = float(input("Digite a temperatura em ºF: "))
conversao = 5*((fahrenheit-32)/9)

print(f"A temperatura em graus Celsius é: {conversao:.2f}")

