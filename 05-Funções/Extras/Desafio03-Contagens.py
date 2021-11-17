"""
    Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e 
realize a contagem.
    Seu programa tem que realizar realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.
"""

def linha():
    print('-='*20)

def contadores_iniciais():
    linha()
    print('Contagem de 1 até 10 de 1 em 1')
    for c1 in range(0, 11, 1):
        print(f'{c1} ', end='')
    print('Fim!')
    linha()
    print('Contagem de 10 até 0 de 2 em 2')
    for c2 in range(10, -1, -2):
        print(f'{c2} ', end='')
    print('Fim!')
    linha()
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if passo == 0:
        if inicio > fim:
            passo = -1
        else:
            passo = 1 
    linha()
    contador(inicio,fim,passo)

def contador(inicio, fim, passo):
    if passo < 0:
        print(f'Contagem de {inicio} até {fim} de {passo*(-1)} em {passo*(-1)}')
        for n in range(inicio, fim-1, passo):
            print(f'{n} ', end='')
    else:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for n in range(inicio, fim+1, passo):
            print(f'{n} ', end='')
    print('Fim!')

#Todo execução do código vai sempre retornar contagem de 1 a 10 e 10 a 0
contadores_iniciais()
