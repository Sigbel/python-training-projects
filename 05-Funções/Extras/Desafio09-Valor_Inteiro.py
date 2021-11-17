"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do 
Python, só que fazendo a validação para aceitar apenas um valor númerico.

Ex:
n = leiaInt('Digite um n')
"""

def leiaInt(msg):
    n = input(msg)
    while not n.isnumeric():
        n = input('\033[31mERRO! digite um número inteiro válido.\033[0m\nDigite um número: ')
    return n

# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
