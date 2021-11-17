"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira
função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre 
todos os valores PARES sorteados pela função anterior.
"""

from random import randint
from time import sleep
numeros = []

def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(5):
        numero = randint(0, 10)
        print(f'{numero} ', end='', flush=True)
        sleep(0.4)
        numeros.append(numero)
    print('PRONTO!')

def somaPar():
    sorteia()
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}')

somaPar()