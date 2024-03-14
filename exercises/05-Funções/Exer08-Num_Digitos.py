"""
Exercício 8 - Número de Digitos

Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""

def quantidade(num):
    num = str(num)
    return f'Quantidade de digitos: {len(num)}'

# Programa Principal
numero = int(input('Digite um número: '))
print(quantidade(numero))
