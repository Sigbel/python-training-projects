"""
    Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
    Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

from time import sleep

def maior(*args):
    print('-='*25)
    print('Analisando os valores passados...')
    m = 0
    for n in args:
        print(f'{n} ', end='', flush=True)
        if n > m:
            m = n
        sleep(0.3)
    print(f'Foram informados {len(args)} valores ao todo.')
    print(f'O maior valor informado foi {m}')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
