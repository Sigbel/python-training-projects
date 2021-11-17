"""
Faça um programa para imprimir:

    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n

para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a 
n-ésima linha.

"""

def n_esimo(num):
    lista_temp = []
    for c1 in range(num+1):
        for c2 in range(c1):
            lista_temp.append(c1)
        for c3 in lista_temp:
            if c3 == lista_temp[-1]:
                print(c3, end=' ')
        if c1 != 0: 
            print()
        c3 = 0
        lista_temp = []

n = int(input('Informe um número: '))
n_esimo(n)
