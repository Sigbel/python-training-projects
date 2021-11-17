"""
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três 
argumentos.
"""

def soma_args(n1,n2,n3):
    return f'A soma é dos números é {n1 + n2 + n3}'

n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
n3 = float(input('Digite o 3º número: '))

print(soma_args(n1,n2,n3))
