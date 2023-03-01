"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de 
caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""

def pn(num):
    if num > 0:
        return 'P'
    else:
        return 'N'

n = float(input('Digite um número: '))
print(pn(n))

