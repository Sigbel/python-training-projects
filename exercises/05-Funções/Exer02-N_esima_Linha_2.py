"""
Exercício 2 - N..esima Linha (2)

Faça um programa para imprimir:
 
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n

para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a 
n-ésima linha.
"""


def n_esimo(num):
    
    lista_temp = []  
    for c1 in range(num+1):
        c2 = 1
        while c2 <= c1:
            lista_temp.append(c2)
            c2 += 1
        for c3 in lista_temp:            
            print(c3, end=' ')
        if c1 != 0:
            print()

        c3 = 0
        lista_temp = []


n = int(input('Informe um número: '))
n_esimo(n)
