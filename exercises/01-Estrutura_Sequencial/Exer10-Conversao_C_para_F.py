"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""

celsius = float(input("Digite a temperatura em ºC: "))
conversao = ((9/5)*celsius) + 32

print(f"A temperatura em graus Celsius é: {conversao:.2f}")

