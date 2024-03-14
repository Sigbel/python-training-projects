"""
Desafio 2 - Funçao Escreva

Faça um programa que tenha uma função chamada escreva(), que recaba um texto qualquer como parâmetro e mostre
uma mensagem com tamanho adaptável.
"""

def escreva(msg):
    print('~'*(len(msg)+4))
    print(f'{msg}'.center(len(msg)+4))
    print('~'*(len(msg)+4))

escreva('Olá, Mundo')