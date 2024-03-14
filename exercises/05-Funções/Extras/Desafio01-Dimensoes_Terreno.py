"""
Desafio 1 - Dimensões do Terreno

Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e 
comprimento) e mostre a área do terreno
"""

print('Controle de Terrenos')
print('-'*20)

def area(largura, comprimento):
    a = largura*comprimento
    print(f'A área do terreno é {largura}x{comprimento} igual a: {a} m²')

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area(largura, comprimento)
